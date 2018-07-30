# State-of-the-art one_image and reture proboscis coordinates
# Watershed test
import cv2
import numpy as np
from matplotlib import pyplot as plt
import time as t
from settings import *
from detection_code import *


def proboscis_monitor_once(frame):
    
    create_track_bars()

    if tune_mode == True:
        remove_body_thresh = cv2.getTrackbarPos('remove_body_thresh', 'cimg')

    else:
        remove_body_thresh = 100

    img = frame[IMG_upper_left_x:IMG_upper_left_x + HEIGHT,IMG_upper_left_y:IMG_upper_left_y + WIDTH,:]

    cimg = img.copy()  


    # detection bounding boxes
    src_img_copy = img.copy()
    bb_list, cimg = bbox_detection(src_img_copy, cimg, remove_body_thresh)

    if len(bb_list)==0:
        print('bb_list is None, please check the bounding box detection')
        return None, None, None, None

    # fit body lines
    line_img = img.copy()
    cimg, body_info = fit_lines(line_img, cimg, bb_list, remove_body_thresh)

    # find_head
    head_img = img.copy()
    if len(head_img.shape)==3:
        head_img = cv2.cvtColor(head_img,cv2.COLOR_BGR2GRAY)
    head_list = find_head_v1(head_img, cimg, bb_list, 50, 5, remove_body_thresh)

    # find proboscis
    proboscis_img = img.copy()
    proboscis_coords_list = list()
    if len(proboscis_img.shape)==3:
        proboscis_img = cv2.cvtColor(proboscis_img,cv2.COLOR_BGR2GRAY)

    cimg, proboscis_coords_list, proboscis_orient_list, bb_list = find_proboscis(proboscis_img, cimg, bb_list, head_list, remove_body_thresh)

#         disp_img = np.concatenate((img, cimg), axis = 1)
    cimg_s = cv2.resize(cimg,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
    cv2.imshow('cimg', cimg_s)

    return proboscis_coords_list, proboscis_orient_list, bb_list, cimg


if __name__ == "__main__":

    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #out = cv2.VideoWriter('output.avi',fourcc, 4.0, (1600,1200))
    
    while(cap.isOpened()):
        t_start = t.time()
        ret, frame = cap.read()
        if ret==True:
            proboscis_coords, proboscis_orients, bb_list, cimg = proboscis_monitor_once(frame)
            print(proboscis_coords, proboscis_orients)
            t_end = t.time()
            print(t_end - t_start)
            #out.write(cimg)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    #out.release()
    cv2.destroyAllWindows()
    
