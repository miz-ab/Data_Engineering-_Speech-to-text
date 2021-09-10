from kafka import KafkaConsumer


TOPIC_NAME = 'TestTopic'

consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    print(message)
