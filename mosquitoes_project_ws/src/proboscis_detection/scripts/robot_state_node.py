#!/usr/bin/env python
from __future__ import print_function

import roslib
#roslib.load_manifest('my_package')
import sys
import rospy
from std_msgs.msg import String
from rospy.numpy_msg import numpy_msg
import numpy as np
import time as t
from robot_state_info.msg import robot_state_info

class robot_state:

    def __init__(self,mos_num):
      self.pub = rospy.Publisher('robot_state_info', numpy_msg(robot_state_info), latch = True ,queue_size=10)
      info = robot_state_info()
      info.tracking = 1
      info.mosquito = mos_num
      rospy.loginfo(info.tracking)
      rospy.loginfo(info.mosquito)
      self.pub.publish(info)
      


def robot_state_node(mos_num):
    rs = robot_state(mos_num)
    rospy.init_node('robot_state_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    rate.sleep
   

if __name__ == '__main__':
    robot_state_node(3)
