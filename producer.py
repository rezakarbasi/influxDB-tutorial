from influxdb import InfluxDBClient
import datetime
import numpy as numpy

from influxdb import InfluxDBClient
import datetime
import numpy as np
import time

client = InfluxDBClient(database='shop') # default port 8086
while True:
    dt = str(datetime.datetime.now())
    room = np.random.randint(1,5)
    price = int(np.random.random()*50+10)/10
    weight = int(price/20 + np.random.random()*3)/10

    json_body = [{
                    'measurement':'customer',
                    'tags':{'room':room},
                    'fields':{'price':price,'weight':weight}#,
                    # 'time':dt
                }]
    client.write_points(json_body)
    print(json_body[0])
    time.sleep(0.1)
