# https://github.com/dpkp/kafka-python

from kafka import KafkaConsumer
from kafka import TopicPartition

consumer = KafkaConsumer('mytopic')

for msg in consumer:
	print (msg)


'''
consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
consumer.assign([TopicPartition('mytopic', 2)])

print("waiting...")
msg = next(consumer)
print(msg)
'''
