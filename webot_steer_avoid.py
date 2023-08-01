#!/usr/bin/env python3 

import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan
from math import pi
import os

class Webot_control:
    def __init__(self):
        rospy.init_node("webot_node") #node 이름 정하기
        self.webot_ctrl_pub = rospy.Publisher("/commands/servo/position", Float64, queue_size=1) # node 역할 정하기
        #queue size는 rostopic bw "토픽이름"으로 확인
        rospy.Subscriber("/scan", LaserScan, self.laser_CB)
        self.laser_msg = LaserScan()
        self.rate = rospy.Rate(10) # 주기 설정
        self.safe_range = 0.30
        self.detect_degree = 90 # -90과 90 사이 -> 963
        self.detect_range = 0.60
        self.sensitivity = 10
    
    def laser_CB(self, msg):
        # print(f"---------------------")
        degrees = [(msg.angle_min + msg.angle_increment * index)*180/pi for index, value in enumerate(msg.ranges)]
        num = 0
        index_list = []
        degree_list = []
        left_degree = []
        right_degree = []
        for index, value in enumerate(msg.ranges):
            if self.detect_degree < abs(degrees[index]) and 0 < value < self.safe_range:
                # print(index)
                index_list.append(index)
                degree_list.append(degrees[index])
        # print(index_list) #각도 내에 있는 인덱스 리스트
        # print(degree_list)

        for degree in degree_list:
            if degree > 0:
                right_degree.append(degree)
            else:
                left_degree.append(degree)
        num_right_degree = len(right_degree)
        num_left_degree = len(left_degree)
        os.system("clear")
        print(f"num left  degree: {num_right_degree}")
        print(f"num right degree: {num_left_degree}")

        num_left_degree = 0 if num_left_degree < self.sensitivity else num_left_degree
        num_right_degree = 0 if num_right_degree < self.sensitivity else num_right_degree

        if num_right_degree == 0 and num_left_degree == 0:
            steer = 0.5
        elif num_right_degree > num_left_degree:
            steer = 0
        else:
            steer = 1
        self.webot_ctrl_pub.publish(steer)


        # if index_list != -1:
        if -1 == 1:
            for index in index_list:
                if index > 963:
                    right_degree.append(index)
                elif index < 321:
                    left_degree.append(index)

            os.system("clear")
            if left_degree != []:
                print(f"left  obj: {max(left_degree)}")
                print(f"left  obj: {321 - min(left_degree)}")
            if right_degree != []:
                print(f"right obj: {min(right_degree)}")
                print(f"right obj: {max(right_degree) - 963}")

def main():
    webot_control = Webot_control()
    rospy.spin()

if __name__ == "__main__":
    main()