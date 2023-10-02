#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Published message: %s", data.data)
    
def listener():

    
    rospy.init_node('sub', anonymous=True)

    rospy.Subscriber("chitchat", String, callback)
    
    rospy.spin()


if __name__ == '__main__':
	listener()
	
