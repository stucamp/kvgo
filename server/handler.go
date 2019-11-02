package server

import (
	"context"
	"fmt"
	pb "github.com/somerska/kvgo/api"
	"sync"
)

type KvServer struct {
	pb.UnimplementedKeyValueStoreServer
	mut   sync.RWMutex
	store map[string]string
}

func (s *KvServer) Create(ctx context.Context, in *pb.CreateRequest) (*pb.CreateResponse, error) {
	keyValue := in.GetKeyValue()
	s.mut.Lock()
	defer s.mut.Unlock()

	if _, alreadyExists := s.store[keyValue.Key.Key]; alreadyExists {
		return &pb.CreateResponse{
			Success: &pb.Success{
								WasSuccessful:        false,
								Description:          fmt.Sprintf("Key {%v} already exists", keyValue.Key.Key),
			}}, nil
	}
	s.store[keyValue.Key.Key] = keyValue.Value.Value
	return &pb.CreateResponse{
		Success: &pb.Success {
							WasSuccessful: true,
							Description:fmt.Sprintf("Key {%v} created", keyValue.Key.Key),
		}}, nil
}

func (s *KvServer) Retrieve(ctx context.Context, in *pb.RetrieveRequest) (*pb.RetrieveResponse, error){
	key := in.GetKey()
	s.mut.RLock()
	defer s.mut.RUnlock()

	if value, keyExists := s.store[key.Key]; keyExists {
		return &pb.RetrieveResponse{
						Success: &pb.Success{WasSuccessful: true, Description: ""},
						Value: &pb.Value{Value: value,},
		}, nil
	} else {
		return &pb.RetrieveResponse{
			Success: &pb.Success{
								WasSuccessful: false,
								Description: fmt.Sprintf("Key {%v} does not exist", key.Key)},
			Value: &pb.Value{Value: "",},
		}, nil
	}
}

func (s *KvServer) Update(ctx context.Context, in *pb.UpdateRequest) (*pb.UpdateResponse, error) {
	keyValue := in.GetKeyValue()
	s.mut.Lock()
	defer s.mut.Unlock()

	if _, keyExists := s.store[keyValue.Key.Key]; keyExists {
		s.store[keyValue.Key.Key] = keyValue.Value.Value
		return &pb.UpdateResponse{
			Success:&pb.Success{
				WasSuccessful: true,
				Description:fmt.Sprintf("Key {%v} updated", keyValue.Key.Key)}}, nil
	}  else {
		return &pb.UpdateResponse{Success: &pb.Success{
			WasSuccessful: false,
			Description:fmt.Sprintf("Key {%v} does not exist", keyValue.Key.Key)}}, nil
	}
}

func (s *KvServer) Delete(ctx context.Context, in *pb.DeleteRequest) (*pb.DeleteResponse, error) {
	key := in.GetKey()
	s.mut.Lock()
	defer s.mut.Unlock()

	if _, keyExists := s.store[key.Key]; keyExists {
		delete(s.store, key.Key)
		return &pb.DeleteResponse{
			Success:&pb.Success{
				WasSuccessful: true,
				Description:fmt.Sprintf("Key {%v} deleted", key.Key)}}, nil
	}  else {
		return &pb.DeleteResponse{
			Success: &pb.Success{
				WasSuccessful: false,
				Description:fmt.Sprintf("Key {%v} does not exist", key.Key)}}, nil
	}
}



