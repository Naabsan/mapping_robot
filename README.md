ROS2 Mapping Robot Project

Overview
This project is the final result of a study project. The aim was to build a robot capable of mapping its environment in 2D using an RPLIDAR A1 and Raspberry Pi 4, integrating ROS2 for control and visualization.

![image](https://github.com/user-attachments/assets/f0f970b5-1803-4d3d-a4fb-0eb2b8660309)


Features
2D Mapping: The robot is equipped with a RPLIDAR A1 sensor, providing 360° coverage with a 6-meter range, allowing for accurate mapping of the surroundings.
ROS2 Integration: The robot is fully controlled using ROS2 and its packages, enabling real-time data visualization in RViz2.
Autonomous Power: Powered by an Intenso Powerbank S10000, providing mobile energy for up to 5 hours of operation.
Remote Operation: Secure Shell (SSH) allows remote management and monitoring of the robot via a laptop.
SLAM Capabilities: The robot uses the Cartographer SLAM algorithm for simultaneous localization and mapping (SLAM) without the need for odometry or IMU data.
Hardware Components
Raspberry Pi 4: Central processing unit, running Ubuntu 22.04 (Jammy) with ROS2 Humble distribution.
RPLIDAR A1: Low-cost 2D LIDAR sensor for environment scanning.
Intenso Powerbank S10000: Provides portable energy for the Raspberry Pi and LIDAR.
Elegoo Car Kit: Serves as the platform for mounting the robot's components.
Software
ROS2 (Robot Operating System 2): Framework for robot software development, enabling communication between robot components.
Includes packages for LIDAR integration and visualization in RViz2.
SLAM with Cartographer.
RViz2: Visualization tool for real-time monitoring of the robot’s mapping process.
SSH: Remote access and control over the Raspberry Pi for robot management and data collection.
Setup and Installation
1. Hardware Assembly
Mount the Raspberry Pi, RPLIDAR, and powerbank onto the Elegoo platform as described in the project documentation.
Connect the components via USB and power cables.
2. Software Setup
Install Ubuntu 22.04 (Jammy) on the Raspberry Pi 4.
Set up ROS2 Humble distribution.
Install the necessary ROS2 packages for LIDAR sensor integration and SLAM.
Set up SSH for remote control.
3. Running the Robot
Use SSH to remotely connect to the Raspberry Pi.
Start ROS2 nodes to launch the SLAM algorithm and view real-time mapping data in RViz2.
Future Work
Integration of motors for autonomous navigation.
Addition of camera-based object detection using models like YOLO.


