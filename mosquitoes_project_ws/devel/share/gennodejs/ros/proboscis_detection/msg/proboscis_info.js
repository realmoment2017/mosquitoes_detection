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

class proboscis_info {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.positions = null;
      this.orientations = null;
      this.bounding_boxes = null;
    }
    else {
      if (initObj.hasOwnProperty('positions')) {
        this.positions = initObj.positions
      }
      else {
        this.positions = [];
      }
      if (initObj.hasOwnProperty('orientations')) {
        this.orientations = initObj.orientations
      }
      else {
        this.orientations = [];
      }
      if (initObj.hasOwnProperty('bounding_boxes')) {
        this.bounding_boxes = initObj.bounding_boxes
      }
      else {
        this.bounding_boxes = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type proboscis_info
    // Serialize message field [positions]
    bufferOffset = _arraySerializer.int32(obj.positions, buffer, bufferOffset, null);
    // Serialize message field [orientations]
    bufferOffset = _arraySerializer.float32(obj.orientations, buffer, bufferOffset, null);
    // Serialize message field [bounding_boxes]
    bufferOffset = _arraySerializer.int32(obj.bounding_boxes, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type proboscis_info
    let len;
    let data = new proboscis_info(null);
    // Deserialize message field [positions]
    data.positions = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [orientations]
    data.orientations = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [bounding_boxes]
    data.bounding_boxes = _arrayDeserializer.int32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.positions.length;
    length += 4 * object.orientations.length;
    length += 4 * object.bounding_boxes.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'proboscis_detection/proboscis_info';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4eceeeb62787b55dec9faa253821d942';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32[] positions
    float32[] orientations
    int32[] bounding_boxes
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new proboscis_info(null);
    if (msg.positions !== undefined) {
      resolved.positions = msg.positions;
    }
    else {
      resolved.positions = []
    }

    if (msg.orientations !== undefined) {
      resolved.orientations = msg.orientations;
    }
    else {
      resolved.orientations = []
    }

    if (msg.bounding_boxes !== undefined) {
      resolved.bounding_boxes = msg.bounding_boxes;
    }
    else {
      resolved.bounding_boxes = []
    }

    return resolved;
    }
};

module.exports = proboscis_info;
