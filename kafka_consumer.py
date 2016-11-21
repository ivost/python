# https://github.com/dpkp/kafka-python

from kafka import KafkaConsumer
from kafka import TopicPartition

consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
consumer.assign([TopicPartition('mytopic', 1)])

print("waiting...")
msg = next(consumer)
print(msg)

