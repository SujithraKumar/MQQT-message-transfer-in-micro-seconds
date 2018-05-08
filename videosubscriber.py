#!/usr/bin/python

import time
import paho.mqtt.client as mqtt

def on_message(mosq, obj, msg):
    print "Topic : ",msg.topic
    with open('oneoombVideo.mp4', 'wb') as f:
        f.write(msg.payload)
    print "File transferred"




client = mqtt.Client()
client.connect("192.168.1.102",1883,60)
client.subscribe("video",0)
client.on_message = on_message

while True:
   client.loop(15)
   time.sleep(2)
