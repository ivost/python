import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

broker="broker.emqx.io"
topic = "ivo/temp"

client = mqtt.Client("P2") #create new instance

print("connecting to broker")
client.connect(broker, 1883) 
client.subscribe(topic)

client.on_message=on_message

client.loop_start()    #start the loop

time.sleep(100) # wait

client.loop_stop() #stop the loop
