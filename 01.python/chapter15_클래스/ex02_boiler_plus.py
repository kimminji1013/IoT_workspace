# 보일러 대신에 다른 기능도 사용하고 싶을 때
# 보일러 대신 함수로 받자

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

class Light:
    def on(self):
        print('전등이 켜집니다.')

class Controller:
    def __init__(self, base, func):
        self.base = base
        self.func = func
        self._temp = 10
   
    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        if value < self.base:
            self.func()         # 만약, 41번 줄 없이 42번줄에서 Light.on을 했다면 self.func(self)로 사용해야 함.
        self._temp = value


tsensor = TempSensor()
light = Light()
controller = Controller(5, light.on)

while True:
    controller.temp = tsensor.read_temp()
    print(controller.temp)
    time.sleep(1)