import paho.mqtt.client as mqtt
import time
import sys
import httplib, urllib
import json

sys.path.insert(0, '/usr/lib/python2.7/bridge/')
from bridgeclient import BridgeClient as bridgeclient

value = bridgeclient()
deviceId = "DoAbkdeD"
deviceKey = "8rNc4VefyorUw2pT"

dataChnId1 = "x"
dataChnId2 = "y"
dataChnId3 = "z"
MQTT_SERVER =  "192.168.5.104" # gateway IP
#MQTT_SERVER =  "192.168.5.104" #"mqtt.mcs.mediatek.com"
MQTT_PORT = 1883
MQTT_ALIVE = 60
#MQTT_TOPIC1 = "mcs/" + deviceId + "/" + deviceKey + "/" + dataChnId1
#MQTT_TOPIC2 = "mcs/" + deviceId + "/" + deviceKey + "/" + dataChnId2
#MQTT_TOPIC3 = "mcs/" + deviceId + "/" + deviceKey + "/" + dataChnId3
MQTT_TOPIC = "mcs/" + deviceId + "/" + deviceKey + "/" + dataChnId1
mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)

while True:
    x0 = value.get("x")
    y0 = value.get("y")
    z0 = value.get("z")
    s = "\!00Y3OUn4kwIJ0a1I#DLP9sgjy#" + str(x0) + "/" + str(y0) + "/" +str(z0)
    #payload = {"datapoints":[{"dataChnId":"x","values":{"value":x0}}]}
    mqtt_client.publish(MQTT_TOPIC, "%s" %(s), qos=0)
    #payload = {"datapoints":[{"dataChnId":"y","values":{"value":y0}}]}
    #mqtt_client.publish(MQTT_TOPIC2, json.dumps(payload), qos=0)
    #payload = {"datapoints":[{"dataChnId":"z","values":{"value":z0}}]}
    #mqtt_client.publish(MQTT_TOPIC3, json.dumps(payload), qos=0)
    time.sleep(1)
