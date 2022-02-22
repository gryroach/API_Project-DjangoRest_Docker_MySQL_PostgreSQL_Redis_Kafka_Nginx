from pykafka import KafkaClient

client = KafkaClient(hosts='kafka:9093')
topic = client.topics['sync']
balanced_consumer = topic.get_balanced_consumer(
    consumer_group='syncgroup',
    auto_commit_enable=True,
    zookeeper_connect='zookeeper:2181'
)
