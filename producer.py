from kafka import KafkaProducer

TOPIC_NAME = 'TestTopic'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_server=KAFKA_SERVER)
producer.send(TOPIC_NAME, b'Test Message!')
producer.flush()