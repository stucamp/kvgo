# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kv.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
    name='kv.proto',
    package='',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b('\n\x08kv.proto\"\x16\n\x05Value\x12\r\n\x05value\x18\x01 \x01(\t\"\x12\n\x03Key\x12\x0b\n\x03key\x18\x01 \x01(\t\"4\n\x08KeyValue\x12\x11\n\x03key\x18\x01 \x01(\x0b\x32\x04.Key\x12\x15\n\x05value\x18\x02 \x01(\x0b\x32\x06.Value\",\n\rCreateRequest\x12\x1b\n\x08keyValue\x18\x01 \x01(\x0b\x32\t.KeyValue\"+\n\x0e\x43reateResponse\x12\x19\n\x07success\x18\x01 \x01(\x0b\x32\x08.Success\"$\n\x0fRetrieveRequest\x12\x11\n\x03key\x18\x01 \x01(\x0b\x32\x04.Key\"D\n\x10RetrieveResponse\x12\x19\n\x07success\x18\x01 \x01(\x0b\x32\x08.Success\x12\x15\n\x05value\x18\x02 \x01(\x0b\x32\x06.Value\",\n\rUpdateRequest\x12\x1b\n\x08keyValue\x18\x01 \x01(\x0b\x32\t.KeyValue\"+\n\x0eUpdateResponse\x12\x19\n\x07success\x18\x01 \x01(\x0b\x32\x08.Success\"\"\n\rDeleteRequest\x12\x11\n\x03key\x18\x01 \x01(\x0b\x32\x04.Key\"+\n\x0e\x44\x65leteResponse\x12\x19\n\x07success\x18\x01 \x01(\x0b\x32\x08.Success\"5\n\x07Success\x12\x15\n\rwasSuccessful\x18\x01 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t2\xc9\x01\n\rKeyValueStore\x12+\n\x06\x43reate\x12\x0e.CreateRequest\x1a\x0f.CreateResponse\"\x00\x12\x31\n\x08Retrieve\x12\x10.RetrieveRequest\x1a\x11.RetrieveResponse\"\x00\x12+\n\x06Update\x12\x0e.UpdateRequest\x1a\x0f.UpdateResponse\"\x00\x12+\n\x06\x44\x65lete\x12\x0e.DeleteRequest\x1a\x0f.DeleteResponse\"\x00\x62\x06proto3')
)




_VALUE = _descriptor.Descriptor(
    name='Value',
    full_name='Value',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='value', full_name='Value.value', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=12,
    serialized_end=34,
)


_KEY = _descriptor.Descriptor(
    name='Key',
    full_name='Key',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key', full_name='Key.key', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=36,
    serialized_end=54,
)


_KEYVALUE = _descriptor.Descriptor(
    name='KeyValue',
    full_name='KeyValue',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key', full_name='KeyValue.key', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='value', full_name='KeyValue.value', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=56,
    serialized_end=108,
)


_CREATEREQUEST = _descriptor.Descriptor(
    name='CreateRequest',
    full_name='CreateRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='keyValue', full_name='CreateRequest.keyValue', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=110,
    serialized_end=154,
)


_CREATERESPONSE = _descriptor.Descriptor(
    name='CreateResponse',
    full_name='CreateResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='success', full_name='CreateResponse.success', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=156,
    serialized_end=199,
)


_RETRIEVEREQUEST = _descriptor.Descriptor(
    name='RetrieveRequest',
    full_name='RetrieveRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key', full_name='RetrieveRequest.key', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=201,
    serialized_end=237,
)


_RETRIEVERESPONSE = _descriptor.Descriptor(
    name='RetrieveResponse',
    full_name='RetrieveResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='success', full_name='RetrieveResponse.success', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='value', full_name='RetrieveResponse.value', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=239,
    serialized_end=307,
)


_UPDATEREQUEST = _descriptor.Descriptor(
    name='UpdateRequest',
    full_name='UpdateRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='keyValue', full_name='UpdateRequest.keyValue', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=309,
    serialized_end=353,
)


_UPDATERESPONSE = _descriptor.Descriptor(
    name='UpdateResponse',
    full_name='UpdateResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='success', full_name='UpdateResponse.success', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=355,
    serialized_end=398,
)


_DELETEREQUEST = _descriptor.Descriptor(
    name='DeleteRequest',
    full_name='DeleteRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key', full_name='DeleteRequest.key', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=400,
    serialized_end=434,
)


_DELETERESPONSE = _descriptor.Descriptor(
    name='DeleteResponse',
    full_name='DeleteResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='success', full_name='DeleteResponse.success', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=436,
    serialized_end=479,
)


_SUCCESS = _descriptor.Descriptor(
    name='Success',
    full_name='Success',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='wasSuccessful', full_name='Success.wasSuccessful', index=0,
            number=1, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='description', full_name='Success.description', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=481,
    serialized_end=534,
)

