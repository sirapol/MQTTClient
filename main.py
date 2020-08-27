#Python version : 3.7.3

import paho.mqtt.client as mqtt
client = mqtt.Client()
host="58.64.25.160"
port=500
mqUsr="sirapsri"
mqPas="sirapsri"
client.username_pw_set(mqUsr,mqPas)
client.connect(host,port)
client.publish("TEST/MQ","Hello")
client.disconnect()