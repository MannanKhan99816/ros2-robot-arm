from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    pkg_path = get_package_share_directory('urdf_tutorial')
    urdf_path = os.path.join(pkg_path, 'urdf', '01-simple-link.urdf')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': open(urdf_path).read()
            }]
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            output='screen'
        )
    ])
