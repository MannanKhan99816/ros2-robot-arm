ROS2 R2D2 Robot Simulation

This project simulates a simple R2D2-like robot using ROS2 Humble, URDF, and RViz.

Features

URDF robot model

Robot visualization in RViz

Circular robot motion using Python

TF-based robot movement

ROS2 nodes and publishers

Technologies

ROS2 Humble

Python

URDF

RViz

How to Run
Start robot model

ros2 run robot_state_publisher robot_state_publisher src/urdf_tutorial/urdf/r2d2_robot.urdf

Start joint state GUI

ros2 run joint_state_publisher_gui joint_state_publisher_gui

Start RViz

rviz2

Run circular motion

python3 src/my_package/src/circle_motion.py