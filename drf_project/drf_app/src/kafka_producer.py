from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['kafka:9093'],
    value_serializer=lambda x: bytes(x, 'utf-8')
)
