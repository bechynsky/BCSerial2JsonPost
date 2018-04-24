import time
import requests
import serial
import json
import configparser

# creta config.ini file
# if URL contains % use %%
# [DEFAULT]
# URL = https://...
# COM = /dev/tty...

configuration = configparser.ConfigParser()
configuration.read('config.ini')


# This is URL from Request trigger
URL = configuration['DEFAULT']['URL']
PORT_NAME = configuration['DEFAULT']['COM']

# This is reqired by Request trigger
HEADER = {'Content-Type': 'application/json'}

# Connect to serial port
s = serial.Serial(PORT_NAME, 115200)


while True:
    # read data from serial port
    serialData = s.readline().decode('ascii').strip()
    jsonData = json.loads(serialData)
    
    topicParts = jsonData[0].split('/')
    
    if len(topicParts) != 4:
        continue

    # create payload
    payload = {'device': topicParts[0],
                'sensor': topicParts[1], 
                'sensorInfo': topicParts[2], 
                'measurement': topicParts[3],
                'value': jsonData[1],
                'time': time.strftime("%Y-%m-%d %H:%M:%S")}

    print(payload)  

    # send payload, payload is converted to JSON
    r = requests.post(URL, json = payload, headers=HEADER)
    # proper return code is 202 (Accepted), https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#2xx_Success
    print(r.status_code)
    
