from __future__ import print_function

import logging

import grpc
import barbot_pb2_grpc
import barbot_pb2


def run():
    print("Will try to place order ...")
    with grpc.insecure_channel('0.0.0.0:50051') as channel:
        stub = barbot_pb2_grpc.BarbotStub(channel)
        response = stub.PlaceOrder(barbot_pb2.OrderRequest(user_id='gfwilki@clemson.edu', drink_num=3))
    print("Client ack received: " + response.ack)


if __name__ == '__main__':
    logging.basicConfig()
    run()
