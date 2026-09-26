from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():

    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan',
            '/odom@nav_msgs/msg/Odometry@gz.msgs.Odometry',
            '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
        ],
        output='screen',
    )

    planner = Node(
        package='navigrid_planner',
        executable='planner_node',
        output='screen',
    )

    safety = Node(
        package='navigrid_safety',
        executable='safety_node',
        output='screen',
    )

    return LaunchDescription([
        bridge,
        planner,
        safety,
    ])
