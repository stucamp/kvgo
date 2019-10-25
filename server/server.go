package server

import (
	pb "github.com/somerska/kvgo/api"
	"google.golang.org/grpc"
	"log"
	"net"
	"sync"
)

//go:generate protoc -I ../api/ --go_out=plugins=grpc:../api ../api/kv.proto


func main(){
	kvstore := make(map[string]string)
	mutex := sync.RWMutex{}
	safeKvStore := SafeMap{mutex, kvstore}
	newGrpcServer(&safeKvStore)

}

func newGrpcServer(kvStore *SafeMap) {
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()

	pb.RegisterKeyValueStoreServer(s, &Server{
		UnimplementedKeyValueStoreServer: pb.UnimplementedKeyValueStoreServer{},
		sm:                               SafeMap{},
	})

	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}

