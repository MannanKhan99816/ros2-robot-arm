import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
import tf2_ros
import math
import time


class CircleMotion(Node):

    def __init__(self):
        super().__init__('circle_motion')

        self.broadcaster = tf2_ros.TransformBroadcaster(self)
        self.timer = self.create_timer(0.05, self.publish_tf)

        self.start_time = time.time()

    def publish_tf(self):

        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "world"
        t.child_frame_id = "axis"

        elapsed = time.time() - self.start_time

        radius = 2.0
        speed = 0.5

        x = radius * math.cos(speed * elapsed)
        y = radius * math.sin(speed * elapsed)

        # position
        t.transform.translation.x = x
        t.transform.translation.y = y
        t.transform.translation.z = 0.0

        # orientation (face direction of motion)
        yaw = speed * elapsed + math.pi/2

        qx = 0.0
        qy = 0.0
        qz = float(math.sin(yaw / 2))
        qw = float(math.cos(yaw / 2))

        t.transform.rotation.x = qx
        t.transform.rotation.y = qy
        t.transform.rotation.z = qz
        t.transform.rotation.w = qw

        self.broadcaster.sendTransform(t)


def main(args=None):

    rclpy.init(args=args)

    node = CircleMotion()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()