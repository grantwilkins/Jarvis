from concurrent import futures
import logging

import grpc
import barbot_pb2_grpc
import barbot_pb2
import hello

private_key_path = "../../certs/server-key.pem"
certificate_path = "../../certs/server-cert.pem"

class Barbot(barbot_pb2_grpc.BarbotServicer):

    def PlaceOrder(self, request, context):
        return barbot_pb2.OrderReply(ack='Received order from %s!' % request.user_id)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    barbot_pb2_grpc.add_BarbotServicer_to_server(Barbot(), server)
    with open(private_key_path, 'rb') as f:
        private_key = f.read()
    with open(certificate_path, 'rb') as f:
        certificate_chain = f.read()
    server_credentials = grpc.ssl_server_credentials( ( (private_key, certificate_chain), ) )
    server.add_insecure_port('0.0.0.0:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
