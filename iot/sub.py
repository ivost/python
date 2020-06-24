import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    #print(f"got {message.topic}:{msg}")
    #print("got msg", msg, "topic", message.topic)
    fields = msg.split(',')
    #print(fields)
    # ts = fields[0]
    sensor = fields[1]
    #print(sensor)
    value = float(fields[2]) / 100.
    #print(value)
    t = "temp"	#topic(message.topic)
    #m = '{},sensor={} value={}'.format(t, sensor, value)
    m = f"{t},sensor={sensor} value={value}"
    print("sending", m)


broker="broker.emqx.io"
topic = "ivo/tc"

client = mqtt.Client("mysub") #create new instance

client.on_message=on_message

print("connecting to broker " + broker)
client.connect(broker, 1883)

print("subscribing to topic " + topic)
client.subscribe(topic)


client.loop_start()    #start the loop
while True:
    time.sleep(1) # wait

client.loop_stop() #stop the loop