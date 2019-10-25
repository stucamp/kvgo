package server

import (
	"context"
	pb "github.com/somerska/kvgo/api"
)

type Server struct {
	pb.UnimplementedKeyValueStoreServer
	sm SafeMap
}

func (s *Server) Create(ctx context.Context, in *pb.CreateRequest) *pb.CreateResponse{
	keyValue := in.GetKeyValue()
	err := s.sm.Create(keyValue.Key.Key, keyValue.Value.Value)
	if err != nil {
		return &pb.CreateResponse{Success: &pb.Success{WasSuccessful: false, Description:err.Error()}}
	} else {
		return &pb.CreateResponse{Success:&pb.Success{WasSuccessful: true, Description:""}}
	}
}

func (s *Server) Retrieve(ctx context.Context, in *pb.RetrieveRequest) *pb.RetrieveResponse{
	key := in.GetKey()
	err, value := s.sm.Retrieve(key.Key)
	if err != nil {
		return &pb.RetrieveResponse{
			Success: &pb.Success{WasSuccessful: false, Description: err.Error()},
			Value: &pb.Value{Value: ""},
		}
	} else {
		return &pb.RetrieveResponse{
			Success: &pb.Success{WasSuccessful: true, Description: ""},
			Value: &pb.Value{Value: value},
		}
	}
}

func (s *Server) Update(ctx context.Context, in *pb.UpdateRequest) *pb.UpdateResponse {
	keyValue := in.GetKeyValue()
	err := s.sm.Update(keyValue.Key.Key, keyValue.Value.Value)
	if err != nil {
		return &pb.UpdateResponse{Success: &pb.Success{WasSuccessful: false, Description:err.Error()}}
	} else {
		return &pb.UpdateResponse{Success:&pb.Success{WasSuccessful: true, Description:""}}
	}
}

func (s *Server) Delete(ctx context.Context, in *pb.DeleteRequest) *pb.DeleteResponse {
	key := in.GetKey()
	err := s.sm.Delete(key.Key)
	if err != nil {
		return &pb.DeleteResponse{Success: &pb.Success{WasSuccessful: false, Description:err.Error()}}
	} else {
		return &pb.DeleteResponse{Success:&pb.Success{WasSuccessful: true, Description:""}}
	}
}



