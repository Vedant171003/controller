Holonomic Drive Robot Navigation
This project was developed as part of a team of three for a competition involving the implementation of a simple controller to navigate three different holonomic drive simulated robots to a series of desired poses using localization in the Gazebo (ROS) simulator.

Overview
The objective of the competition was to make the localization and control of the holonomic drive robots more realistic than in previous tasks. To achieve this, we utilized image processing techniques with OpenCV to localize the robots using an overhead camera and Aruco markers. Additionally, we implemented inverse kinematics to control the robot’s movement more accurately.

Features
Holonomic Drive Simulation: The project includes a Gazebo simulation environment with holonomic drive robots.
Image Processing Localization: Utilizing OpenCV and Aruco markers for robot localization.
Inverse Kinematics Control: Implementing inverse kinematics to control the robot's movement accurately.
ROS2 Workspace: The project is organized as a proper ROS2 workspace for seamless integration and development.
Installation
To use this project, follow these steps:

Clone the repository into your ROS2 workspace:
bash
Copy code
cd ros2_workspace/src
git clone https://github.com/yourusername/holonomic_drive_robot_navigation.git
Build your ROS2 workspace:
bash
Copy code
cd ros2_workspace
colcon build
Usage
Launch the simulation environment with the following command:

bash
Copy code
ros2 launch holonomic_drive_robot_navigation gazebo.launch.py
This will launch Gazebo with the holonomic drive robot simulation.

Additional Information
For more detailed information on the project setup, usage instructions, or any inquiries, please refer to the documentation or contact the project maintainers.
