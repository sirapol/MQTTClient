#Python version : 3.7.3

import paho.mqtt.client as mqtt

client = mqtt.Client()

host="yourHost"
port=500        # your port
mqUsr="user"
mqPas="password"

client.username_pw_set(mqUsr,mqPas)     # If your broker is not require user,pass. Let comment this.
client.connect(host,port)               # Open connection
client.publish("TEST/MQ","Hello")       # "TEST/MQ" is Tag , "Hellow" is data
client.disconnect()                     # Close connection