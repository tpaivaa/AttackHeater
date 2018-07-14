from machine import Pin
import uasyncio as asyncio


class AsyncRelePins(object):
	def __init__(self, awt):
		self.awt = awt
		self.rele1 = Pin(18, Pin.OUT, Pin.PULL_DOWN, value=1)
		self.rele2 = Pin(19, Pin.OUT, Pin.PULL_DOWN, value=1)
		self.rele3 = Pin(21, Pin.OUT, Pin.PULL_DOWN, value=1)
		self.rele4 = Pin(22, Pin.OUT, Pin.PULL_DOWN, value=1)
		self.heatingPin = Pin(26, Pin.IN, Pin.PULL_UP)
		self.safety1 = Pin(34, Pin.IN, Pin.PULL_UP)
		self.safety2 = Pin(35, Pin.IN, Pin.PULL_UP)

	def heatON(self):
		self.rele1.value(0)
		self.rele2.value(0)
		self.rele3.value(0)
		self.rele4.value(0)
	def heatOFF(self):
		self.rele1.value(1)
		self.rele2.value(1)
		self.rele3.value(1)
		self.rele4.value(1)
	def pumpON(self):
		self.rele1.value(0)
	def pumpOFF(self):
		self.rele1.value(1)
