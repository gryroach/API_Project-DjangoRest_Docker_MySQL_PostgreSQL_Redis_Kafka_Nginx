from kafka import KafkaProducer, KafkaConsumer

producer = KafkaProducer(
    bootstrap_servers='172.20.0.3:9093',
    value_serializer=lambda x: bytes(x, 'utf-8')
)

consumer = KafkaConsumer('sync',
                         bootstrap_servers=['kafka:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         value_deserializer=[lambda x: x.decode("utf-8")],
                         api_version=(0, 10),
                         consumer_timeout_ms=1000)
