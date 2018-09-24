def get_tracking_features(old_gray, bb_list, index=0):  
    # params for ShiTomasi corner detection
    feature_params = dict( maxCorners = 100,
                           qualityLevel = 0.3,
                           minDistance = 7,
                           blockSize = 15 )

    # Parameters for lucas kanade optical flow
    lk_params = dict( winSize  = (15,15),
                      maxLevel = 4,
                      criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    # Create some random colors
    color = np.random.randint(0,255,(100,3))

    # Take first frame and find corners in it

    tracking_feature_x, tracking_feature_y, tracking_feature_w, tracking_feature_h = bb_list[index]
    tracking_feature_roi = old_gray[tracking_feature_y:tracking_feature_y + tracking_feature_h,  
                                  tracking_feature_x:tracking_feature_x + tracking_feature_w]

    plt.imshow(tracking_feature_roi, 'gray')
    plt.show()
    p0 = cv2.goodFeaturesToTrack(tracking_feature_roi, mask = None, **feature_params)
    p0[:,:,0] += tracking_feature_x
    p0[:,:,1] += tracking_feature_y

    return p0, lk_params, color

def tracking(p0, old_gray, frame_gray, lk_params, color, cimg, cv_image):
    # calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    if p1 is not None:
        # Select good points
        good_new = p1[st==1]
        good_old = p0[st==1]

        # Create a mask image for drawing purposes
        mask = np.zeros_like(cimg)

        # draw the tracks
        for i,(new,old) in enumerate(zip(good_new,good_old)):
            a,b = new.ravel()
            c,d = old.ravel()
            mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
            cimg = cv2.circle(cimg,(a,b),5,color[i].tolist(),-1)
        features_mean = np.mean(good_new, axis=0)

        if not math.isnan(features_mean[0]):
            cv2.rectangle(cimg,(int(features_mean[0]-100),int(features_mean[1]-100)), \
                               (int(features_mean[0]+100),int(features_mean[1]+100)),(64,117,0),5)

        # get the head position 
        head_img = cv_image.copy()
        if len(head_img.shape)==3:
            head_img = cv2.cvtColor(head_img,cv2.COLOR_BGR2GRAY)
        head_list = find_head_v1(head_img, cimg, bb_list, 50, 5, remove_body_thresh)

        cimg = cv2.add(cimg,mask)
        cv2.imshow('frame',cimg)

        # Now update the previous frame and previous points
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1,1,2)
    else:
        p0 = None
    
    return p0, old_gray, cimg
