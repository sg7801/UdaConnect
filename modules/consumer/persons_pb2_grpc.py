import grpc
import persons_pb2 as persons__pb2
class PersonServiceStub(object):
    def __init__(self, channel):
        self.Create = channel.unary_unary(
                '/CallService/Create',
                request_serializer=persons__pb2.PersonsMessage.SerializeToString,
                response_deserializer=persons__pb2.PersonsMessage.FromString,
                )
class PersonServiceServicer(object):
    def Create(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
def add_PersonServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=persons__pb2.PersonsMessage.FromString,
                    response_serializer=persons__pb2.PersonsMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'CallService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
class PersonService(object):
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
        return grpc.experimental.unary_unary(request, target, '/CallService/Create',
            persons__pb2.PersonsMessage.SerializeToString,
            persons__pb2.PersonsMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)