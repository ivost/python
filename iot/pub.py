import paho.mqtt.client as mqtt
import time

broker="broker.emqx.io"
topic = "ivo/temp"

client = mqtt.Client("mypub")

print("connecting to broker")
client.connect(broker, 1883) 

for i in range(10):
	time.sleep(4) # wait
	print("Publishing message to topic", topic)
	client.publish(topic, str(i))

