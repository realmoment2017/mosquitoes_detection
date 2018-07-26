import numpy as np
import cv2
from settings import *

def nothing(x):
    pass

def create_track_bars():
    cv2.namedWindow('cimg')
    cv2.createTrackbar('remove_body_thresh', 'cimg', 50, 150, nothing)
    cv2.setTrackbarPos('remove_body_thresh', 'cimg', 100)

def remove_body_head(img, remove_body_thresh):
    #remove_body    
    body_img = img.copy()
    ret, body_thresh_img = cv2.threshold(body_img,remove_body_thresh,255,cv2.THRESH_BINARY_INV)
    body_thresh_copy = body_thresh_img.copy()
    kernel = np.ones((7,7),np.uint8)
    body_thresh_img = cv2.erode(body_thresh_img,kernel,iterations=3)
    
    body_thresh_img = cv2.dilate(body_thresh_img,kernel,iterations=3)

    diff = abs(body_thresh_copy - body_thresh_img)

    kernel = np.ones((7,7),np.uint8)
    diff = cv2.erode(diff,kernel,iterations=1)
    diff = cv2.dilate(diff,kernel,iterations=1)
    return img, diff

def remove_body_proboscis(img, remove_body_thresh):
    #remove_body    
    body_img = img.copy()
    ret, body_thresh_img = cv2.threshold(body_img,remove_body_thresh,255,cv2.THRESH_BINARY_INV)
    body_thresh_copy = body_thresh_img.copy()
    kernel = np.ones((7,7),np.uint8)
    body_thresh_img = cv2.erode(body_thresh_img,kernel,iterations=3)
    body_thresh_img = cv2.dilate(body_thresh_img,kernel,iterations=5)
    diff = abs(body_thresh_copy - body_thresh_img)
#     img_s = diff.copy()
#     img_s = cv2.resize(img_s,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
#     cv2.imshow('img_s', img_s)
    kernel = np.ones((3,3),np.uint8)
    diff = cv2.erode(diff,kernel,iterations=1)
#     diff = cv2.dilate(diff,kernel,iterations=2)

    return img, diff

def get_img_value(img, x, y):
    aver = 0
    aver += (img[y,x]*6 + img[y-3,x] + img[y+3,x] + img[y,x-3] + img[y,x+3])/10.0
    aver += (img[y,x]*6 + img[y-4,x+3] + img[y+2,x-3] + img[y-1,x-3] + img[y+4,x+2])/10.0
    return aver
    

