from kafka import KafkaConsumer
from helper.helper import show_list_of_messages_in_topic


'''
TOPIC_NAME = 'TestTopic'

consumer = KafkaConsumer(TOPIC_NAME)
print(consumer.topics())
for message in consumer:
    print(message)
    
'''

show_list_of_messages_in_topic()

