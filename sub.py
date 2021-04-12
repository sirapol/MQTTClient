# Python version : 3.7.3

import sys
import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime
print("import finish")

if (sys.argv[1]=="-h") or len(sys.argv)<5:
    print("sizeof : ",len(sys.argv))
    print("help")
    print("e.g. python3 sub.py host port user pass")
    quit()


host = sys.argv[1]          # your host name
port = int(sys.argv[2])       # your port
mqUsr = sys.argv[3]      # username
mqPas = sys.argv[4]      # pass

topicMain = "test/#"
topic1 = "topic/1"

def on_message(client, userdata, message):
    time.sleep(1)
    print(datetime.now(),"received message =",str(message.payload.decode("utf-8")))

def message_1(client,userdata,msg):                 # secondary subscribe callback
    print("from ",topic1)
    print(msg.payload.decode("utf-8"))

client= mqtt.Client()
client.message_callback_add(topic1,message_1)       # add  secondary subscribe 
client.on_message=on_message
client.username_pw_set(mqUsr,mqPas)                 # set username , password
client.connect(host,port)                           # connect to host with port
print("mqtt connected")
client.loop_start()
client.subscribe(topicMain)                         # add primary subscribe 

while True :                                        # while loop for receive data
    pass 
