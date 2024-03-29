import grpc
import location_event_pb2
import location_event_pb2_grpc
print("Sending sample payload...")
channel = grpc.insecure_channel("localhost:5005")
stub = location_event_pb2_grpc.location_eventServiceStub(channel)
location_event = location_event_pb2.location_eventMessage(
    userId=1,
    latitude=-100,
    longitude=30
)
location_event2 = location_event_pb2.location_eventMessage(
    userId=2,
    latitude=-100,
    longitude=30
)
response1 = stub.Create(location_event)
response2 = stub.Create(location_event2)
print("Location sent...")
print(location_event, location_event2)
