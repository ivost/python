import json
from kafka import KafkaProducer

print("kafka sender")

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for _ in range(3):
	print("sending...")
    producer.send('mytopic', {'foo': 'bar'})

# Block until all pending messages are sent
producer.flush()
