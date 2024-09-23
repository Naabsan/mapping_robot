import os
from launch import LaunchDescription
from launch_ros.actions import Node

# Pfad zum Home-Verzeichnis des aktuellen Benutzers
home_dir = os.path.expanduser("~")

# Pfad zum Verzeichnis 'urdf' in Ihrem Paket 'mapping_robo'
urdf_dir = os.path.join(home_dir, 'mapping_ws-main', 'src', 'mapping_robo', 'urdf')

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[
                {'robot_description': open(os.path.join(urdf_dir, 'torobo.urdf')).read()}
            ]
        ),
    ])

