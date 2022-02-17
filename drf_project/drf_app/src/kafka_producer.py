from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['broker:9092'],
    value_serializer=lambda x: str(x)
)
