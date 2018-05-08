import paho.mqtt.client as mqtt
import sys
client = mqtt.Client()
client.connect("/",1883,60)
client.publish("topic/test", sys.argv[1]);
client.disconnect();
