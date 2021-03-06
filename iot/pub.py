import paho.mqtt.client as mqtt
import time

broker="broker.emqx.io"
#broker = "test.mosquitto.org"   # broker.emqx.io"

topic = "ivo/tc"
#topic = "sc160_temp"

client = mqtt.Client("mypub")
val = 2501
id = 112233
print("connecting to broker", broker, "topic", topic)
client.connect(broker, 1883)

for i in range(100):
    now = int(time.time())
    msg = "{},{},{}".format(now, id, val)
    print("sending ", topic, msg)
    client.publish(topic, msg)
    val = val + 20
    time.sleep(2)
