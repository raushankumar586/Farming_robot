#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64 , Int8, String

joint1_pub = rospy.Publisher(
    "/joint1_position_controller/command", Float64, queue_size=2)
joint2_pub = rospy.Publisher(
    "/joint2_position_controller/command", Float64, queue_size=10)
joint3_pub = rospy.Publisher(
    "/joint3_position_controller/command", Float64, queue_size=2)
joint4_pub = rospy.Publisher(
    "/joint4_position_controller/command", Float64, queue_size=2)
joint5_pub = rospy.Publisher(
    "/joint5_position_controller/command", Float64, queue_size=2)
joint11_pub = rospy.Publisher(
    "/joint11_position_controller/command", Float64, queue_size=2)
joint12_pub = rospy.Publisher(
    "/joint12_position_controller/command", Float64, queue_size=2)
joint13_pub = rospy.Publisher(
    "/joint13_position_controller/command", Float64, queue_size=2)
joint14_pub = rospy.Publisher(
    "/joint14_position_controller/command", Float64, queue_size=2)
joint15_pub = rospy.Publisher(
    "/joint15_position_controller/command", Float64, queue_size=2)

left_top = rospy.Publisher(
    "/top_left_gripper_joint_controller/command", Float64, queue_size=2)
left_down = rospy.Publisher(
    "/down_left_gripper_joint_controller/command", Float64, queue_size=2)

right_top = rospy.Publisher(
    "/top_right_gripper_joint_controller/command", Float64, queue_size=2)
right_down = rospy.Publisher(
    "/down_right_gripper_joint_controller/command", Float64, queue_size=2)



hand  = 1.0 

def position_control(j1=0,j2=0,j3=0,j4=0,j5=0,lt=0, ld=0):
    
    joint1_pub.publish(j1)
    joint2_pub.publish(j2)
    joint3_pub.publish(j3)
    joint4_pub.publish(j4)
    joint5_pub.publish(j5)
    left_top.publish(lt)
    left_down.publish(ld)
    

def gripper_control(data):
    left_top.publish(data.data)
    left_down.publish(data.data)
    rospy.logwarn("gripper  data {}".format(data.data))
    


def position_control_left(j11=0,j12=0,j13=0,j14=0,j15=0):
    joint11_pub.publish(j11)
    joint12_pub.publish(j12)
    joint13_pub.publish(j13)
    joint14_pub.publish(j14)
    joint15_pub.publish(j15)

def position_control_right(j1=0,j2=0,j3=0,j4=0,j5=0):

    joint1_pub.publish(j1)
    joint2_pub.publish(j2)
    joint3_pub.publish(j3)
    joint4_pub.publish(j4)
    joint5_pub.publish(j5)

def which_hand(hands):
   hand= hands.data


def callback(GST): 
    global hand
    Gesture= GST.data 
    print('Entering if condition')

    
    if Gesture == 1.0 :
        # position_control()
        if hand== 1.0:
            position_control_left(0.36,-0.93,-0.65,-0.65,-0.33)
        elif hand == 2.0 :
            position_control_right(0.36,0.93,0.65,0.65,0.33)
        else :
            position_control(0.36,0.93,0.65,0.65,0.33)
    elif Gesture == 2.0 :
         position_control()
         
    elif Gesture == 3.0:
        position_control(-0.10, 1.57, 0.0, 1.57, 0.25, 5.0, 5.0)
    elif Gesture == 4.0:
        position_control(0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 3.0)
    elif Gesture == 5.0:
        position_control(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    else:
        print('Exited')
    pass
    #rate.sleep()

def subscriber():
    
    print('I am in')
    rospy.init_node("control_hands", anonymous=True)
    global rate
    rate = rospy.Rate(10)
    rospy.Subscriber("/right_hands",Float64,callback)
    rospy.Subscriber("/single_hand",Float64, which_hand)
    rospy.Subscriber("/gripper",Float64, gripper_control)
    print('After subscribe')
    rospy.spin()


if __name__ == '__main__':
    try:
        print('before subscribe')
        subscriber()
    except rospy.ROSInterruptException:
        pass
