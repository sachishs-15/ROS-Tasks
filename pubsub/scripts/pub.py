#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chitchat', String, queue_size=10)
    rospy.init_node('publish', anonymous=True)

    pubstr = "Yay!! I've published something"
    
    while not rospy.is_shutdown():
	    pub.publish(pubstr)
	    rospy.loginfo(pubstr)
	    pub.publish(pubstr)
	    rospy.spin()
    

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

