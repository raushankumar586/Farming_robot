#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64 , Int8, String

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

hand  = 1.0 

def position_control(j1=0,j2=0,j3=0,j4=0,j5=0,j11=0,j12=0,j13=0,j14=0,j15=0):
    
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
# def main():
#     rospy.init_node("control_hands", anonymous=True)
#     global rate
#     rate = rospy.Rate(5)
    
    # while not rospy.is_shutdown():
    #     for i in range(20):
            
            
    #         position_control(0,3,6,-4,0 -0,-1,4,-10,-20)
    #         rate.sleep() 
    #         print ('Completed first round')

    #     for i in range(20):
            
    #         position_control()
    #         rate.sleep() 
    #         print ('Full rotation completed')


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
            position_control(0.36,0.93,0.65,0.65,0.33, 0.36,-0.93,-0.65,-0.65,-0.33)
    elif Gesture == 2.0 :
         position_control()
         
    elif Gesture == 3.0 :
        position_control(-0.10,1.57, 0.0,1.57,0.25, 0.10,-1.57,-0.0,-1.57,0.25)
    elif Gesture == 4.0 :
        position_control(-1.46,1.57,0.04,0.0,-0.42, 1.55,0.0,-1.57,0.0,0.0,)
    elif Gesture == 5.0 :
        position_control(0,0.1, 0.2,0.3,0.4, -0,-0.1, -0.2,-0.3,-0.4,)
    else:
        print('Exited')
    pass
    #rate.sleep()

def subscriber():
    
    print('I am in')
    rospy.init_node("control_hands", anonymous=True)
    global rate
    rate = rospy.Rate(10)
    rospy.Subscriber("/both_hands",Float64,callback)
    rospy.Subscriber("/single_hand",Float64, which_hand)
    print('After subscribe')
    rospy.spin()


if __name__ == '__main__':
    try:
        print('before subscribe')
        subscriber()
    except rospy.ROSInterruptException:
        pass
