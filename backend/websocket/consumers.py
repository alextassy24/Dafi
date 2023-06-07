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
iteration = 0

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
            iteration = 0
            tempMinValue = data['tempMinValue']
            tempMaxValue = data['tempMaxValue']
            pressMinValue = data['pressMinValue']
            pressMaxValue = data['pressMaxValue']
            
            machine = StateMachine(tempMinValue, tempMaxValue, pressMinValue, pressMaxValue)
            
        else:
            self.action = data['action']
            await self.send_data(self.action)
            
    async def send_data(self, action):
        global iteration
        print(self.action)
        if action == 'start':
            await asyncio.sleep(1)
            machine.idle()
            
            async def generate_data():
                global iteration
                
                while True:
                    await asyncio.sleep(2)
                    print(machine.state)
                    if not machine.generating:
                        print(machine.state)
                        break
                    print(f'iteration:{iteration}')
                    
                    machine.temperature = tempMinValue + iteration
                    machine.pressure = pressMinValue + iteration
                    await self.send_values(machine)
                    await self.save_temperature(machine.temperature)
                    await self.save_pressure(machine.pressure)
                    iteration += 1
                
            asyncio.create_task(generate_data())
            
        elif action == 'stop':
            machine.stop()
            await self.send(json.dumps({
            'status': machine.state,
            'tempMinValue': tempMinValue,
            'tempMaxValue': tempMaxValue,
            'pressMinValue': pressMinValue,
            'pressMaxValue': pressMaxValue,
            'pressure': machine.pressure,
            'temperature': machine.temperature,
            }))
            
        elif action == 'cooling':
            machine.cooling()
            # async def generate_data():
            #     global iteration
                
            #     while True:
            #         await asyncio.sleep(2)
            #         print(machine.state)
            #         if not machine.generating:
            #             print(machine.state)
            #             break
            #         print(f'iteration:{iteration}')
                    
            #         machine.temperature += iteration
            #         machine.pressure += iteration
            #         await self.send_values(machine)
            #         await self.save_temperature(machine.temperature)
            #         await self.save_pressure(machine.pressure)
            #         iteration += 1
                
            # asyncio.create_task(generate_data())
            
        elif action == 'heating':
            machine.heating()
            # async def generate_data():
            #     global iteration

            #     while True:
            #         await asyncio.sleep(2)
            #         print(machine.state)
            #         machine.temperature += iteration
            #         machine.pressure += iteration
            #         await self.send_values(machine)
            #         await self.save_temperature(machine.temperature)
            #         await self.save_pressure(machine.pressure)
            #         print(f'iteration:{iteration}')
            #         iteration += 1

            #         if machine.generating == False:
            #             print(machine.state)
            #             break
                
            # asyncio.create_task(generate_data())

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
