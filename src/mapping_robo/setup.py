from setuptools import setup

package_name = 'mapping_robo'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/cartographer_launch.py', 'launch/rplidar_launch.py', 'launch/rviz_launch.py','launch/all_launch.py', 'launch/state_launch.py', 'launch/slam_launch.py']),
    ],
    install_requires=[
        'setuptools',
    ],
    zip_safe=True,
    author='tonait01',
    author_email='tonait01@hs-esslingen.de',
    maintainer='tonait01',
    maintainer_email='tonait01@hs-esslingen.de',
    description='This package does it all, launch robot description, rplidar and SLAM',
    license='TODO: Lizenzangabe',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
             
        ],
    },
)

