import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    print(f"got {message.topic}:{msg}")

broker="broker.emqx.io"
topics = ["ivo/tc", "ivo/hp", "ivo/ph"]

client = mqtt.Client("mysub") #create new instance

print("connecting to broker " + broker)
client.connect(broker, 1883)

for topic in topics:
    print("subscribing to topic " + topic)
    client.subscribe(topic)

client.on_message=on_message

client.loop_start()    #start the loop
while True:
    time.sleep(1) # wait

client.loop_stop() #stop the loop