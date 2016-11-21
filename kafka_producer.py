from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from kafka.producer import KafkaProducer
from time import sleep
from datetime import datetime
import json

print("kafka sender")

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
#producer = KafkaProducer(bootstrap_servers='localhost:9092')

for _ in range(5):
	print("sending...")
	producer.send('mytopic', {'foo': 'bar', 'age': 21})
	producer.flush()
	sleep(1)

'''


producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

	#producer.send('mytopic', b'MESSAGE')

for _ in range(3):
	print("sending...")
    producer.send('mytopic', {'foo': 'bar'})

# Block until all pending messages are sent
producer.flush()

#kafka = KafkaClient("localhost:9092")
kafka = KafkaClient()

producer = SimpleProducer(kafka)

while 1:
  producer.send_messages("mytopic", "Message " + str(datetime.now().time()) )
  sleep(1)

'''