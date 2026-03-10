#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CircleMotion(Node):

    def __init__(self):
        super().__init__('circle_motion')

        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.move_robot)

    def move_robot(self):

        msg = Twist()

        msg.linear.x = 0.5
        msg.angular.z = 0.5

        self.publisher_.publish(msg)

        self.get_logger().info("Robot moving in circle")


def main(args=None):

    rclpy.init(args=args)

    node = CircleMotion()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()