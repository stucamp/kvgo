  # kvgo

### Description

Kvgo is an in-memory key-value store over http2 using grpc.  Read operations can benefit from the read-write lock used around the backing data structure.   
This was written mostly for fun and because I enjoy golang and grpc.  

### Todo

- Command line options to modify server configuration.
- Expand types supported, right now the key value store only works with strings for both keys and values.
- Expand capabilities with some pubsub options:
    * Subscribe to keys value change.
    * Subscribe to keys deleted.







 