"""
# generators / pipelines

file_name = "techcrunch.csv"
 2 lines = (line for line in open(file_name))
 3 list_line = (s.rstrip()split(",") for s in lines)
 4 cols = next(list_line)
 5 company_dicts = (dict(zip(cols, data)) for data in list_line)
 6 funding = (
 7     int(company_dict["raisedAmt"])
 8     for company_dict in company_dicts
 9     if company_dict["round"] == "A"
10 )
11 total_series_a = sum(funding)
12 print(f"Total series A fundraising: ${total_series_a}")
"""
import time
import datetime

import struct
import paho.mqtt.client as mqtt
import time
from random import seed, randint

# MQTT

broker = "test.mosquitto.org"
topic = "ivotemp"

def on_receive(client, userdata, message):
    top = str(message.topic)
    msg = str(message.payload.decode("utf-8"))
    # val = struct.unpack("h", message.payload)[0]
    print("received {}:{} ", format(topic, val))

def main():
    global mqtt_client
    mqtt_client = mqtt.Client("thingy52-1")
    print("connect")
    mqtt_client.connect(broker, 1883)
    mqtt_client.subscribe(topic)
    mqtt_client.on_message = on_receive
    mqtt_client.loop_start()

    seed(1)

    # Main program loop
    while 1:
        value = str(randint(2400, 2600))
        #val = struct.pack("h", value)
        print("publish " + value)
        #print("publish {}:{}", format(topic, value))
        mqtt_client.publish(topic, value)
        time.sleep(1)


def lines(file_path):
    for line in open(file_path):
        yield line.rstrip()


def readings():
    """
    tuple with 3 fields:
    id - string
    time - simulated
    value - float
    :return:
    """
    file_path = './temperature.txt'
    for line in lines(file_path):
        cols = line.split(',')
        yield cols


# for r in readings():
#    print(r)

main()
