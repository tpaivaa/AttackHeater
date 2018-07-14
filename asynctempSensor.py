import machine
import onewire, ds18x20
import uasyncio as asyncio

class OneWireTemps(object):
    def __init__(self, dt):
        self.dt = dt
        self.temps = []
        self.tempIN = ''
        self.tempOUT = ''
        self.pin = 25
        self.dat = machine.Pin(self.pin)
        self.ds = ds18x20.DS18X20(onewire.OneWire(self.dat))
        self.sensors = self.ds.scan()
        loop = asyncio.get_event_loop()
        loop.create_task(self.run())

    async def run(self):
        while True:
            if len(self.sensors) >= 1:
                self.ds.convert_temp()
                await asyncio.sleep_ms(750)
                for i,tempSensor in enumerate(self.sensors):
                    self.temps.append("{:.1f}".format(self.ds.read_temp(self.sensors[i])))
                self.dt.writeTemps(self.temps)
                self.tempIN = self.temps[0]
                self.tempOUT = self.temps[1]
                self.temps = []
            else:
                self.sensors = self.ds.scan()
                await asyncio.sleep_ms(1500)
            await asyncio.sleep_ms(1000)

    def getTemps(self):
        return { 'tempIN' : self.tempIN, 'tempOUT': self.tempOUT } 

    def getSensors(self):
        return self.sensors