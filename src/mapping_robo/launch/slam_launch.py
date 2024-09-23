import os
from launch import LaunchDescription
from launch_ros.actions import Node
# Pfad zum Home-Verzeichnis des aktuellen Benutzers
home_dir = os.path.expanduser("~")

# Pfad zum Verzeichnis 'config' in Ihrem Paket 'mapping_robo'
config_dir = os.path.join(home_dir, 'mapping_ws-main', 'src', 'mapping_robo', 'config')
def generate_launch_description():
    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            
            arguments=[
                '-configuration_directory',
                config_dir,
                '-configuration_basename',
                'mapper_params_online_async.yaml'
            ]
        )

    ])
