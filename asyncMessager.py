import uasyncio as asyncio
from umqtt.robust import MQTTClient
import ujson
import config

def sub_cb(topic, msg):
	if (topic == "home/attackHeater/stat"):
		print(msg)

class AsyncMqttMessages(object):
	def __init__(self):
		self.heatmessage = {'Heating':''}
		self.tempMessage = {'TempIN':'', 'TempOUT':''}
		self.mqttID = config.mqttID
		self.mqttBroker = config.mqttBroker
		self.user = config.mqttuser
		self.password = config.mqttpassword
		self.client = MQTTClient(self.mqttID, self.mqttBroker, self.user, self.password, port=1883)
		self.client.connect()
		self.client.set_callback(sub_cb)
		self.client.subscribe(topic="home/attackHeater/stat")

	def publishHeat(message):
		self.heatmessage = self.heatmessage['heating'] = message
		m = ujson.dumps(self.heatmessage)
		self.client.publish(topic="home/attacHeater/heating", msg=m)
	def publishTemp(temp_in, temp_out):
		self.tempMessage['TempIN'] = temp_in
		self.tempMessage['TempOUT'] = temp_out
		m = ujson.dumps(self.tempMessage)
		self.client.publish(topic="home/attacHeater/heating", msg=m)
