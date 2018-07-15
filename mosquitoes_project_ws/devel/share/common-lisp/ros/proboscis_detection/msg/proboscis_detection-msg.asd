
(cl:in-package :asdf)

(defsystem "proboscis_detection-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "proboscis_info" :depends-on ("_package_proboscis_info"))
    (:file "_package_proboscis_info" :depends-on ("_package"))
    (:file "robot_state_info" :depends-on ("_package_robot_state_info"))
    (:file "_package_robot_state_info" :depends-on ("_package"))
  ))