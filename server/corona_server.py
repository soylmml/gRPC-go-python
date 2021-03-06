from concurrent import futures
import logging

import grpc

import coronavirus_pb2
import coronavirus_pb2_grpc


class DatosCoronavirus(coronavirus_pb2_grpc.DatosCoronarirusServicer):

    def Datos(self, request, context):
        print("Datos recibidos!")
        print(request.datoscorona)
        return coronavirus_pb2.Reply(confirmacion='Datos recibidos:, %s!' % request.datoscorona)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    coronavirus_pb2_grpc.add_DatosCoronarirusServicer_to_server(DatosCoronavirus(), server)
    server.add_insecure_port('[::]:3001')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()

