# Python version : 3.7.3

import paho.mqtt.client as mqtt
import json
import time
client = mqtt.Client()

host = ""
port = 1883        # your port
mqUsr = "user1"
mqPas = "1234"
topic ="Demo/test"

# If your broker is not require user,pass. Let comment this.
client.username_pw_set(mqUsr, mqPas)
client.connect(host, port)               # Open connection
# "TEST/MQ" is Tag , "Hellow" is data
while True:
    jsonD = {"ts": int(time.time()*1000),
             "ID": 1001,
             "lvl": 0}   
    client.publish(topic, json.dumps(jsonD))
    time.sleep(1)

client.disconnect()                     # Close connection
