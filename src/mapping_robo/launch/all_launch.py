import os
from launch import LaunchDescription
from launch_ros.actions import Node

# Pfad zum Home-Verzeichnis des aktuellen Benutzers
home_dir = os.path.expanduser("~")

# Pfad zum Verzeichnis 'config' in Ihrem Paket 'mapping_robo'
config_dir = os.path.join(home_dir, 'mapping_ws-main', 'src', 'mapping_robo', 'config')

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
         Node(
            package='rplidar_ros',
            executable='rplidar_composition', 
            name='rplidarNode',  # Fügen Sie den Knotennamen hinzu
            output='screen',
            parameters=[
                {
                    'serial_port': '/dev/ttyUSB0',  # Anpassen des seriellen Ports
                    'serial_baudrate': 115200,     
                    'frame_id': 'laser',  
                    'inverted': False,  
                    'angle_compensate': True,
                    'scan_mode': 'Standard'
                    
                }
            ]
        ),
                Node(
            package='cartographer_ros',
            executable='cartographer_node',
            name='cartographer_node',
            output='screen',
            arguments=[
                '-configuration_directory',
                config_dir,
                '-configuration_basename',
                'lidar_2d.lua'
            ]
        ),
                Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', 'mapping_robo/config/rviz/rviz_config.rviz']
        ),
    ])

