import sys

import paho.mqtt.client as mqtt
import time
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision, WriteApi, rest
from influxdb_client.client.write_api import SYNCHRONOUS
from paho.mqtt.client import Client

writer = None
subscriber = None
topics = ["ivo/tc", "ivo/hp", "ivo/ph"]


def influx_init():
    global writer
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
    # ts = fields[0]
    sensor = fields[1]
    value = float(fields[2]) / 100.
    t = topic(message.topic)
    print(f"got {t}:{value}")
    data = f"{t},sensor={sensor} value={value}"
    print(f"write {data}")
    try:
        writer.write(bucket, org, data)
    except rest.ApiException as ex:
        # ex = sys.exc_info()[0]
        print(ex)


def mqtt_init():
    global subscriber
    broker = "broker.emqx.io"
    subscriber = mqtt.Client("mysub")  # create new instance

    print("connecting to broker " + broker)
    subscriber.connect(broker, 1883)
    subscriber.on_message = on_message
    for top in topics:
        print("subscribing to topic " + top)
        subscriber.subscribe(top)


def main():
    global subscriber

    influx_init()
    mqtt_init()

    subscriber.loop_start()
    while True:
        time.sleep(10)
    subscriber.loop_stop()  # stop the loop


main()
