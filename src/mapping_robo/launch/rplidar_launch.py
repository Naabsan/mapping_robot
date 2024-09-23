from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rplidar_ros',
            executable='rplidar_composition',  
            name='rplidarNode', 
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
        )

    ])
