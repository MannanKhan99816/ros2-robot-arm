from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
import os


def generate_launch_description():

    urdf_path = os.path.join(
        os.getenv('HOME'),
        'ros2_ws/src/gazebo_tutorial/urdf/teslabot.urdf'
    )

    gazebo = ExecuteProcess(
        cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
        output='screen'
    )

    robot_state_pub = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': open(urdf_path).read()}]
    )

    return LaunchDescription([
        gazebo,
        robot_state_pub
    ])