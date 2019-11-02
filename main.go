package main

import (
	"flag"
	sv "github.com/somerska/kvgo/server"
)

func main(){
	ipaddrPtr := flag.String("ipv4", "localhost", "IP Address where the server will be hosted")
	portPtr := flag.String("port", "50051", "Port where the server will be hosted")
	flag.Parse()
	config := sv.Config{
		Ipaddr: *ipaddrPtr,
		Port:   *portPtr,
	}
	sv.Run(config)
}


