import paho.mqtt.client as mqtt
import time

broker="broker.emqx.io"
topic = "ivo/temp"

client = mqtt.Client("mypub")

print("connecting to broker", broker)
client.connect(broker, 1883)

for i in range(12):
    time.sleep(1)
    now = int(time.time())
    msg = f"{now},tc,{i}"
    print(f"sending {topic}:{msg}")
    client.publish(topic, msg)