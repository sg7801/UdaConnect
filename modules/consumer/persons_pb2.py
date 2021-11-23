from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
  name='persons.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rpersons.proto\"Y\n\x0ePersonsMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x14\n\x0c\x63ompany_name\x18\x04 \x01(\t29\n\x0b\x43\x61llService\x12*\n\x06\x43reate\x12\x0f.PersonsMessage\x1a\x0f.PersonsMessageb\x06proto3'
)
_PERSONSMESSAGE = _descriptor.Descriptor(
  name='PersonsMessage',
  full_name='PersonsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PersonsMessage.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='PersonsMessage.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='PersonsMessage.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='company_name', full_name='PersonsMessage.company_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=17,
  serialized_end=106,
)
DESCRIPTOR.message_types_by_name['PersonsMessage'] = _PERSONSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
PersonsMessage = _reflection.GeneratedProtocolMessageType('PersonsMessage', (_message.Message,), {
  'DESCRIPTOR' : _PERSONSMESSAGE,
  '__module__' : 'persons_pb2'
  # @@protoc_insertion_point(class_scope:PersonsMessage)
  })
_sym_db.RegisterMessage(PersonsMessage)
_CALLSERVICE = _descriptor.ServiceDescriptor(
  name='CallService',
  full_name='CallService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=108,
  serialized_end=165,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='CallService.Create',
    index=0,
    containing_service=None,
    input_type=_PERSONSMESSAGE,
    output_type=_PERSONSMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALLSERVICE)
DESCRIPTOR.services_by_name['CallService'] = _CALLSERVICE
