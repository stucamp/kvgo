  # kvgo

### Description

Kvgo is an in-memory key-value store over http2 using grpc with protobuf.
This was written mostly for fun and because I enjoy golang and grpc.  


### Usage
##### Build
```shell script
go build .
```
##### Run
```shell script

$ ./kvgo --help
Usage of kvgo.exe:
  -ipv4 string
        IP Address where the server will be hosted (default "localhost")
  -port string
        Port where the server will be hosted (default "50051")

$ ./kvgo
```


### Todo

- Tests
- Client
- Command line options to modify server configuration.
- Expand types supported, right now the key value store only works with strings for both keys and values.
- Expand capabilities with some pubsub options:
    * Subscribe to keys value change.
    * Subscribe to keys deleted.







 