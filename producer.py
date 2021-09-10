from kafka import KafkaProducer

TOPIC_NAME = 'TestTopic'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
producer.send(TOPIC_NAME, b'Test Message five!')
producer.flush()