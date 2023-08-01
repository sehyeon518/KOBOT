#!/usr/bin/env python3 

import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import Image, CompressedImage
from math import *
import os
import cv2
from cv_bridge import CvBridge
import numpy as np

class Webot_control:
    def __init__(self):
        rospy.init_node("webot_node") #node 이름 정하기
        #rospy.Subscriber("/usb_cam/image_rect_color", Image, self.img_CB)
        rospy.Subscriber("usb_cam/image_rect_color/compressed", CompressedImage, self.comp_img_CB)
        self.webot_speed_pub = rospy.Publisher("/commands/motor/speed", Float64, queue_size=1) # node 역할 정하기
        self.cvbridge = CvBridge()
        self.comp_img = []

    def comp_img_CB(self,msg):
        self.comp_img = self.cvbridge.compressed_imgmsg_to_cv2(msg)
        hsv_img = cv2.cvtColor(self.comp_img,cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(hsv_img)
        os.system("clear")
        #print(np.average(self.comp_img)) # 손으로 다 가리면 값 낮아짐, 후레쉬 비추면 값 높아짐
        print(f"H_average : {np.average(h)}")
        print(f"S_average : {np.average(s)}")
        print(f"V_average : {np.average(v)}")

        cv2.imshow("comp_img",self.comp_img)
        cv2.waitKey(1)

        if np.average(v) < 0:
            speed = 10
        else : 
            speed = 1000
        self.webot_speed_pub.publish(speed)

def main():
    webot_control = Webot_control()
    rospy.spin()

if __name__ == "__main__":
    main()