def find_head_v1(img, cimg, bb_list, min_dist=35, acc_thresh=8, remove_body_thresh=80):
    #using hough circle detection
    
    #remove_body    
    img, diff = remove_body_head(img, remove_body_thresh)
    diff = 255-diff
    img[diff==255] = 255
    
    #img_s = img.copy()
    #img_s = cv2.resize(img_s,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
    #cv2.imshow('body_thresh_img', img_s)

    ret, thresh = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
    img[thresh>0] = 255
    img = cv2.medianBlur(img,5)
    
    img_s = img.copy()
    img_s = cv2.resize(img_s,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
    cv2.imshow('body_thresh_img', img_s)
    
    head_list = list()
    for (x,y,w,h) in bb_list:
        roi = img[y:y+h, x:x+w]
#         cv2.rectangle(cimg,(x,y),(x+w,y+h),(255,0,255),2)
        circles = cv2.HoughCircles(roi,cv2.HOUGH_GRADIENT,1,minDist = min_dist,
                                    param1=20,param2=acc_thresh,minRadius=5,maxRadius=13)
        
        if circles is not None:
            circles = np.uint16(np.around(circles))
            aver_min = 9999
            for i in circles[0,:]:
                # draw the outer circle
                dist_list = [i[0], abs(w-i[0]), i[1], abs(h-i[1])]
                min_dist = min(dist_list)
#                 if min_dist<20:
                aver = get_img_value(img, x + i[0], y + i[1])
                if aver<aver_min:
                    aver_min = aver
                    c_x = x + i[0]
                    c_y = y + i[1]

            if aver_min<120:
                cv2.circle(cimg,(c_x,c_y),10,(0,255,0),2)
                head_list.append((c_y, c_x))
                    # draw the center of the circle
        #             cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    
    return head_list

def find_head_v2(img, cimg, bb_list, min_dist, acc_thresh, remove_body_thresh=80):
    #remove_body    
    img, diff = remove_body(img, remove_body_thresh)
    diff = 255-diff
    img[diff==255] = 255
    
    head_list = list()
    for (x,y,w,h) in bb_list:
        roi = img[y:y+h, x:x+w]
        ret, thresh = cv2.threshold(roi,20,255,cv2.THRESH_BINARY)
        roi[thresh>0] = 255
        roi = cv2.medianBlur(roi,5)
        roi = 255-roi
        kernel = np.ones((7,7),np.uint8)
        roi = cv2.erode(roi,kernel,iterations=1)
        roi = cv2.dilate(roi,kernel,iterations=1)
        
        cnt_img, contours, hierarchy = cv2.findContours(roi,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        # Draw bounding boxes
        for cnt in contours:
            # Check for qualified region proposals
            area = cv2.contourArea(cnt)
            (circle_x,circle_y),radius = cv2.minEnclosingCircle(cnt)
            center = (int(circle_x),int(circle_y))
            radius = int(radius)
            if area > 200 and area<800:
                cv2.circle(cimg,(int(x + center[0]), int(y + center[1])),10,(0,255,0),2)
                head_list.append((y + center[1], x + center[0]))
    
    return head_list


def find_proboscis(img, cimg, bb_list, head_list, remove_body_thresh=80, bb_size=30):
    
    # remove_body    
    img, diff = remove_body_proboscis(img, remove_body_thresh)
    proboscis_coords_list = []
    proboscis_orient_list = []
    bb_list_refine = []
    for (x,y,w,h), (head_h,head_w) in zip(bb_list, head_list):
        if (head_h - bb_size)>0:
            y = (head_h - bb_size)
        if (head_w - bb_size)>0:
            x = (head_w - bb_size)
        cv2.rectangle(cimg,(x,y),(x+bb_size*2,y+bb_size*2),(255,0,255),2)
        
        roi = diff[y:y+bb_size*2, x:x+bb_size*2]

        
        minLineLength = 17
        maxLineGap = 17
        acc_thresh = 17
        lines = cv2.HoughLinesP(roi,1,np.pi/180,acc_thresh,minLineLength,maxLineGap)
        cv2.circle(cimg,(head_w, head_h),10,(0,255,0),2)
        max_dist = 0
        theta_list = list()
        degree_list = list()

        if lines is not None:
            for line in lines:
                for x1,y1,x2,y2 in line:
                    if np.linalg.norm([abs(x1-x2), abs(y1-y2)],2)>minLineLength:
                        p1 = np.array([x1+x,y1+y], dtype=np.float32)
                        p2 = np.array([x2+x,y2+y], dtype=np.float32)
                        p3 = np.array([head_w,head_h], dtype=np.float32)
#                         cv2.line(cimg,(x1+x,y1+y),(x2+x,y2+y),(0,255,255),2)
                        dist = np.abs(np.cross(p2-p1, p1-p3)) / np.linalg.norm(p2-p1)
                        if dist<15:
#                             cv2.line(cimg,(x1+x,y1+y),(x2+x,y2+y),(0,255,0),2)
                            
                            dist_p1 = np.linalg.norm(p1-p3)
                            dist_p2 = np.linalg.norm(p2-p3)
                            if dist_p1>max_dist:
                                max_dist = dist_p1
                                end_point = p1
                            if dist_p2>max_dist:
                                max_dist = dist_p2
                                end_point = p2
        if max_dist>0:
            #theta = np.arctan2(end_point[0] - head_w, end_point[1] - head_h)
            #cv2.line(cimg,(head_w,head_h),(int(head_w + 40*np.sin(theta)), int(head_h + 40*np.cos(theta))),(0,255,255),3)
            #proboscis_coords = (int(head_w + 20*np.sin(theta)), int(head_h + 20*np.cos(theta)))
            #proboscis_coords_list.append(proboscis_coords)
            #theta = theta-(np.pi/2)

            theta = np.arctan2(-(end_point[1] - head_h), end_point[0] - head_w)

            cv2.line(cimg,(head_w,head_h),(int(head_w + 40*np.cos(theta)), int(head_h - 40*np.sin(theta))),(0,255,255),3)
            proboscis_coords = (int(head_w + 20*np.cos(theta)), int(head_h - 20*np.sin(theta)))
            proboscis_coords_list.append(proboscis_coords)

            proboscis_orient_list.append(theta)
            cv2.circle(cimg,(proboscis_coords[0], proboscis_coords[1]),3,(0,0,255),2)
            bb_list_refine.append([x,y,w,h])
#             cv2.line(cimg,(head_w,head_h),(end_point[0], end_point[1]),(0,150,255),6)
    #print(proboscis_coords_list, proboscis_orient_list)
    return cimg, proboscis_coords_list, proboscis_orient_list, bb_list_refine

def bbox_detection(src_img_copy, thresh, cimg):
    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)


    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=5)


    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform,0.01*dist_transform.max(),255,0)


    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)


    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)

    # Add one to all labels so that sure background is not 0, but 1
    # Markers: unknown--0, background--1, others--start from 2
    markers = markers+1

    # Now, mark the region of unknown with zero
    markers[unknown==255] = 0

    # Markers: Boundaries are marked as -1, background -- 1, others--start from 2
    markers = cv2.watershed(src_img_copy,markers)

    # Bounding box test
    markers_copy = markers.copy()
    markers_copy[markers_copy==-1] = 1
    markers_copy = np.array(markers_copy, dtype = np.uint8)

    num_iters = markers_copy.max() + 1

    bb_list = []
    for index in range(2, num_iters):
        thresh_img = np.zeros((HEIGHT, WIDTH), dtype = np.uint8)
        thresh_img[markers_copy==index] = 255
        im2, contours, hierarchy = cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        # Draw bounding boxes
        idx =0 
        for cnt in contours:
            idx += 1
            x,y,w,h = cv2.boundingRect(cnt)
            # Check for qualified region proposals
            area = cv2.contourArea(cnt)
            aspect_ratio = max(float(w)/h, float(h)/w)
            if area > 2000 and area<8000 and aspect_ratio<3:
                bb = cv2.boundingRect(cnt)
                bb_list.append(bb)
                cv2.rectangle(cimg,(x,y),(x+w,y+h),(255,255,0),2)
    return bb_list, cimg


