#!/usr/bin/env python
from __future__ import print_function

import roslib
#roslib.load_manifest('my_package')
import sys
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np
import rospy
from std_msgs.msg import String

class image_converter:
    def __init__(self):
#    self.image_pub = rospy.Publisher("image_topic_2",Image)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/cv_camera/image_raw_latch",Image,self.callback)
        self.tool_tip_coords = []

    def callback(self,data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
#         cv2.imshow('cv_image', cv_image)

        self.tool_tip_coords = capture_tooltip(cv_image)
        #print(self.tool_tip_coords)
        self.image_sub.unregister()

    def get_tool_tip_info(self):
        return self.tool_tip_coords

def get_tooltip():
    ic = image_converter()
    rospy.init_node('calibration_image_converter', anonymous=True)

    rospy.rostime.wallsleep(0.5)
    tool_tip = ic.get_tool_tip_info()
    print(tool_tip)
#     try:
#         rospy.spin()
#     except KeyboardInterrupt:
#         print("Shutting down")
    return tool_tip

def capture_tooltip(img):
        # Convert BGR to HSV
    cimg = img.copy()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([80,40,80])
    upper_blue = np.array([130,80,140])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
#         res = cv2.bitwise_and(frame,frame, mask= mask)
#         cv2.circle(frame, (100,200),5,(130,50,50), 3)
#         print(hsv[200,100])


    kernel = np.ones((25,25),np.uint8)
    blue = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    diff = blue.copy()
    im2, contours, hierarchy = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#         cimg = cv2.drawContours(cimg, contours, -1, (0,255,0), 3)

    tool = None
    max_area = 0
    for index, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        if area>500:
            if area > max_area:
                max_area = area
                tool = index
    if tool is not None:
        epsilon = 0.05*cv2.arcLength(contours[tool],True)
        approx = cv2.approxPolyDP(contours[tool],epsilon,True)
        cimg = cv2.drawContours(cimg, [approx], -1, (255,255,0), 3)

        # Calculate the Gaussian Derivative
        sobel_mask_x = [[1.0,0.0,-1.0],[2.0,0.0,-2.0],[1.0,0.0,-1.0]]
        sobel_mask_y = [[-1.0,-2.0,-1.0],[0.0,0.0,0.0],[1.0,2.0,1.0]]
        kernel_x = np.array(sobel_mask_x)*1.0/8.0 #coefficient 1.0/8.0 is used to be the approximation of the DOG
        kernel_y = np.array(sobel_mask_y)*1.0/8.0 #coefficient 1.0/8.0 is used to be the approximation of the DOG
        diff_corner = diff.copy()
        diff_corner = cv2.GaussianBlur(diff_corner,(15,15),0)
        Ix = cv2.filter2D(diff_corner, -1, kernel_x)  
        Iy = cv2.filter2D(diff_corner, -1, kernel_y) 
        Ixx = Ix*Ix
        Ixy = Ix*Iy
        Iyy = Iy*Iy
        kernel_2d = np.array([[0.1,0.274,0.1],[ 0.274, 0.452, 0.274],[0.1,0.274,0.1]]) # 2d Gaussian Kernel
        Ixx = cv2.filter2D(Ixx,-1,kernel_2d)
        Ixy = cv2.filter2D(Ixy,-1,kernel_2d)
        Iyy = cv2.filter2D(Iyy,-1,kernel_2d)

        k=0.06
        # Compute the corner response function R
        R = Ixx * Iyy - Ixy * Ixy - k * (Ixx + Iyy)**2  

        # Threshold R
        max_res = -1
        tool_tip = None
#             for index, corner in enumerate(approx):
#                 if min(corner[0][1], corner[0][0])>10:
#                     res = R[corner[0][1]][corner[0][0]]
#                     print(abs(res))
#                     if abs(res)>max_res:
#                         max_res = abs(res)
#                         tool_tip = (corner[0][1], corner[0][0])

        index = np.argmax(approx[:,0,1])
#             print(approx.shape, index)
#             print(approx[:,0,0])
        tool_tip = (approx[index,0,0], approx[index,0,1]) # changed here
        if tool_tip is not None:
            print('x:{}    y:{}'.format(tool_tip[0], tool_tip[1]))
            cv2.circle(cimg,(tool_tip[1],tool_tip[0]), 5, (0,0,255), -1) 
            cimg_s = cv2.resize(cimg,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC) 
#             cv2.imshow('cimg_s', cimg_s)
#             k = cv2.waitKey(33) & 0xFF
#             cv2.destroyAllWindows()
#             vidcap.release()
            return tool_tip
        else:
            print('Please run again')
            cimg_s = cv2.resize(cimg,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC) 
            #cv2.imshow('cimg_s', cimg_s)
            #k = cv2.waitKey(-1) & 0xFF
            #cv2.destroyAllWindows()
            #vidcap.release()
            return None


    else:
        print('No tool in the field of view, please check it again.')
        cimg_s = cv2.resize(cimg,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC) 
        #cv2.imshow('cimg_s', cimg_s)
        #k = cv2.waitKey(-1) & 0xFF
#         cv2.destroyAllWindows()
        #vidcap.release()
        return None

if __name__ == '__main__':
    coord = get_tooltip()
    print(coord)
