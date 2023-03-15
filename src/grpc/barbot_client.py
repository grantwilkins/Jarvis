from __future__ import print_function

import logging

import grpc
import barbot_pb2_grpc
import barbot_pb2

IP_ADDR = '0.0.0.0'
PORT = '50051'

def place_order(user_id,drink_name,drink_id, stirring):
    print("Will try to place order ...")
    with grpc.insecure_channel(IP_ADDR + ':' + PORT) as channel:
        stub = barbot_pb2_grpc.BarbotStub(channel)
        response = stub.PlaceOrder(barbot_pb2.OrderRequest(
            user_id    = user_id, 
            drink_name = drink_name,
            drink_id   = drink_id,
            stirring   = stirring))
    print("Client ack received: " + response.user_id + " ordered " + response.drink_name)

if __name__ == '__main__':
    logging.basicConfig()
    place_order()
