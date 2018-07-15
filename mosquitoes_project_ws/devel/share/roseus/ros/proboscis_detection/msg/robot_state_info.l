;; Auto-generated. Do not edit!


(when (boundp 'proboscis_detection::robot_state_info)
  (if (not (find-package "PROBOSCIS_DETECTION"))
    (make-package "PROBOSCIS_DETECTION"))
  (shadow 'robot_state_info (find-package "PROBOSCIS_DETECTION")))
(unless (find-package "PROBOSCIS_DETECTION::ROBOT_STATE_INFO")
  (make-package "PROBOSCIS_DETECTION::ROBOT_STATE_INFO"))

(in-package "ROS")
;;//! \htmlinclude robot_state_info.msg.html


(defclass proboscis_detection::robot_state_info
  :super ros::object
  :slots (_tracking _mosquito ))

(defmethod proboscis_detection::robot_state_info
  (:init
   (&key
    ((:tracking __tracking) 0)
    ((:mosquito __mosquito) 0)
    )
   (send-super :init)
   (setq _tracking (round __tracking))
   (setq _mosquito (round __mosquito))
   self)
  (:tracking
   (&optional __tracking)
   (if __tracking (setq _tracking __tracking)) _tracking)
  (:mosquito
   (&optional __mosquito)
   (if __mosquito (setq _mosquito __mosquito)) _mosquito)
  (:serialization-length
   ()
   (+
    ;; int32 _tracking
    4
    ;; int32 _mosquito
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _tracking
       (write-long _tracking s)
     ;; int32 _mosquito
       (write-long _mosquito s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _tracking
     (setq _tracking (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _mosquito
     (setq _mosquito (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get proboscis_detection::robot_state_info :md5sum-) "3462d490b19f22662965869fa73aeb01")
(setf (get proboscis_detection::robot_state_info :datatype-) "proboscis_detection/robot_state_info")
(setf (get proboscis_detection::robot_state_info :definition-)
      "int32 tracking
int32 mosquito

")



(provide :proboscis_detection/robot_state_info "3462d490b19f22662965869fa73aeb01")


