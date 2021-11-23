from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
  name='locations.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0flocations.proto\"a\n\x10LocationsMessage\x12\x11\n\tperson_id\x18\x01 \x01(\x05\x12\x15\n\rcreation_time\x18\x02 \x01(\t\x12\x10\n\x08latitude\x18\x03 \x01(\t\x12\x11\n\tlongitude\x18\x04 \x01(\t2A\n\x0fLocationService\x12.\n\x06\x43reate\x12\x11.LocationsMessage\x1a\x11.LocationsMessageb\x06proto3'
)
_LOCATIONSMESSAGE = _descriptor.Descriptor(
  name='LocationsMessage',
  full_name='LocationsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='LocationsMessage.person_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='LocationsMessage.creation_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='LocationsMessage.latitude', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='LocationsMessage.longitude', index=3,
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
  serialized_start=19,
  serialized_end=116,
)
DESCRIPTOR.message_types_by_name['LocationsMessage'] = _LOCATIONSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
LocationsMessage = _reflection.GeneratedProtocolMessageType('LocationsMessage', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONSMESSAGE,
  '__module__' : 'locations_pb2'
  # @@protoc_insertion_point(class_scope:LocationsMessage)
  })
_sym_db.RegisterMessage(LocationsMessage)
_LOCATIONSERVICE = _descriptor.ServiceDescriptor(
  name='LocationService',
  full_name='LocationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=118,
  serialized_end=183,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='LocationService.Create',
    index=0,
    containing_service=None,
    input_type=_LOCATIONSMESSAGE,
    output_type=_LOCATIONSMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOCATIONSERVICE)
DESCRIPTOR.services_by_name['LocationService'] = _LOCATIONSERVICE