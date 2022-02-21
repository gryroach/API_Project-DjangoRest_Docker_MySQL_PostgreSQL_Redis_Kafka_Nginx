from kafka import KafkaConsumer


consumer = KafkaConsumer('sync',
                         bootstrap_servers=['kafka:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='my-group-1',
                         value_deserializer=[lambda x: x.decode("utf-8")],
                         api_version=(0, 10),
                         consumer_timeout_ms=1000)

consumer2 = KafkaConsumer('sync',
                          bootstrap_servers=['kafka:9093'],
                          auto_offset_reset='earliest',
                          enable_auto_commit=True,
                          group_id='my-group-1',
                          value_deserializer=[lambda x: x.decode("utf-8")],
                          api_version=(0, 10),
                          consumer_timeout_ms=1000)

consumer3 = KafkaConsumer('sync',
                          bootstrap_servers=[':9092'],
                          auto_offset_reset='earliest',
                          enable_auto_commit=True,
                          value_deserializer=[lambda x: x.decode("utf-8")],
                          api_version=(0, 10),
                          consumer_timeout_ms=1000)

consumer4 = KafkaConsumer('sync',
                          bootstrap_servers=[':9093'],
                          auto_offset_reset='earliest',
                          enable_auto_commit=True,
                          value_deserializer=[lambda x: x.decode("utf-8")],
                          api_version=(0, 10),
                          consumer_timeout_ms=1000)