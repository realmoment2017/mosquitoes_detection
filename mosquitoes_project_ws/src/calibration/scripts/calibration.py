#!/usr/bin/env python

import roslib
import rospy
import sys
import string
import gclib
from time import sleep
from capture_tooltip import *



def strtoform(s):
    prev_i = 0
    l = len(s)
    flag = 0
    for i in range(0,l):
        if s[i] is ",":
            if flag is 0:
                B = s[prev_i:i]
                B = int(B)
            if flag is 1:
                C = s[prev_i:i]
                C = int(C)
            flag = flag+1
            prev_i = i+2
        if flag is 2:
            D = s[prev_i:l]
            D = int(D)
            flag = flag+1
    return(B,C) 
    

            
        
      
            
    

def main():
  g = gclib.py() #make an instance of the gclib python class
  
  try:
    print('gclib version:', g.GVersion())



    ###########################################################################
    #  Connect
    ###########################################################################
    g.GOpen('169.254.3.246 --direct -s ALL')
    #g.GOpen('COM1 --direct')
    print(g.GInfo())

    # set gain values
    g.GCommand('KP ,80,80,80')
    g.GCommand('KD ,10,10,10')
    

    # get intitial position and set it as zero values
    zero_pos = g.GCommand('TP ,B,C,D')
    zero_pos = strtoform(zero_pos)


    # initialize
    robo_pos = [[0]*2]*300
    camera_pos = [[0]*2]*300
    a_count = 0

    #loop though the workspace
    for i in range(1,21):
        for j in range(1,16):
            print(i,j)
            g.GCommand('PR ,0,-2200')
            g.GCommand('BG C')
            sleep(1)
            cam_pos = get_tooltip()
            print(cam_pos)
            #while len(cam_pos)<2:
            #   cam_pos = get_tooltip()    
            #   print(cam_pos)
            robo = g.GCommand('TP ,B,C,D')
            robo = strtoform(robo)
            
            camera_pos[a_count] = cam_pos
            robo_pos[a_count] = robo
            a_count = a_count+1
            
        g.GCommand('PR ,,33000')
        g.GCommand('BG C')
        sleep(2)
        g.GCommand('PR ,2300')
        g.GCommand('BG B')
        sleep(2)
    g.GCommand('PR ,-46000')
    g.GCommand('BG B')
    sleep(3)
    
    


  ###########################################################################
  # except handler
  ###########################################################################  
  except gclib.GclibError as e:
    print('Unexpected GclibError:', e)
  
  finally:
    g.GClose() #don't forget to close connections!
  
 

  return(camera_pos,robo_pos)
    
            
    

    

    
    
   

  

  
 
#runs main() if example.py called from the console
if __name__ == '__main__':
   main()