def fit_lines(src_img_copy, cimg, bb_list, thresh=80):
    gray = cv2.cvtColor(src_img_copy,cv2.COLOR_BGR2GRAY)
    _, line_img = cv2.threshold(gray,thresh,255,cv2.THRESH_BINARY_INV)
    kernel = np.ones((3,3),np.uint8)    
    opening = cv2.morphologyEx(line_img,cv2.MORPH_OPEN,kernel, iterations = 2)
    line_dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    ret, line_sure_fg = cv2.threshold(line_dist_transform,0.2*line_dist_transform.max(),255,0)
    
#     cv2.imshow("line_sure_fg",line_sure_fg)
#     cv2.waitKey(-1)
    
    body_info = []
    for (x,y,w,h) in bb_list:
        roi = line_sure_fg[y:y+h, x:x+w]
        roi = roi.astype(np.uint8)
        rows,cols = roi.shape[:2]
#         roi_draw = roi.copy()
#         roi_draw = cv2.cvtColor(roi_draw,cv2.COLOR_GRAY2BGR)

        im2, contours, hierarchy = cv2.findContours(roi,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        max_area = 0
        index = 0
        max_index = None
        theta = 0
        for index, cnt in enumerate(contours):
            area = cv2.contourArea(cnt)
            if area>max_area:
                max_area = area
                max_index = index
        if max_index is not None:
            cnt = contours[max_index]
    #         roi_draw = cv2.drawContours(roi_draw, [cnt], 0, (0,255,0), 5)
    #         cv2.imshow('line_img_roi', roi_draw)
    #         cv2.waitKey(-1)
    
            [vx,vy,x_l,y_l] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
            theta = -(np.arctan2(vy, vx))[0]
            center_x = x+int(x_l)
            center_y = y+int(y_l)
            cv2.circle(cimg,(center_x,center_y),2,(0,255,255),10)
            center = (center_x, center_y)
            cv2.line(cimg,(int(center_x - 50*np.cos(theta)),int(center_y + 50*np.sin(theta))),
                          (int(center_x + 50*np.cos(theta)),int(center_y - 50*np.sin(theta))),(0,255,0),2)
            body_info.append([center, theta])
        else: 
            body_info.append([(None, None), None])
    return cimg, body_info
