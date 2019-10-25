package server

import (
	"context"
	pb "github.com/somerska/kvgo/api"
)

type Server struct {
	pb.UnimplementedKeyValueStoreServer
	sm SafeMap
}

func (s *Server) Create(ctx context.Context, in *pb.CreateRequest) (*pb.CreateResponse, error){
	keyValue := in.GetKeyValue()
	err := s.sm.Create(keyValue.Key.Key, keyValue.Value.Value)
	if err != nil {
		return &pb.CreateResponse{Success: &pb.Success{WasSuccessful: false, Description:err.Error()}}, nil
	} else {
		return &pb.CreateResponse{Success:&pb.Success{WasSuccessful: true, Description:""}}, nil
	}
}

func (s *Server) Retrieve(ctx context.Context, in *pb.RetrieveRequest) (*pb.RetrieveResponse, error){
	key := in.GetKey()
	err, value := s.sm.Retrieve(key.Key)
	if err != nil {
		return &pb.RetrieveResponse{
			Success: &pb.Success{WasSuccessful: false, Description: err.Error()},
			Value: &pb.Value{Value: ""},
		}, nil
	} else {
		return &pb.RetrieveResponse{
			Success: &pb.Success{WasSuccessful: true, Description: ""},
			Value: &pb.Value{Value: value},
		}, nil
	}
}

func (s *Server) Update(ctx context.Context, in *pb.UpdateRequest) (*pb.UpdateResponse, error) {
	keyValue := in.GetKeyValue()
	err := s.sm.Update(keyValue.Key.Key, keyValue.Value.Value)
	if err != nil {
		return &pb.UpdateResponse{Success: &pb.Success{WasSuccessful: false, Description:err.Error()}}, nil
	} else {
		return &pb.UpdateResponse{Success:&pb.Success{WasSuccessful: true, Description:""}}, nil
	}
}

func (s *Server) Delete(ctx context.Context, in *pb.DeleteRequest) (*pb.DeleteResponse, error) {
	key := in.GetKey()
	err := s.sm.Delete(key.Key)
	if err != nil {
		return &pb.DeleteResponse{Success: &pb.Success{WasSuccessful: false, Description:err.Error()}}, nil
	} else {
		return &pb.DeleteResponse{Success:&pb.Success{WasSuccessful: true, Description:""}}, nil
	}
}



