import grpc
import locations_pb2
import persons_pb2
import locations_pb2_grpc
import persons_pb2_grpc
channel = grpc.insecure_channel("localhost:5005")
location_stub = locations_pb2_grpc.LocationServiceStub(channel)
person_stub = persons_pb2_grpc.PersonServiceStub(channel)
locations = locations_pb2.LocationsMessage(
    person_id=3,
    creation_time='07:00 hrs GMT+3',
    latitude='-1.1',
    longitude='ABC'
)
persons = persons_pb2.PersonsMessage(
    id = 7,
    first_name = 'Srishti',
    last_name = 'Guleria',
    company_name = 'ABC'
)
response = location_stub.Create(locations)
response = person_stub.Create(persons)
