;; Auto-generated. Do not edit!


(when (boundp 'proboscis_detection::proboscis_info)
  (if (not (find-package "PROBOSCIS_DETECTION"))
    (make-package "PROBOSCIS_DETECTION"))
  (shadow 'proboscis_info (find-package "PROBOSCIS_DETECTION")))
(unless (find-package "PROBOSCIS_DETECTION::PROBOSCIS_INFO")
  (make-package "PROBOSCIS_DETECTION::PROBOSCIS_INFO"))

(in-package "ROS")
;;//! \htmlinclude proboscis_info.msg.html


(defclass proboscis_detection::proboscis_info
  :super ros::object
  :slots (_positions _orientations _bounding_boxes ))

(defmethod proboscis_detection::proboscis_info
  (:init
   (&key
    ((:positions __positions) (make-array 0 :initial-element 0 :element-type :integer))
    ((:orientations __orientations) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:bounding_boxes __bounding_boxes) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _positions __positions)
   (setq _orientations __orientations)
   (setq _bounding_boxes __bounding_boxes)
   self)
  (:positions
   (&optional __positions)
   (if __positions (setq _positions __positions)) _positions)
  (:orientations
   (&optional __orientations)
   (if __orientations (setq _orientations __orientations)) _orientations)
  (:bounding_boxes
   (&optional __bounding_boxes)
   (if __bounding_boxes (setq _bounding_boxes __bounding_boxes)) _bounding_boxes)
  (:serialization-length
   ()
   (+
    ;; int32[] _positions
    (* 4    (length _positions)) 4
    ;; float32[] _orientations
    (* 4    (length _orientations)) 4
    ;; int32[] _bounding_boxes
    (* 4    (length _bounding_boxes)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[] _positions
     (write-long (length _positions) s)
     (dotimes (i (length _positions))
       (write-long (elt _positions i) s)
       )
     ;; float32[] _orientations
     (write-long (length _orientations) s)
     (dotimes (i (length _orientations))
       (sys::poke (elt _orientations i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; int32[] _bounding_boxes
     (write-long (length _bounding_boxes) s)
     (dotimes (i (length _bounding_boxes))
       (write-long (elt _bounding_boxes i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[] _positions
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _positions (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _positions i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; float32[] _orientations
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _orientations (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _orientations i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; int32[] _bounding_boxes
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _bounding_boxes (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _bounding_boxes i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get proboscis_detection::proboscis_info :md5sum-) "4eceeeb62787b55dec9faa253821d942")
(setf (get proboscis_detection::proboscis_info :datatype-) "proboscis_detection/proboscis_info")
(setf (get proboscis_detection::proboscis_info :definition-)
      "int32[] positions
float32[] orientations
int32[] bounding_boxes

")



(provide :proboscis_detection/proboscis_info "4eceeeb62787b55dec9faa253821d942")


