from kafka import KafkaConsumer


TOPIC_NAME = 'TestTopic'

consumer = KafkaConsumer(TOPIC_NAME)
print(consumer.topics())
for message in consumer:
    print(message)
