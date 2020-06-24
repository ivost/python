import paho.mqtt.client as mqtt
import time

broker="broker.emqx.io"
#broker = "test.mosquitto.org"   # broker.emqx.io"

topic = "ivo/tc"
#topic = "sc160_temp"

client = mqtt.Client("mypub")

print("connecting to broker", broker, "topic", topic)
client.connect(broker, 1883)

for i in range(12000):
    time.sleep(10)
    now = int(time.time())
    msg = f"{now},123456,{i}"
    print(f"sending {topic}:{msg}")
    client.publish(topic, msg)