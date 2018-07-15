; Auto-generated. Do not edit!


(cl:in-package proboscis_detection-msg)


;//! \htmlinclude robot_state_info.msg.html

(cl:defclass <robot_state_info> (roslisp-msg-protocol:ros-message)
  ((tracking
    :reader tracking
    :initarg :tracking
    :type cl:integer
    :initform 0)
   (mosquito
    :reader mosquito
    :initarg :mosquito
    :type cl:integer
    :initform 0))
)

(cl:defclass robot_state_info (<robot_state_info>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <robot_state_info>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'robot_state_info)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name proboscis_detection-msg:<robot_state_info> is deprecated: use proboscis_detection-msg:robot_state_info instead.")))

(cl:ensure-generic-function 'tracking-val :lambda-list '(m))
(cl:defmethod tracking-val ((m <robot_state_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader proboscis_detection-msg:tracking-val is deprecated.  Use proboscis_detection-msg:tracking instead.")
  (tracking m))

(cl:ensure-generic-function 'mosquito-val :lambda-list '(m))
(cl:defmethod mosquito-val ((m <robot_state_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader proboscis_detection-msg:mosquito-val is deprecated.  Use proboscis_detection-msg:mosquito instead.")
  (mosquito m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <robot_state_info>) ostream)
  "Serializes a message object of type '<robot_state_info>"
  (cl:let* ((signed (cl:slot-value msg 'tracking)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'mosquito)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <robot_state_info>) istream)
  "Deserializes a message object of type '<robot_state_info>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'tracking) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'mosquito) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<robot_state_info>)))
  "Returns string type for a message object of type '<robot_state_info>"
  "proboscis_detection/robot_state_info")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'robot_state_info)))
  "Returns string type for a message object of type 'robot_state_info"
  "proboscis_detection/robot_state_info")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<robot_state_info>)))
  "Returns md5sum for a message object of type '<robot_state_info>"
  "3462d490b19f22662965869fa73aeb01")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'robot_state_info)))
  "Returns md5sum for a message object of type 'robot_state_info"
  "3462d490b19f22662965869fa73aeb01")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<robot_state_info>)))
  "Returns full string definition for message of type '<robot_state_info>"
  (cl:format cl:nil "int32 tracking~%int32 mosquito~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'robot_state_info)))
  "Returns full string definition for message of type 'robot_state_info"
  (cl:format cl:nil "int32 tracking~%int32 mosquito~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <robot_state_info>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <robot_state_info>))
  "Converts a ROS message object to a list"
  (cl:list 'robot_state_info
    (cl:cons ':tracking (tracking msg))
    (cl:cons ':mosquito (mosquito msg))
))
