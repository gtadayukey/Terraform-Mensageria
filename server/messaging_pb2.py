# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: messaging.proto
# Protobuf Python Version: 6.31.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    0,
    '',
    'messaging.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fmessaging.proto\x12\tmessaging\",\n\x0eMessageRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"1\n\x0fMessageResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t2V\n\x0eMessageService\x12\x44\n\x0bSendMessage\x12\x19.messaging.MessageRequest\x1a\x1a.messaging.MessageResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messaging_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MESSAGEREQUEST']._serialized_start=30
  _globals['_MESSAGEREQUEST']._serialized_end=74
  _globals['_MESSAGERESPONSE']._serialized_start=76
  _globals['_MESSAGERESPONSE']._serialized_end=125
  _globals['_MESSAGESERVICE']._serialized_start=127
  _globals['_MESSAGESERVICE']._serialized_end=213
# @@protoc_insertion_point(module_scope)
