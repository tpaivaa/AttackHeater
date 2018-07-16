import uasyncio as asyncio


class AsyncHeating(object):
	def __init__(self, arp, d, asm):
		self.arp = arp
		self.d = d
		self.asm = asm
		self.heat = not(self.arp.heatingPin.value())
		self.safety = self.arp.safety1.value() & self.arp.safety2.value()
		loop = asyncio.get_event_loop()
		loop.create_task(self.run())

	async def run(self):
			while self.safety:
				self.d.writeRun(int(not(self.arp.heatingPin.value())))
				self.heat = not(self.arp.heatingPin.value())
				if (self.heat):
					self.arp.heatON()
					#self.asm.publishHeat('ON')
				else:
					self.arp.heatOFF()
					#self.asm.publishHeat('OFF')
				await asyncio.sleep_ms(500)
				self.safety = self.arp.safety1.value() & self.arp.safety2.value()
			else:
				raise Exception('Heating Interupted')