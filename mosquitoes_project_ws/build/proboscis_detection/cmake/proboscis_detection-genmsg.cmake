# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "proboscis_detection: 2 messages, 0 services")

set(MSG_I_FLAGS "-Iproboscis_detection:/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(proboscis_detection_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/proboscis_info.msg" NAME_WE)
add_custom_target(_proboscis_detection_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "proboscis_detection" "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/proboscis_info.msg" ""
)

get_filename_component(_filename "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/robot_state_info.msg" NAME_WE)
add_custom_target(_proboscis_detection_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "proboscis_detection" "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/robot_state_info.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(proboscis_detection
  "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/proboscis_info.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/proboscis_detection
)
_generate_msg_cpp(proboscis_detection
  "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/robot_state_info.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/proboscis_detection
)

### Generating Services

### Generating Module File
_generate_module_cpp(proboscis_detection
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/proboscis_detection
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(proboscis_detection_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(proboscis_detection_generate_messages proboscis_detection_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/proboscis_info.msg" NAME_WE)
add_dependencies(proboscis_detection_generate_messages_cpp _proboscis_detection_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/robot_state_info.msg" NAME_WE)
add_dependencies(proboscis_detection_generate_messages_cpp _proboscis_detection_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(proboscis_detection_gencpp)
add_dependencies(proboscis_detection_gencpp proboscis_detection_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS proboscis_detection_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(proboscis_detection
  "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/proboscis_info.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/proboscis_detection
)
_generate_msg_eus(proboscis_detection
  "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/robot_state_info.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/proboscis_detection
)

### Generating Services

### Generating Module File
_generate_module_eus(proboscis_detection
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/proboscis_detection
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(proboscis_detection_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(proboscis_detection_generate_messages proboscis_detection_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/proboscis_info.msg" NAME_WE)
add_dependencies(proboscis_detection_generate_messages_eus _proboscis_detection_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/robot_state_info.msg" NAME_WE)
add_dependencies(proboscis_detection_generate_messages_eus _proboscis_detection_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(proboscis_detection_geneus)
add_dependencies(proboscis_detection_geneus proboscis_detection_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS proboscis_detection_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(proboscis_detection
  "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/proboscis_info.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/proboscis_detection
)
_generate_msg_lisp(proboscis_detection
  "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/robot_state_info.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/proboscis_detection
)

### Generating Services

### Generating Module File
_generate_module_lisp(proboscis_detection
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/proboscis_detection
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(proboscis_detection_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(proboscis_detection_generate_messages proboscis_detection_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/proboscis_info.msg" NAME_WE)
add_dependencies(proboscis_detection_generate_messages_lisp _proboscis_detection_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/robot_state_info.msg" NAME_WE)
add_dependencies(proboscis_detection_generate_messages_lisp _proboscis_detection_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(proboscis_detection_genlisp)
add_dependencies(proboscis_detection_genlisp proboscis_detection_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS proboscis_detection_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(proboscis_detection
  "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/proboscis_info.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/proboscis_detection
)
_generate_msg_nodejs(proboscis_detection
  "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/robot_state_info.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/proboscis_detection
)

### Generating Services

### Generating Module File
_generate_module_nodejs(proboscis_detection
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/proboscis_detection
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(proboscis_detection_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(proboscis_detection_generate_messages proboscis_detection_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/proboscis_info.msg" NAME_WE)
add_dependencies(proboscis_detection_generate_messages_nodejs _proboscis_detection_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/robot_state_info.msg" NAME_WE)
add_dependencies(proboscis_detection_generate_messages_nodejs _proboscis_detection_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(proboscis_detection_gennodejs)
add_dependencies(proboscis_detection_gennodejs proboscis_detection_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS proboscis_detection_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(proboscis_detection
  "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/proboscis_info.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/proboscis_detection
)
_generate_msg_py(proboscis_detection
  "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/robot_state_info.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/proboscis_detection
)

### Generating Services

### Generating Module File
_generate_module_py(proboscis_detection
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/proboscis_detection
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(proboscis_detection_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(proboscis_detection_generate_messages proboscis_detection_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/proboscis_info.msg" NAME_WE)
add_dependencies(proboscis_detection_generate_messages_py _proboscis_detection_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/administer/mosquitoes_project_ws/src/proboscis_detection/msg/robot_state_info.msg" NAME_WE)
add_dependencies(proboscis_detection_generate_messages_py _proboscis_detection_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(proboscis_detection_genpy)
add_dependencies(proboscis_detection_genpy proboscis_detection_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS proboscis_detection_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/proboscis_detection)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/proboscis_detection
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(proboscis_detection_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/proboscis_detection)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/proboscis_detection
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(proboscis_detection_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/proboscis_detection)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/proboscis_detection
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(proboscis_detection_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/proboscis_detection)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/proboscis_detection
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(proboscis_detection_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/proboscis_detection)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/proboscis_detection\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/proboscis_detection
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(proboscis_detection_generate_messages_py std_msgs_generate_messages_py)
endif()
