import os
from concurrent import futures

import grpc
from kafka import KafkaProducer
import messaging_pb2 as pb2
import messaging_pb2_grpc as pb2_grpc

# Implementação do servicer gerado pelo protoc
class MessageService(pb2_grpc.MessageServiceServicer):
    def __init__(self, kafka_bootstrap):
        # cria o producer apontando para o host kafka definido em docker-compose
        self.producer = KafkaProducer(
            bootstrap_servers=kafka_bootstrap,
            key_serializer=lambda k: k.encode('utf-8'),
            value_serializer=lambda v: v.encode('utf-8')
        )

    def SendMessage(self, request, context):
        try:
            # envia para o tópico "messages"
            self.producer.send(
                topic='messages',
                key=request.key,
                value=request.value
            )
            self.producer.flush()
            return pb2.MessageResponse(success=True, error="")
        except Exception as e:
            return pb2.MessageResponse(success=False, error=str(e))


def serve():
    # lê a variável de ambiente definida no docker-compose
    # kafka_bootstrap = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092')
    kafka_bootstrap = os.getenv('KAFKA_BOOTSTRAP_SERVERS', '172.18.0.3:9092')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_MessageServiceServicer_to_server(
        MessageService(kafka_bootstrap),
        server
    )
    server.add_insecure_port('0.0.0.0:50051')
    print("gRPC server listening on 0.0.0.0:50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
