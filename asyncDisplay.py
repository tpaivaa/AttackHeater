from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
import uasyncio as asyncio

class AsyncWriteTemp():
	def __init__(self):
		self.temps = ['-','-']
		self.status = 'OFF'
		self.on = self.status
		self.DEFAULT_I2C_ADDR =  0x3f
		self.i2c = I2C(scl=Pin(13), sda=Pin(27), freq=400000)
		self.lcd = I2cLcd(self.i2c, self.DEFAULT_I2C_ADDR, 2, 16)
		self.aste = [0xe,0xa,0xe,0x0,0x0,0x0,0x0,0x0]
		self.lcd.custom_char(0, bytearray(self.aste))
		self.lcd.clear()
		self.lcd.move_to(0, 0)
		self.lcd.putstr("in  ")
		self.lcd.putstr(self.temps[0])
		self.lcd.putchar(chr(0))
		self.lcd.putstr("C")
		self.lcd.move_to(0, 1)
		self.lcd.putstr("out ")
		self.lcd.putstr(self.temps[1])
		self.lcd.putchar(chr(0))
		self.lcd.putstr("C")
		self.lcd.move_to(13, 0)
		self.lcd.putstr(self.on)
		loop = asyncio.get_event_loop()
		loop.create_task(self.run())

	async def run(self):
		while True:
			self.lcd.move_to(4, 0)
			self.lcd.putstr(self.temps[0])
			self.lcd.putchar(chr(0))
			self.lcd.putstr("C")
			self.lcd.move_to(4, 1)
			self.lcd.putstr(self.temps[1])
			self.lcd.putchar(chr(0))
			self.lcd.putstr("C")
			await asyncio.sleep_ms(2000)

	def write(self, text):
		self.lcd.clear()
		self.lcd.move_to(0, 0)
		self.lcd.putstr(text)

	def writeRun(self,status):
		if (status == 1):
			self.on = 'ON '
		else:
			self.on = 'OFF'
		self.lcd.move_to(13, 0)
		self.lcd.putstr(self.on)

	def counter(self, count):
		self.lcd.move_to(14, 1)
		self.lcd.putstr(count)

	def highvoltageState(self, state1, state2):
		self.lcd.move_to(11, 1)
		self.lcd.putstr(state1)
		self.lcd.putstr(state2)

	def writeTemps(self,temps):
		self.temps = temps
	def lightsOFF(self):
		self.lcd.backlight_off()
	def lightsON(self):
		self.lcd.backlight_on()
