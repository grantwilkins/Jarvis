from __future__ import print_function

import logging

import grpc
import barbot_pb2_grpc
import barbot_pb2

#IP_ADDR = 'localhost'
IP_ADDR = '172.20.10.5'
PORT = '5005'

def place_order(user_id, drink_name, container_num, amount_oz, stirring):
    print("Will try to place order ...")
    with grpc.insecure_channel(IP_ADDR + ':' + PORT) as channel:
        stub = barbot_pb2_grpc.BarbotStub(channel)
        response = stub.PlaceOrder(barbot_pb2.OrderRequest(
            user_id    = user_id, 
            drink_name = drink_name,
            container_num = container_num,
            amount_oz = amount_oz,
            stirring   = stirring))
    print("Client ack received: " + response.user_id + " ordered " + str(amount_oz) + "oz of " + response.drink_name)

def inject_flavor(user_id, flavor_name, flavor_id):
    print("Will try to place order ...")
    with grpc.insecure_channel(IP_ADDR + ':' + PORT) as channel:
        stub = barbot_pb2_grpc.BarbotStub(channel)
        response = stub.InjectFlavor(barbot_pb2.FlavorRequest(
            user_id    = user_id, 
            flavor_name = flavor_name,
            flavor_id   = flavor_id))
    print("Client ack received: " + response.user_id + " ordered " + response.flavor_name)

def query_levels():
    print("Will try to query levels ...")
    with grpc.insecure_channel(IP_ADDR + ':' + PORT) as channel:
        stub = barbot_pb2_grpc.BarbotStub(channel)
        response = stub.QueryLevels(barbot_pb2.LevelRequest())
    print("Client ack received: " + response.user_id + " ordered " + response.drink_name)


if __name__ == '__main__': 
    logging.basicConfig()