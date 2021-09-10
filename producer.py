from kafka import KafkaProducer

TOPIC_NAME = ''
KAFKA_SERVER = ''

producer = KafkaProducer(bootstrap_server=KAFKA_SERVER)
producer.send(TOPIC_NAME, b'Test Message!')
producer.flush()