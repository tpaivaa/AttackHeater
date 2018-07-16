import machine
from machine import Pin
import uasyncio as asyncio
from asynctempSensor import OneWireTemps
from asyncDisplay import AsyncWriteTemp
from asyncRelePins import AsyncRelePins
from asyncHeating import AsyncHeating
from asyncMessager import AsyncMqttMessages
import paawodyfi as wlan

async def killer():
	pin = Pin(14, Pin.IN, Pin.PULL_UP)
	while pin.value():
		await asyncio.sleep_ms(50)

try:
	wlan.connect()
	while True:
		d = AsyncWriteTemp() 				# writes temps to display
		t = OneWireTemps(d) 				# gets temps from sensors
		arp = AsyncRelePins(d) 				# control of relay's
		asm = AsyncMqttMessages()			# mqtt messages
		h = AsyncHeating(arp, d, asm)		# control of Heating
		loop = asyncio.get_event_loop()		# Eventloop
		loop.run_until_complete(killer())	# run until button pushed (reset)

except Exception as e:
	d.write('Heating interupted!')
	machine.reset()
	d.write('Resetted')