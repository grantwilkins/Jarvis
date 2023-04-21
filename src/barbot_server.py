from concurrent import futures
import logging
import sys
sys.path.append('../device')
import grpc
import barbot_pb2_grpc
import barbot_pb2
#import pumping_system
class Barbot(barbot_pb2_grpc.BarbotServicer):

    def PlaceOrder(self, request, context):
        order_array = []
        print("Received order from " + request.user_id + " for " + request.drink_name)
        for i in range(len(request.container_amounts)):
            order_array.append((request.container_amounts[i].container_id, request.container_amounts[i].amount_oz))
            print("Pumping out " + str(request.container_amounts[i].amount_oz) + " oz from " + str(request.container_amounts[i].container_id))
        #if(request.flavor_id != 0):
            #pumping_system.flavor_out(flavor_num=request.flavor_id)
        #pumping_system.pump_handler(order_array)
        return barbot_pb2.OrderReply(user_id=request.user_id, drink_name=request.drink_name, flavor_name=request.flavor_name)

    def CleanSystem(self, request, context):
        print("Received clean request from " + request.user_id)
        #pumping_system.clean_system()
        return barbot_pb2.CleanReply(user_id=request.user_id)

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
    #pumping_system.init_pumping_system()
    serve()
