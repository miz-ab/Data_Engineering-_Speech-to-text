from kafka import KafkaConsumer

TOPIC_NAME = 'TestTopic'


def show_list_of_topics():
    consumer = KafkaConsumer(TOPIC_NAME)
    print(consumer.topics())


def show_list_of_messages_in_topic():
    consumer = KafkaConsumer(TOPIC_NAME)
    message_list = []
    for message in consumer:
        message_list.append(message.value)
    print(message_list)
