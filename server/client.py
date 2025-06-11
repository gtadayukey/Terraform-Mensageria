import grpc
import messaging_pb2 as pb2
import messaging_pb2_grpc as pb2_grpc

def run():
    channel = grpc.insecure_channel('172.18.0.4:50051')
    stub   = pb2_grpc.MessageServiceStub(channel)
    resp   = stub.SendMessage(pb2.MessageRequest(
        key='user123',
        value='Testando envio ao Kafka'
    ))
    print(f"sucesso={resp.success}, erro='{resp.error}'")

if __name__ == '__main__':
    run()
