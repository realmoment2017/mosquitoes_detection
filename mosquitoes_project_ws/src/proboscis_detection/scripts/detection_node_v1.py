#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from rospy.numpy_msg import numpy_msg
#from proboscis_detection.msgs import proboscis_info

import cv2
import numpy as np
from matplotlib import pyplot as plt
import time as t
from settings import *
from detection_code import *
from proboscis_monitor_once import *
from proboscis_detection.msg import proboscis_info

def detection_node():
    pub = rospy.Publisher('prob_info', numpy_msg(proboscis_info), queue_size=10)
    rospy.init_node('detection_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        while (cap.isOpened()):
	    t_start = t.time()
	    ret, frame = cap.read()
	    if ret==True:
                proboscis_coords_trans = list()
	        proboscis_coords, proboscis_orients, cimg = proboscis_monitor_once(frame)
                if proboscis_coords is not None:
                    for index in range(len(proboscis_coords)):
                        proboscis_coords_trans.append( proboscis_coords[index][0])
                        proboscis_coords_trans.append( proboscis_coords[index][1]) 
                        if proboscis_orients[index]<-np.pi:
                            proboscis_orients[index] += 2*np.pi
                    proboscis_coords_trans = np.array(proboscis_coords_trans, dtype=np.int32)
                    proboscis_orients_trans = np.array(proboscis_orients, dtype=np.float32)
                    info = proboscis_info()
                    info.positions = proboscis_coords_trans
                    info.orientations = proboscis_orients_trans
                    rospy.loginfo(info.positions)
                    rospy.loginfo(info.orientations)
                    pub.publish(info)

	        if cv2.waitKey(1) & 0xFF == 27:
		    break
	    else:
	        break
            rate.sleep()
        # Release everything if job is finished
        cap.release()
        #out.release()
        cv2.destroyAllWindows()



if __name__ == '__main__':
    try:
        detection_node()
    except rospy.ROSInterruptException:
        pass
