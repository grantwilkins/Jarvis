from concurrent import futures
import logging
import sys
sys.path.append('../device')
import grpc
import barbot_pb2_grpc
import barbot_pb2
import pumping_system
import Container
class Barbot(barbot_pb2_grpc.BarbotServicer):

    def PlaceOrder(self, request, context):
        print("Received order from " + request.user_id + " for " + request.drink_name)
        pumping_system.pump_out(Container("Vodka", 10, 1), 1)
        return barbot_pb2.OrderReply(ack='Completed order for ' + request.drink_name + ' from ' + request.user_id)

    def InjectFlavor(self, request, context):
        print("Received flavor injection from " + request.user_id + " for " + request.flavor_name)
        return barbot_pb2.FlavorReply(ack='Completed flavor injection for ' + request.flavor_name + ' from ' + request.user_id)
    
    def QueryLevels(self, request, context):
        print("Received level query from " + request.user_id)
        return barbot_pb2.LevelReply(ack='Completed level query from ' + request.user_id)

def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    barbot_pb2_grpc.add_BarbotServicer_to_server(Barbot(), server)
    server.add_insecure_port('0.0.0.0:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()
    

if __name__ == '__main__':
    logging.basicConfig()
    pumping_system.init_pumping_system()
    serve()
