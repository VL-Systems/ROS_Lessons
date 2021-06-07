#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped


def subs():
    rospy.init_node('mark1_pose')
    sub = rospy.Subscriber('amcl_pose', PoseWithCovarianceStamped, callbeck)
    rospy.spin()


def callbeck(msg):
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    z = msg.pose.pose.position.z
    rospy.loginfo(x)
    rospy.loginfo(y)
    rospy.loginfo(z)


if __name__ == '__main__':
    try:
        subs()
    except rospy.ROSInterruptException:
        pass
