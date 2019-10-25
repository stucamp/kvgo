  # kvgo

### Description

Kvgo is an in-memory key-value store over http2 using grpc.  Read operations can benefit from the read-write lock used around the backing data structure.   
This was written mostly for fun and because I enjoy golang and grpc.  

### Todo

- Command line options to modify server configuration (host, port, etc.)
- Expand types supported, right now the backing structure is ```map[string]string```
- Expand capabilities with some pubsub options
    * Subscribe to keys value change
    * Subscribe to keys deleted







 