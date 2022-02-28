from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=["192.168.48.4:9093"],
    value_serializer=lambda x: bytes(x, 'utf-8')
)
