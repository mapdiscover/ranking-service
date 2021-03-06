# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mdrankingservice.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mdrankingservice.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x16mdrankingservice.proto\"D\n\x0bidentifiers\x12\x13\n\x0bidentifiers\x18\x01 \x01(\t\x12\x0f\n\x07\x63urzoom\x18\x02 \x01(\x05\x12\x0f\n\x07minzoom\x18\x03 \x01(\x05\"@\n\x05\x65ntry\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12\x11\n\tlongitude\x18\x02 \x01(\x05\x12\x10\n\x08latitude\x18\x03 \x01(\x05\"*\n\x05\x63lick\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12\r\n\x05\x65vent\x18\x02 \x01(\t\"\x14\n\x04\x64iff\x12\x0c\n\x04\x64iff\x18\x01 \x01(\t\" \n\nidentifier\x12\x12\n\nidentifier\x18\x01 \x01(\t\"(\n\x0eidentifiersOut\x12\x16\n\x0eidentifiersOut\x18\x01 \x01(\t\"\x18\n\x06status\x12\x0e\n\x06status\x18\x01 \x01(\t2\xd9\x01\n\x10MDRankingService\x12*\n\tgetIdents\x12\x0c.identifiers\x1a\x0f.identifiersOut\x12\x1b\n\x08\x61\x64\x64\x45ntry\x12\x06.entry\x1a\x07.status\x12 \n\rincreaseClick\x12\x06.click\x1a\x07.status\x12\x1c\n\x08\x66\x65\x65\x64\x62\x61\x63k\x12\x07.status\x1a\x07.status\x12\x17\n\x05\x62\x61tch\x12\x05.diff\x1a\x07.status\x12#\n\x0b\x64\x65leteEntry\x12\x0b.identifier\x1a\x07.statusb\x06proto3'
)




_IDENTIFIERS = _descriptor.Descriptor(
  name='identifiers',
  full_name='identifiers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifiers', full_name='identifiers.identifiers', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='curzoom', full_name='identifiers.curzoom', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minzoom', full_name='identifiers.minzoom', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=26,
  serialized_end=94,
)


_ENTRY = _descriptor.Descriptor(
  name='entry',
  full_name='entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='entry.identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='entry.longitude', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='entry.latitude', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=96,
  serialized_end=160,
)


_CLICK = _descriptor.Descriptor(
  name='click',
  full_name='click',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='click.identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event', full_name='click.event', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=162,
  serialized_end=204,
)


_DIFF = _descriptor.Descriptor(
  name='diff',
  full_name='diff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='diff', full_name='diff.diff', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=206,
  serialized_end=226,
)


_IDENTIFIER = _descriptor.Descriptor(
  name='identifier',
  full_name='identifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='identifier.identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=228,
  serialized_end=260,
)


_IDENTIFIERSOUT = _descriptor.Descriptor(
  name='identifiersOut',
  full_name='identifiersOut',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifiersOut', full_name='identifiersOut.identifiersOut', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=262,
  serialized_end=302,
)


_STATUS = _descriptor.Descriptor(
  name='status',
  full_name='status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='status.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=304,
  serialized_end=328,
)

DESCRIPTOR.message_types_by_name['identifiers'] = _IDENTIFIERS
DESCRIPTOR.message_types_by_name['entry'] = _ENTRY
DESCRIPTOR.message_types_by_name['click'] = _CLICK
DESCRIPTOR.message_types_by_name['diff'] = _DIFF
DESCRIPTOR.message_types_by_name['identifier'] = _IDENTIFIER
DESCRIPTOR.message_types_by_name['identifiersOut'] = _IDENTIFIERSOUT
DESCRIPTOR.message_types_by_name['status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

identifiers = _reflection.GeneratedProtocolMessageType('identifiers', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFIERS,
  '__module__' : 'mdrankingservice_pb2'
  # @@protoc_insertion_point(class_scope:identifiers)
  })
_sym_db.RegisterMessage(identifiers)

entry = _reflection.GeneratedProtocolMessageType('entry', (_message.Message,), {
  'DESCRIPTOR' : _ENTRY,
  '__module__' : 'mdrankingservice_pb2'
  # @@protoc_insertion_point(class_scope:entry)
  })
_sym_db.RegisterMessage(entry)

click = _reflection.GeneratedProtocolMessageType('click', (_message.Message,), {
  'DESCRIPTOR' : _CLICK,
  '__module__' : 'mdrankingservice_pb2'
  # @@protoc_insertion_point(class_scope:click)
  })
_sym_db.RegisterMessage(click)

diff = _reflection.GeneratedProtocolMessageType('diff', (_message.Message,), {
  'DESCRIPTOR' : _DIFF,
  '__module__' : 'mdrankingservice_pb2'
  # @@protoc_insertion_point(class_scope:diff)
  })
_sym_db.RegisterMessage(diff)

identifier = _reflection.GeneratedProtocolMessageType('identifier', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFIER,
  '__module__' : 'mdrankingservice_pb2'
  # @@protoc_insertion_point(class_scope:identifier)
  })
_sym_db.RegisterMessage(identifier)

identifiersOut = _reflection.GeneratedProtocolMessageType('identifiersOut', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFIERSOUT,
  '__module__' : 'mdrankingservice_pb2'
  # @@protoc_insertion_point(class_scope:identifiersOut)
  })
_sym_db.RegisterMessage(identifiersOut)

status = _reflection.GeneratedProtocolMessageType('status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'mdrankingservice_pb2'
  # @@protoc_insertion_point(class_scope:status)
  })
_sym_db.RegisterMessage(status)



_MDRANKINGSERVICE = _descriptor.ServiceDescriptor(
  name='MDRankingService',
  full_name='MDRankingService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=331,
  serialized_end=548,
  methods=[
  _descriptor.MethodDescriptor(
    name='getIdents',
    full_name='MDRankingService.getIdents',
    index=0,
    containing_service=None,
    input_type=_IDENTIFIERS,
    output_type=_IDENTIFIERSOUT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='addEntry',
    full_name='MDRankingService.addEntry',
    index=1,
    containing_service=None,
    input_type=_ENTRY,
    output_type=_STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='increaseClick',
    full_name='MDRankingService.increaseClick',
    index=2,
    containing_service=None,
    input_type=_CLICK,
    output_type=_STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='feedback',
    full_name='MDRankingService.feedback',
    index=3,
    containing_service=None,
    input_type=_STATUS,
    output_type=_STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='batch',
    full_name='MDRankingService.batch',
    index=4,
    containing_service=None,
    input_type=_DIFF,
    output_type=_STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='deleteEntry',
    full_name='MDRankingService.deleteEntry',
    index=5,
    containing_service=None,
    input_type=_IDENTIFIER,
    output_type=_STATUS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MDRANKINGSERVICE)

DESCRIPTOR.services_by_name['MDRankingService'] = _MDRANKINGSERVICE

# @@protoc_insertion_point(module_scope)
