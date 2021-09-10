from kafka import KafkaConsumer

TOPIC_NAME = 'TestTopic'

def show_list_of_topics():
    consumer = KafkaConsumer(TOPIC_NAME)
    print(consumer.topics())

def show_list_of_messages_in_topic():
    consumer = KafkaConsumer(TOPIC_NAME)
    for message in consumer:
        print(message.value)
