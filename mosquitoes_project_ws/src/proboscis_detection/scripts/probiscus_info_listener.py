#!/usr/bin/env python



import rospy
import numpy as np
from rospy.numpy_msg import numpy_msg
from proboscis_detection.msg import proboscis_info





class probiscus_info:
    def __init__(self):
        
        self.prob = rospy.Subscriber("prob_info",numpy_msg(proboscis_info),self.callback)
        self.prob_coords = []
	self.prob_orientation = []
	self.mos_box = []

    def callback(self,data):
	self.prob_coords = data.positions
	self.prob_orientation = data.orientations
        #self.mos_box = data.bounding_box
        self.prob.unregister()

    def get_prob_coods(self):
        return self.prob_coords

    def get_prob_orient(self):
        return self.prob_orientation

    def get_bounding_box(self):
        return self.mos_box

def get_prob_info():
    pi = probiscus_info()
    rospy.init_node('listener', anonymous=True)
    rospy.rostime.wallsleep(1)
    prob_ori = pi.get_prob_orient()
    prob_coods = pi.get_prob_coods()
    mos_box = pi.get_bounding_box()
    info = dict({'position':prob_coods, 'orientation':prob_ori, 'boxes':mos_box})
    

    return info

if __name__ == '__main__':
    for i in range(1,6):
       info = get_prob_info()
       print(info['orientation'])

    
