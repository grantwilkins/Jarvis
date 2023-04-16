from concurrent import futures
import logging
import sys
sys.path.append('../device')
import grpc
import barbot_pb2_grpc
import barbot_pb2
import pumping_system
class Barbot(barbot_pb2_grpc.BarbotServicer):

    def PlaceOrder(self, request, context):
        print("Received order from " + request.user_id + " for " + request.drink_name)
        pumping_system.pump_out(request.container_num, request.amount_oz)
        return barbot_pb2.OrderReply(user_id=request.user_id, drink_name=request.drink_name)

    def InjectFlavor(self, request, context):
        print("Received flavor injection from " + request.user_id + " for " + request.flavor_name)
        return barbot_pb2.FlavorReply(user_id=request.user_id, flavor_name=request.flavor_name)
    
    def QueryLevels(self, request, context):
        print("Received level query from " + request.user_id)
        return barbot_pb2.LevelReply(container_id=request.container_id, container_level=100)

def serve():
    port = '5005'
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
