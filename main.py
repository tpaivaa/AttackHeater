import machine
from machine import Pin
import uasyncio as asyncio
from asynctempSensor import OneWireTemps
from asyncDisplay import AsyncWriteTemp
from asyncRelePins import AsyncRelePins
from asyncHeating import AsyncHeating
from asyncMessager import AsyncMqttMessages
import paawodyfi as w

async def killer():
	pin = Pin(14, Pin.IN, Pin.PULL_UP)
	while pin.value():
		await asyncio.sleep_ms(50)

try:
	w.connect()
	while True:
		d = AsyncWriteTemp()
		t = OneWireTemps(d)
		arp = AsyncRelePins(d)
		#asm = AsyncMqttMessages()
		h = AsyncHeating(arp, d)
		loop = asyncio.get_event_loop()
		loop.run_until_complete(killer())

except Exception as e:
	d.write('Heating interupted!')
	machine.reset()
	d.write('Resetted')