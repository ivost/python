from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "dirs2RRmP64CaJ6AZ6dkhvvBRCYogzs4mXGG-BEhYboLSFaJ0WBfqmMNEmMxwH58znBM26VPaMeaXOtL9teLKg=="
org = "ac5f998776be2950"
bucket = "ivo1"

client = InfluxDBClient(url="https://us-west-2-1.aws.cloud2.influxdata.com", token=token)

w = client.write_api(write_options=SYNCHRONOUS)


data = "mem,host=host1 used_percent=20"
w.write(bucket, org, data)

data = "mem,host=host1 used_percent=25"
w.write(bucket, org, data)

data = "mem,host=host1 used_percent=10"
w.write(bucket, org, data)
