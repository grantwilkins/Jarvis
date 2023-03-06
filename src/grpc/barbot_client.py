from __future__ import print_function

import logging

import grpc
import barbot_pb2_grpc
import barbot_pb2

creds_path = '../../certs/server-cert.pem'

def run():
    print("Will try to place order ...")
    with open(creds_path, 'rb') as f:
        creds = grpc.ssl_channel_credentials(f.read())
    with grpc.secure_channel('localhost:50051', creds) as channel:
        stub = barbot_pb2_grpc.BarbotStub(channel)
        response = stub.PlaceOrder(barbot_pb2.OrderRequest(user_id='gfwilki@clemson.edu', drink_num=3))
    print("Client ack received: " + response.ack)


if __name__ == '__main__':
    logging.basicConfig()
    run()
