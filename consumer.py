from kafka import KafkaConsumer


TOPIC_NAME = ''

consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    print(message)
