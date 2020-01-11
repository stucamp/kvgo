package server

import (
	"context"
	pb "github.com/somerska/kvgo/api"
	"google.golang.org/grpc"
	"log"
	"testing"
	"time"
)

const (
	address     = "localhost:50051"
	keyName 	= "counter"
	startingVal = "20"
)

func TestCanCreateAKeyAndRetrieveTheValue(t *testing.T) {
	conn, err := grpc.Dial(address, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()

	kvClient := pb.NewKeyValueStoreClient(conn)
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	kvClient.Create(ctx, &pb.CreateRequest{
		KeyValue:             &pb.KeyValue{
			Key:                  &pb.Key{
				Key:                  keyName,
			},
			Value:                &pb.Value{
				Value:                startingVal,
			},
		},

	})

	response, _ := kvClient.Retrieve(ctx, &pb.RetrieveRequest{
		Key:                  &pb.Key{
			Key:                  "counter",
		},
	})

	log.Printf("Got this response %s", response.Value.Value)
}