_KEYVALUE.fields_by_name['key'].message_type = _KEY
_KEYVALUE.fields_by_name['value'].message_type = _VALUE
_CREATEREQUEST.fields_by_name['keyValue'].message_type = _KEYVALUE
_CREATERESPONSE.fields_by_name['success'].message_type = _SUCCESS
_RETRIEVEREQUEST.fields_by_name['key'].message_type = _KEY
_RETRIEVERESPONSE.fields_by_name['success'].message_type = _SUCCESS
_RETRIEVERESPONSE.fields_by_name['value'].message_type = _VALUE
_UPDATEREQUEST.fields_by_name['keyValue'].message_type = _KEYVALUE
_UPDATERESPONSE.fields_by_name['success'].message_type = _SUCCESS
_DELETEREQUEST.fields_by_name['key'].message_type = _KEY
_DELETERESPONSE.fields_by_name['success'].message_type = _SUCCESS
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['Key'] = _KEY
DESCRIPTOR.message_types_by_name['KeyValue'] = _KEYVALUE
DESCRIPTOR.message_types_by_name['CreateRequest'] = _CREATEREQUEST
DESCRIPTOR.message_types_by_name['CreateResponse'] = _CREATERESPONSE
DESCRIPTOR.message_types_by_name['RetrieveRequest'] = _RETRIEVEREQUEST
DESCRIPTOR.message_types_by_name['RetrieveResponse'] = _RETRIEVERESPONSE
DESCRIPTOR.message_types_by_name['UpdateRequest'] = _UPDATEREQUEST
DESCRIPTOR.message_types_by_name['UpdateResponse'] = _UPDATERESPONSE
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['DeleteResponse'] = _DELETERESPONSE
DESCRIPTOR.message_types_by_name['Success'] = _SUCCESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
    'DESCRIPTOR' : _VALUE,
    '__module__' : 'kv_pb2'
    # @@protoc_insertion_point(class_scope:Value)
})
_sym_db.RegisterMessage(Value)

Key = _reflection.GeneratedProtocolMessageType('Key', (_message.Message,), {
    'DESCRIPTOR' : _KEY,
    '__module__' : 'kv_pb2'
    # @@protoc_insertion_point(class_scope:Key)
})
_sym_db.RegisterMessage(Key)

KeyValue = _reflection.GeneratedProtocolMessageType('KeyValue', (_message.Message,), {
    'DESCRIPTOR' : _KEYVALUE,
    '__module__' : 'kv_pb2'
    # @@protoc_insertion_point(class_scope:KeyValue)
})
_sym_db.RegisterMessage(KeyValue)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), {
    'DESCRIPTOR' : _CREATEREQUEST,
    '__module__' : 'kv_pb2'
    # @@protoc_insertion_point(class_scope:CreateRequest)
})
_sym_db.RegisterMessage(CreateRequest)

CreateResponse = _reflection.GeneratedProtocolMessageType('CreateResponse', (_message.Message,), {
    'DESCRIPTOR' : _CREATERESPONSE,
    '__module__' : 'kv_pb2'
    # @@protoc_insertion_point(class_scope:CreateResponse)
})
_sym_db.RegisterMessage(CreateResponse)

RetrieveRequest = _reflection.GeneratedProtocolMessageType('RetrieveRequest', (_message.Message,), {
    'DESCRIPTOR' : _RETRIEVEREQUEST,
    '__module__' : 'kv_pb2'
    # @@protoc_insertion_point(class_scope:RetrieveRequest)
})
_sym_db.RegisterMessage(RetrieveRequest)

RetrieveResponse = _reflection.GeneratedProtocolMessageType('RetrieveResponse', (_message.Message,), {
    'DESCRIPTOR' : _RETRIEVERESPONSE,
    '__module__' : 'kv_pb2'
    # @@protoc_insertion_point(class_scope:RetrieveResponse)
})
_sym_db.RegisterMessage(RetrieveResponse)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEREQUEST,
    '__module__' : 'kv_pb2'
    # @@protoc_insertion_point(class_scope:UpdateRequest)
})
_sym_db.RegisterMessage(UpdateRequest)

UpdateResponse = _reflection.GeneratedProtocolMessageType('UpdateResponse', (_message.Message,), {
    'DESCRIPTOR' : _UPDATERESPONSE,
    '__module__' : 'kv_pb2'
    # @@protoc_insertion_point(class_scope:UpdateResponse)
})
_sym_db.RegisterMessage(UpdateResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
    'DESCRIPTOR' : _DELETEREQUEST,
    '__module__' : 'kv_pb2'
    # @@protoc_insertion_point(class_scope:DeleteRequest)
})
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), {
    'DESCRIPTOR' : _DELETERESPONSE,
    '__module__' : 'kv_pb2'
    # @@protoc_insertion_point(class_scope:DeleteResponse)
})
_sym_db.RegisterMessage(DeleteResponse)

Success = _reflection.GeneratedProtocolMessageType('Success', (_message.Message,), {
    'DESCRIPTOR' : _SUCCESS,
    '__module__' : 'kv_pb2'
    # @@protoc_insertion_point(class_scope:Success)
})
_sym_db.RegisterMessage(Success)



_KEYVALUESTORE = _descriptor.ServiceDescriptor(
    name='KeyValueStore',
    full_name='KeyValueStore',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=537,
    serialized_end=738,
    methods=[
        _descriptor.MethodDescriptor(
            name='Create',
            full_name='KeyValueStore.Create',
            index=0,
            containing_service=None,
            input_type=_CREATEREQUEST,
            output_type=_CREATERESPONSE,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='Retrieve',
            full_name='KeyValueStore.Retrieve',
            index=1,
            containing_service=None,
            input_type=_RETRIEVEREQUEST,
            output_type=_RETRIEVERESPONSE,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='Update',
            full_name='KeyValueStore.Update',
            index=2,
            containing_service=None,
            input_type=_UPDATEREQUEST,
            output_type=_UPDATERESPONSE,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='Delete',
            full_name='KeyValueStore.Delete',
            index=3,
            containing_service=None,
            input_type=_DELETEREQUEST,
            output_type=_DELETERESPONSE,
            serialized_options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_KEYVALUESTORE)

DESCRIPTOR.services_by_name['KeyValueStore'] = _KEYVALUESTORE

# @@protoc_insertion_point(module_scope)