# State-of-the-art one_image and reture proboscis coordinates
# Watershed test
import cv2
import numpy as np
from matplotlib import pyplot as plt
import time as t
from settings import *
from detection_code import *

# def sys_init():
#     IMG_upper_left_x = 0 
#     IMG_upper_left_y = 0
#     WIDTH = 1600
#     HEIGHT = 1200

#     tune_mode = False

#     cap = cv2.VideoCapture(0)
#     cap.set(3,1600)
#     cap.set(4,1200)
#     cap.set(cv2.CAP_PROP_BRIGHTNESS, 40)
#     cap.set(cv2.CAP_PROP_CONTRAST, 100)
    
#     return IMG_upper_left_x, IMG_upper_left_y, WIDTH, HEIGHT, tune_mode, cap


def proboscis_monitor_once(frame):
    
    create_track_bars()

    if tune_mode == True:
        remove_body_thresh = cv2.getTrackbarPos('remove_body_thresh', 'cimg')

    else:
        remove_body_thresh = 120

    img = frame[IMG_upper_left_x:IMG_upper_left_x + HEIGHT,IMG_upper_left_y:IMG_upper_left_y + WIDTH,:]

    cimg = img.copy()  
    src_img_copy = img.copy()
#         cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)


    gray = cv2.cvtColor(src_img_copy,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,120,255,cv2.THRESH_BINARY_INV)

#     # noise removal
#     kernel = np.ones((3,3),np.uint8)
#     opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)


#     # sure background area
#     sure_bg = cv2.dilate(opening,kernel,iterations=5)


#     # Finding sure foreground area
#     dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
#     ret, sure_fg = cv2.threshold(dist_transform,0.01*dist_transform.max(),255,0)


#     # Finding unknown region
#     sure_fg = np.uint8(sure_fg)
#     unknown = cv2.subtract(sure_bg,sure_fg)


#     # Marker labelling
#     ret, markers = cv2.connectedComponents(sure_fg)

#     # Add one to all labels so that sure background is not 0, but 1
#     # Markers: unknown--0, background--1, others--start from 2
#     markers = markers+1

#     # Now, mark the region of unknown with zero
#     markers[unknown==255] = 0

#     # Markers: Boundaries are marked as -1, background -- 1, others--start from 2
#     markers = cv2.watershed(src_img_copy,markers)

#     # Bounding box test
#     markers_copy = markers.copy()
#     markers_copy[markers_copy==-1] = 1
#     markers_copy = np.array(markers_copy, dtype = np.uint8)

#     num_iters = markers_copy.max() + 1

#     bb_list = []
#     for index in range(2, num_iters):
#         thresh_img = np.zeros((HEIGHT, WIDTH), dtype = np.uint8)
#         thresh_img[markers_copy==index] = 255
#         im2, contours, hierarchy = cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#         # Draw bounding boxes
#         idx =0 
#         for cnt in contours:
#             idx += 1
#             x,y,w,h = cv2.boundingRect(cnt)
#             # Check for qualified region proposals
#             area = cv2.contourArea(cnt)
#             if area > 2000 and area<8000:
#                 bb = cv2.boundingRect(cnt)
#                 bb_list.append(bb)
#                 cv2.rectangle(cimg,(x,y),(x+w,y+h),(255,255,0),2)

    bb_list, cimg = bbox_detection(src_img_copy, thresh, cimg)

    if len(bb_list)==0:
        print('bb_list is None, please check the bounding box detection')
        return None, None, None, None

    # find_head
    head_img = img.copy()
    if len(head_img.shape)==3:
        head_img = cv2.cvtColor(head_img,cv2.COLOR_BGR2GRAY)
    head_list = find_head_v1(head_img, cimg, bb_list, 50, 5, remove_body_thresh)
#         if len(head_list)!=len(bb_list):
#             print('bb_list length is {}, while head_list is {}'.format(len(bb_list),len(head_list)))
#             continue

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
    
