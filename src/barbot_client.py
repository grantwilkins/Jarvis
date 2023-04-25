from __future__ import print_function

import logging

import grpc
import barbot_pb2_grpc
import barbot_pb2

IP_ADDR = 'localhost'
#IP_ADDR = '172.20.10.6'
PORT = '5005'

def place_order(user_id, drink_name, order_tuple, flavor_name, flavor_id):
    print("Will try to place order ...")
    with grpc.insecure_channel(IP_ADDR + ':' + PORT) as channel:
        stub = barbot_pb2_grpc.BarbotStub(channel)
        response = stub.PlaceOrder(barbot_pb2.OrderRequest(
            user_id=user_id, 
            drink_name=drink_name,
            container_amounts=order_tuple,
            flavor_name=flavor_name,
            flavor_id=flavor_id))
    print("Client ack received: " + response.user_id + " ordered " + response.drink_name + " with " + response.flavor_name + " flavor")

def clean_system(user_id):
    print("Will try to clean system ...")
    with grpc.insecure_channel(IP_ADDR + ':' + PORT) as channel:
        stub = barbot_pb2_grpc.BarbotStub(channel)
        response = stub.CleanSystem(barbot_pb2.CleanRequest(user_id=user_id))
    print("Client ack received: " + response.user_id + " ordered system clean")

def system_check(user_id):
    print("Will try to check system ...")
    with grpc.insecure_channel(IP_ADDR + ':' + PORT) as channel:
        stub = barbot_pb2_grpc.BarbotStub(channel)
        response = stub.SystemCheck(barbot_pb2.SystemCheckRequest(user_id=user_id))
    print("Client ack received: " + response.user_id + " ordered system check")

if __name__ == '__main__':
    logging.basicConfig()