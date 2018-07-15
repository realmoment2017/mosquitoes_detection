// Auto-generated. Do not edit!

// (in-package proboscis_detection.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class robot_state_info {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.tracking = null;
      this.mosquito = null;
    }
    else {
      if (initObj.hasOwnProperty('tracking')) {
        this.tracking = initObj.tracking
      }
      else {
        this.tracking = 0;
      }
      if (initObj.hasOwnProperty('mosquito')) {
        this.mosquito = initObj.mosquito
      }
      else {
        this.mosquito = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type robot_state_info
    // Serialize message field [tracking]
    bufferOffset = _serializer.int32(obj.tracking, buffer, bufferOffset);
    // Serialize message field [mosquito]
    bufferOffset = _serializer.int32(obj.mosquito, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type robot_state_info
    let len;
    let data = new robot_state_info(null);
    // Deserialize message field [tracking]
    data.tracking = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [mosquito]
    data.mosquito = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'proboscis_detection/robot_state_info';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3462d490b19f22662965869fa73aeb01';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 tracking
    int32 mosquito
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new robot_state_info(null);
    if (msg.tracking !== undefined) {
      resolved.tracking = msg.tracking;
    }
    else {
      resolved.tracking = 0
    }

    if (msg.mosquito !== undefined) {
      resolved.mosquito = msg.mosquito;
    }
    else {
      resolved.mosquito = 0
    }

    return resolved;
    }
};

module.exports = robot_state_info;
