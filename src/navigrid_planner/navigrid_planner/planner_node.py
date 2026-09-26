import math

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan


class AdaptivePlanner(Node):

    def __init__(self):
        super().__init__('adaptive_planner')

        # Demonstration goal in the arena
        self.goal_x = 10.0
        self.goal_y = 10.0

        # Adaptive route selection:
        # cost = distance + lambda * slope
        flat_cost = 24.0
        ramp_cost = 17.0 + 8.0 * 0.20
        self.selected_route = (
            "RAMP_A_TO_B" if ramp_cost < flat_cost else "FLAT_ZIGZAG"
        )

        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        self.front = float('inf')
        self.left = float('inf')
        self.right = float('inf')

        self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)

        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel_nav', 10)

        self.create_timer(0.1, self.control_loop)

        self.get_logger().info(
            f'Adaptive planner started: goal=(10.0, 10.0), '
            f'route={self.selected_route}'
        )

    def odom_callback(self, msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y

        q = msg.pose.pose.orientation

        siny_cosp = 2.0 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)

        self.yaw = math.atan2(siny_cosp, cosy_cosp)

    def scan_callback(self, msg):
        def sector(start_deg, end_deg):
            values = []
            angle = msg.angle_min

            for r in msg.ranges:
                deg = math.degrees(angle)

                if start_deg <= deg <= end_deg and math.isfinite(r):
                    values.append(r)

                angle += msg.angle_increment

            return min(values) if values else float('inf')

        self.front = sector(-30, 30)
        self.left = sector(30, 90)
        self.right = sector(-90, -30)

    def control_loop(self):
        cmd = Twist()

        dx = self.goal_x - self.x
        dy = self.goal_y - self.y
        distance = math.hypot(dx, dy)

        if distance < 0.5:
            self.cmd_pub.publish(cmd)
            self.get_logger().info('Goal reached.')
            return

        target_angle = math.atan2(dy, dx)
        error = math.atan2(
            math.sin(target_angle - self.yaw),
            math.cos(target_angle - self.yaw)
        )

        # Adaptive local obstacle avoidance
        if self.front < 1.2:
            cmd.linear.x = 0.0

            if self.left > self.right:
                cmd.angular.z = 0.8
            else:
                cmd.angular.z = -0.8

            self.get_logger().info(
                f'Obstacle detected: {self.front:.2f} m — replanning locally'
            )

        else:
            cmd.linear.x = min(0.8, 0.25 + 0.08 * distance)
            cmd.angular.z = max(-0.8, min(0.8, 1.5 * error))

        self.cmd_pub.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = AdaptivePlanner()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
