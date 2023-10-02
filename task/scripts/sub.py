#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.logininfo("Received data: %s", data.data)
def listen():
    rospy.init_node("Subscriber_Node", anonymous = True)
    rospy.Subsciber("scan", String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listen()
    except rospy.ROSInterruptException:
        pass
