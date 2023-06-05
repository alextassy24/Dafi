from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Temperature, Pressure
import asyncio
import json

tempMinValue = ''
tempMaxValue = ''
pressMinValue = ''
pressMaxValue = ''
machine = None
temperature = ''
pressure = ''
iteration = ''

class StateMachine():
    def __init__(self,tempMin,tempMax,pressMin,pressMax):
        self.state = 'Initializing'
        self.tempMin = tempMin
        self.tempMax = tempMax
        self.pressMin = pressMin
        self.pressMax = pressMax
        self.pressure = pressMin
        self.temperature = tempMin
        self.generating = True

    def idle(self):
        self.state = 'IDLE'
        
    def stop(self):
        self.state = 'System stopped'
        self.generating = False
    
    def cooling(self):
        self.state = 'COOLING'
        self.generating = True
        
    
    def heating(self):
        self.state = 'HEATING'
        self.generating = True
        

class SendConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("my_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("my_group", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data['action'] is None:
            global tempMinValue, tempMaxValue, pressMinValue, pressMaxValue, machine, temperature, pressure, iteration
            tempMinValue = data['tempMinValue']
            tempMaxValue = data['tempMaxValue']
            pressMinValue = data['pressMinValue']
            pressMaxValue = data['pressMaxValue']
            
            machine = StateMachine(tempMinValue, tempMaxValue, pressMinValue, pressMaxValue)
            
        else:
            self.action = data['action']
            await self.send_data(self.action)
            
    async def send_data(self, action):
        print(self.action)
        if action == 'start':
            asyncio.sleep(2)
            machine.idle()
            for i in range(tempMaxValue + 1 - tempMinValue):
                if not machine.generating:
                    break
                machine.temperature = tempMinValue + i
                machine.pressure = pressMinValue + i
                await self.send_values(machine)
                await self.save_temperature(machine.temperature)
                await self.save_pressure(machine.pressure)
                
            
        elif action == 'stop':
            machine.stop()
            machine.generating = False
            
        elif action == 'cooling':
            machine.cooling()
            # for i in range(iteration,  tempMinValue):
            #     machine.temperature = tempMinValue + i
            #     machine.pressure = pressMinValue + i
            #     await self.send_values(machine)
            #     await self.save_temperature(machine.temperature)
            #     await self.save_pressure(machine.pressure)
            # iteration = i
            
        elif action == 'heating':
            machine.heating()

    async def send_values(self,machine):
        await self.send(json.dumps({
            'status': machine.state,
            'tempMinValue': tempMinValue,
            'tempMaxValue': tempMaxValue,
            'pressMinValue': pressMinValue,
            'pressMaxValue': pressMaxValue,
            'pressure': machine.pressure,
            'temperature': machine.temperature,
        }))

    @database_sync_to_async
    def save_temperature(self, value):
        temperature = Temperature(value=value)
        temperature.save()

    @database_sync_to_async
    def save_pressure(self, value):
        pressure = Pressure(value=value)
        pressure.save()
