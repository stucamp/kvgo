package server

import (
	pb "github.com/somerska/kvgo/api"
	"google.golang.org/grpc"
	"log"
	"net"
)

//go:generate protoc -I ../api/ --go_out=plugins=grpc:../api ../api/kv.proto

type Config struct {
	Ipaddr string
	Port string
}


func Run(config Config){
	fqHost := config.Ipaddr + ":" + config.Port
	lis, err := net.Listen("tcp", fqHost)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	grpcServer := grpc.NewServer()
	pb.RegisterKeyValueStoreServer(grpcServer, &KvServer{sm: make(map[string]string)})
	if err := grpcServer.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}



