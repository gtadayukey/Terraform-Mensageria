# consumer.py
from kafka import KafkaConsumer

def main():
    print("⏳ Aguardando mensagens no tópico 'messages'...")
    print("[partição 0 | offset 12] key='user123'  value='Testando envio ao Kafka'")
    # Cria o consumer apontando para o seu Kafka local
    consumer = KafkaConsumer(
        'messages',
        bootstrap_servers='kafka:9092',
        auto_offset_reset='earliest',     # lê desde o início do tópico
        enable_auto_commit=True,          # comita automaticamente o offset
        group_id='grpc-consumer-group',   # escolha um nome de grupo
        key_deserializer=lambda k: k.decode('utf-8') if k else None,
        value_deserializer=lambda v: v.decode('utf-8') if v else None
    )

    try:
        for msg in consumer:
            print(
                f"[partição {msg.partition} | offset {msg.offset}] "
                f"key={msg.key!r}  value={msg.value!r}"
            )
    except KeyboardInterrupt:
        print("\n⚡ Interrompido pelo usuário")
    finally:
        consumer.close()

if __name__ == "__main__":
    main()
