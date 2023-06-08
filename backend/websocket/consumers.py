from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Temperature, Pressure
import asyncio
import json

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
        self.iteration = 0
        
    def set_state(self, state):
        self.state = state
        self.generating = False if state == 'System stopped' else True
    
    def increase(self):
        self.temperature += 1
        self.pressure += 1
        self.iteration += 1
        
    def decrease(self):
        self.temperature -= 1
        self.pressure -= 1
        self.iteration += 1
        
    def print_values(self):
        print(self.state)
        print(f'iteration:{self.iteration}')
        print(f'temperature:{self.temperature}\n pressure:{self.pressure}')
        
class SendConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("my_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("my_group", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data['action'] is None:
            tempMinValue = float(data['tempMinValue'])
            tempMaxValue = float(data['tempMaxValue'])
            pressMinValue = float(data['pressMinValue'])
            pressMaxValue = float(data['pressMaxValue'])
            global machine
            machine = StateMachine(tempMinValue, tempMaxValue, pressMinValue, pressMaxValue)
            
        else:
            self.action = data['action']
            await self.send_data(self.action)
            
    async def send_data(self, action):
        await asyncio.sleep(1)
        if action == 'start':
            machine.set_state('IDLE')
            asyncio.create_task(self.generate_data(True))
        elif action == 'stop':
            machine.set_state('System stopped')
            await self.process_data()
        elif action == 'cooling':
            machine.set_state('COOLING')
            asyncio.create_task(self.generate_data(False))
        elif action == 'heating':
            machine.set_state('HEATING')
            asyncio.create_task(self.generate_data(True))

    async def generate_data(self, increasing):
        while machine.generating:
            await asyncio.sleep(1)
            if increasing:
                machine.increase()
            else:
                machine.decrease()
            machine.print_values()
            await self.process_data()

    async def process_data(self):
        await self.send_values(machine)
        await self.save_temperature(machine.temperature)
        await self.save_pressure(machine.pressure)
        
    async def send_values(self,machine):
        await self.send(json.dumps({
            'status': machine.state,
            'tempMinValue': machine.tempMin,
            'tempMaxValue': machine.tempMax,
            'pressMinValue': machine.pressMin,
            'pressMaxValue': machine.pressMax,
            'pressure': machine.pressure,
            'temperature': machine.temperature,
            'iteration': machine.iteration
        }))

    @database_sync_to_async
    def save_temperature(self, value):
        temperature = Temperature(value=value)
        temperature.save()

    @database_sync_to_async
    def save_pressure(self, value):
        pressure = Pressure(value=value)
        pressure.save()
