import math

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan


class SafetyNode(Node):

    def __init__(self):
        super().__init__('navigrid_safety')

        self.k = 0.5
        self.d_min = 0.5

        self.speed = 0.0
        self.front_distance = float('inf')
        self.latest_cmd = Twist()

        self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        self.create_subscription(
            Twist, '/cmd_vel_nav', self.cmd_callback, 10
        )

        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        self.create_timer(0.05, self.safety_control)

        self.get_logger().info(
            'NaviGrid Safety Override started: d_safe = k*v^2 + d_min'
        )

    def odom_callback(self, msg):
        self.speed = abs(msg.twist.twist.linear.x)

    def scan_callback(self, msg):
        ranges = []

        angle = msg.angle_min
        for r in msg.ranges:
            if -math.radians(30) <= angle <= math.radians(30):
                if math.isfinite(r):
                    ranges.append(r)
            angle += msg.angle_increment

        if ranges:
            self.front_distance = min(ranges)
        else:
            self.front_distance = float('inf')

    def cmd_callback(self, msg):
        self.latest_cmd = msg

    def safety_control(self):
        d_safe = self.k * (self.speed ** 2) + self.d_min

        output = Twist()

        if self.front_distance < d_safe:
            output.linear.x = 0.0
            output.angular.z = 0.8

            self.get_logger().warn(
                f'SAFETY OVERRIDE | '
                f'd={self.front_distance:.2f}m < '
                f'd_safe={d_safe:.2f}m'
            )
        else:
            output = self.latest_cmd

        self.cmd_pub.publish(output)


def main(args=None):
    rclpy.init(args=args)
    node = SafetyNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
