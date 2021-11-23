For generating the gPRC files use the below commands:
- **pip install grpcio-tools**
- **python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ location_event.proto**
