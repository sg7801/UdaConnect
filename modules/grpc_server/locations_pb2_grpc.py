import grpc
import locations_pb2 as locations__pb2
class LocationServiceStub(object):
    def __init__(self, channel):
        self.Create = channel.unary_unary(
                '/LocationService/Create',
                request_serializer=locations__pb2.LocationsMessage.SerializeToString,
                response_deserializer=locations__pb2.LocationsMessage.FromString,
                )
class LocationServiceServicer(object):
    def Create(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
def add_LocationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=locations__pb2.LocationsMessage.FromString,
                    response_serializer=locations__pb2.LocationsMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'LocationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
class LocationService(object):
    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LocationService/Create',
            locations__pb2.LocationsMessage.SerializeToString,
            locations__pb2.LocationsMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
