from pykafka import KafkaClient

client = KafkaClient(hosts='kafka:9093')
topic = client.topics['sync']
