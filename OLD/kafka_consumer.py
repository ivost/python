# https://github.com/dpkp/kafka-python

from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('mytopic')

print 'waiting...'
for msg in consumer:
	print msg.value
	print 'waiting...'


'''
consumer = KafkaConsumer('mytopic', value_deserializer=json.loads)
from kafka import TopicPartition
	# p = Payload(msg)
	# print p
	# print p.foo
	p = lambda:None
	p.__dict__ = json.loads(msg.value)
	print p.foo

consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
consumer.assign([TopicPartition('mytopic', 2)])

print("waiting...")
msg = next(consumer)
print(msg)
class Payload(object):
	def __init__(self, j):
		self.__dict__ = json.loads(j)


'''
