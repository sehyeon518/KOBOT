#!/usr/bin/env python3 

import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan
from math import pi
import os

class Webot_control:
    def __init__(self):
        rospy.init_node("webot_node") #node 이름 정하기
        self.webot_speed_pub = rospy.Publisher("/commands/motor/speed", Float64, queue_size=1) # node 역할 정하기
        self.webot_steer_pub = rospy.Publisher("/commands/servo/position", Float64, queue_size=1) # node 역할 정하기
        #queue size는 rostopic bw "토픽이름"으로 확인
        rospy.Subscriber("/scan", LaserScan, self.laser_CB)
        self.rate = rospy.Rate(10) # 주기 설정
        self.laser_msg = LaserScan()
        self.safe_range = 0.30
        self.detect_degree = 90
        self.detect_range = 0.60
        self.sensitivity = 10
        self.degree_flag = False
        self.degrees = []
        
    def laser_CB(self, msg):
        os.system("clear")
        e_stop_degree_list = []
        avoid_degree_list = []
        left_degree = []
        right_degree = []
        #print(msg)
        if self.degree_flag == False:
            self.degrees = [(msg.angle_min + msg.angle_increment * index)*180/pi for index, value in enumerate(msg.ranges)]
            self.degree_flag = True
        
        for index, value in enumerate(msg.ranges):
            if 150 < value < abs(self.degrees[index]) and 0 < value < self.safe_range:
                e_stop_degree_list.append(self.degrees[index])
            if self.detect_degree < abs(self.degrees[index]) and 0 < value < self.detect_range:
                avoid_degree_list.append(self.degrees[index])

        if len(e_stop_degree_list) > 10:
            speed = 0
            steer = 0.5
            print("E-STOP")
        else:
            speed = 1000

            for avoid_degree in avoid_degree_list:
                if avoid_degree > 0:
                    right_degree.append(avoid_degree)
                else:
                    left_degree.append(avoid_degree)
            num_right_degree = len(right_degree)
            num_left_degree = len(left_degree)

            print(f"num right  degree: {num_right_degree}")
            print(f"num left degree: {num_left_degree}")

            if num_left_degree < self.sensitivity :
                num_left_degree = 0
            if num_right_degree < self.sensitivity :
                num_right_degree = 0

            if num_right_degree == 0 and num_left_degree == 0:
                steer = 0.5
            elif num_right_degree > num_left_degree:
                steer = 0
                print("go-left")
            else:
                steer = 1
                print("go-right")

        self.webot_steer_pub.publish(steer)
        self.webot_speed_pub.publish(speed)
    
def main():
    webot_control = Webot_control()
    rospy.spin()

if __name__ == "__main__":
    main()