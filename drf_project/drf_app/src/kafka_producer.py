from kafka import KafkaProducer, KafkaConsumer

producer = KafkaProducer(
    bootstrap_servers=['kafka1:9092'],
    # value_serializer=lambda x: bytes(x, 'utf-8')
)

consumer = KafkaConsumer('topic_sync',
                         bootstrap_servers=['kafka1:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         value_deserializer=[lambda x: x.decode("utf-8")],
                         api_version=(0, 10),
                         consumer_timeout_ms=1000)
