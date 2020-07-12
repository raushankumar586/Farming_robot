#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

joint1_pub = rospy.Publisher(
    "/hands/joint1_position_controller/command", Float64, queue_size=2)
joint2_pub = rospy.Publisher(
    "/hands/joint2_position_controller/command", Float64, queue_size=10)
joint3_pub = rospy.Publisher(
    "/hands/joint3_position_controller/command", Float64, queue_size=2)
joint4_pub = rospy.Publisher(
    "/hands/joint4_position_controller/command", Float64, queue_size=2)
joint5_pub = rospy.Publisher(
    "/hands/joint5_position_controller/command", Float64, queue_size=2)
joint11_pub = rospy.Publisher(
    "/hands/joint11_position_controller/command", Float64, queue_size=2)
joint12_pub = rospy.Publisher(
    "/hands/joint12_position_controller/command", Float64, queue_size=2)
joint13_pub = rospy.Publisher(
    "/hands/joint13_position_controller/command", Float64, queue_size=2)
joint14_pub = rospy.Publisher(
    "/hands/joint14_position_controller/command", Float64, queue_size=2)
joint15_pub = rospy.Publisher(
    "/hands/joint15_position_controller/command", Float64, queue_size=2)


def position_control(j1=0,j2=0,j3=0,j4=0,j5=0,j11=0,j12=0,j13=0,j14=0,j15=0):
    while not rospy.is_shutdown():
        joint1_pub.publish(j1)
        joint2_pub.publish(j2)
        joint3_pub.publish(j3)
        joint4_pub.publish(j4)
        joint5_pub.publish(j5)
        joint11_pub.publish(j11)
        joint12_pub.publish(j12)
        joint13_pub.publish(j13)
        joint14_pub.publish(j14)
        joint15_pub.publish(j15)


def main():
    rospy.init_node("control_hands", anonymous=True)
    position_control(0.0,0.5,0.8,0.4,0.6, -0.0,-0.5,-0.8,-0.4,-0.6)
    #position_control()
    rospy.spin()


if __name__ == '__main__':
    main()
