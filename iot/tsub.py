import sys

import paho.mqtt.client as mqtt
import time
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision, WriteApi, rest
from influxdb_client.client.write_api import SYNCHRONOUS
from paho.mqtt.client import Client

writer = None
subscriber = None
#topics = ["ivo/tc", "ivo/hp", "ivo/ph"]
topics = ["sc160_temp"]


def influx_init():
    global writer
    print("influx_init")
    token = "dirs2RRmP64CaJ6AZ6dkhvvBRCYogzs4mXGG-BEhYboLSFaJ0WBfqmMNEmMxwH58znBM26VPaMeaXOtL9teLKg=="
    client = InfluxDBClient(url="https://us-west-2-1.aws.cloud2.influxdata.com", token=token)
    writer = client.write_api(write_options=SYNCHRONOUS)


def topic(t):
    map = {topics[0]: "temp", topics[1]: "hum", topics[2]: "baro"}
    return map.get(t, "unknown")


def on_message(client, userdata, message):
    global writer
    org = "ac5f998776be2950"
    bucket = "ivo1"

    msg = str(message.payload.decode("utf-8"))
    fields = msg.split(',')
    sensor = fields[1]
    value = float(fields[2]) / 100.
    t = "temp"  #topic(message.topic)
    m = f"{t},sensor={sensor} value={value}"
    try:
        #print("sending", m)
        writer.write(bucket, org, m)
        print("sent", m)
    except rest.ApiException as ex:
        # ex = sys.exc_info()[0]
        print(ex)


def mqtt_init():
    global subscriber
    #broker = "test.mosquitto.org"   # broker.emqx.io"
    broker = 'broker.emqx.io'

    subscriber = mqtt.Client("IvoSC160_2")  # create new instance
    subscriber.on_message = on_message

    print("connecting to broker " + broker)
    subscriber.connect(broker, 1883)
    print("connected")

    subscriber.subscribe("ivo/tc")
    print("subscribed to ivo/tc")

    #for top in topics:
    #    print("subscribing to topic " + top)
    #    subscriber.subscribe(top)


def main():
    global subscriber

    mqtt_init()
    influx_init()

    print("subscriber.loop_start()")
    subscriber.loop_start()
    while True:
        #print("sleep")
        time.sleep(1)

    print("subscriber.loop_stop()")
    subscriber.loop_stop()  ## stop the loop


main()
