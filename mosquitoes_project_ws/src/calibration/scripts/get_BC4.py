#!/usr/bin/env python

import roslib
import rospy
from sanarian_polynomial import *
from calibration import *

def get_Bern_coeff:
    camera , robo = main()
    bern_coeff = get_bern_cof(camera,robo)
    
