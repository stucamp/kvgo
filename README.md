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
### Performance

For now I've used python for some unary endpoint testing.  This should work fine with newer versions of python but for now I've
tested with python 3.6

####Setup
```shell script
$ sudo apt-get -y update && sudo apt-get -y install python3.6 python3-pip
# activate your virtual environment if using one
$ pip3 install grpcio grpcio-tools
```

####Running
```shell script
# launch kvgo server in one terminal and in another navigate to kvgo/performance
$ python3.6 py_performance.py
Mean time: 0.00021s
Longest 5 times: ['0.04621s', '0.00223s', '0.00126s', '0.00112s', '0.00108s']
Shortest 5 times: ['0.00015s', '0.00015s', '0.00015s', '0.00015s', '0.00015s']
Std dev: 0.00047
Number of requests over 1ms: 2
```




### Todo

- Tests
- Client
- Command line options to modify server configuration.
- Expand types supported, right now the key value store only works with strings for both keys and values.
- Expand capabilities with some pubsub options:
    * Subscribe to keys value change.
    * Subscribe to keys deleted.







 