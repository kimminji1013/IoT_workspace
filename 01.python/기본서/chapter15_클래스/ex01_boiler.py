import random
import time

class TempSensor:
    def __init__(self):
        self.value = 5

    def read_temp(self):
        self.value += random.uniform(-2,1)
        return self.value

class Boiler:
    def on(self):
        print('보일러가 켜집니다.')


class Controller:
    def __init__(self, base):
        self.base = base
        self.boiler = Boiler()
        self._temp = 10

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        if value < self.base:
            self.boiler.on()
        self._temp = value

tsensor = TempSensor()
controller = Controller(5)

while True:
    controller.temp = tsensor.read_temp()
    print(controller.temp)
    time.sleep(1)