from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    robot_description = ParameterValue(
        Command([
            "xacro ",
            "/home/sohini340/navigrid_ws/src/navigrid_description/urdf/navigrid_robot.urdf.xacro"
        ]),
        value_type=str
    )

    return LaunchDescription([
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            output="screen",
            parameters=[
                {"robot_description": robot_description}
            ],
        ),
    ])
