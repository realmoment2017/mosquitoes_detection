#!/usr/bin/env python
from __future__ import print_function

import roslib
#roslib.load_manifest('my_package')
import sys
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from capture_tooltip import *

class image_converter:

  def __init__(self):
#    self.image_pub = rospy.Publisher("image_topic_2",Image)
    global image_sub
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/cv_camera/image_raw",Image,self.callback)
    self.tool_tip_info = 0

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)
    coord = capture_tooltip(cv_image)
    self.tool_tip_info += 1

  def get_tool_tip_info(self):
    return self.tool_tip_info

def get_tooltip():
  ic = image_converter()
  rospy.init_node('calibration_image_converter', anonymous=True)
  #tool_tip = ic.get_tool_tip_info()
  print("here")
  #rospy.rostime.wallsleep(0.15)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")


if __name__ == '__main__':
    get_tooltip()
