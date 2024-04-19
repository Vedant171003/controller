#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    controller_node = Node(
        package="hb_task_1b",           # Replace with your package name
        executable="controller.py",             # Replace with your controller script name
        name="controller_node"                  # Optional name for the node
    )

    service_node = Node(
        package="hb_task_1b",           # Replace with your package name
        executable="service_node.py",           # Replace with your service node script name
        name="service_node"                    # Optional name for the node
    )

    ld.add_action(controller_node)
    ld.add_action(service_node)

    return ld
