#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool
     
class NumberCourierNode(Node):
    def __init__(self):
        self.counter_ = 0
        super().__init__("number_courier")
        self.subscriber_ = self.create_subscription(Int64, "number", self.counter_def, 10)

        self.publisher_ = self.create_publisher(Int64, "number_count", 10)
        
        self.server_ = self.create_service(SetBool, "reset_number_count", self.reset_number)

        self.get_logger().info("Number Courier is initialized")

    def counter_def(self, msg):
        self.counter_ += msg.data
        new_msg = Int64()
        new_msg.data = self.counter_
        self.publisher_.publish(new_msg)
        
    def reset_number(self, request, response):
        if request.data == True:
            self.counter_ = 0
            response.message = "Counter nulled successfully!"
            response.success = True
        else:
            response.message = "Recieved false!"
            response.success = False
        return response
    
     
     
def main(args=None):
    rclpy.init(args=args)
    node = NumberCourierNode()
    rclpy.spin(node)
    rclpy.shutdown()
     
     
if __name__ == "__main__":
    main()