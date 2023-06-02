from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import asyncio
import json

tempMinValue = ''
tempMaxValue = ''
pressMinValue = ''
pressMaxValue = ''
print("First loading")
print(f'tempMaxValue = {tempMaxValue}')
print(f'tempMinValue = {tempMinValue}')
print(f'pressMinValue = {pressMinValue}')
print(f'pressMaxValue = {pressMaxValue}')

class StateMachine():
    def __init__(self,tempMin,tempMax,pressMin,pressMax):
        self.state = 'Initializing'
        self.tempMin = tempMin
        self.tempMax = tempMax
        self.pressMin = pressMin
        self.pressMax = pressMax

    def idle(self):
        self.state = 'IDLE'
    
    def cooling(self):
        self.state = 'COOLING'
    
    def heating(self):
        self.state = 'HEATING'

class SendConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("my_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("my_group", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        print(f'data:', data)
        if data['action'] is None:
            global tempMinValue, tempMaxValue, pressMinValue, pressMaxValue
            tempMinValue = data['tempMinValue']
            tempMaxValue = data['tempMaxValue']
            pressMinValue = data['pressMinValue']
            pressMaxValue = data['pressMaxValue']
            
        else:
            self.action = data['action']
            await self.send_data(self.action)
            
    async def send_data(self, action):
        if action == 'start':
            await asyncio.sleep(3)
            await self.send(json.dumps({'status': 'IDLE',
                                    'tempMinValue': tempMinValue,
                                    'tempMaxValue': tempMaxValue,
                                    'pressMinValue':pressMinValue,
                                    'pressMaxValue':pressMaxValue,}))
            
        elif action == 'stop':
            await asyncio.sleep(3)
            await self.send(json.dumps({'status': 'System stopped',
                                    'tempMinValue': tempMinValue,
                                    'tempMaxValue': tempMaxValue,
                                    'pressMinValue': pressMinValue,
                                    'pressMaxValue': pressMaxValue,}))
            
        elif action == 'cooling':
            await asyncio.sleep(3)
            await self.send(json.dumps({'status': 'COOLING',
                                    'tempMinValue': tempMinValue,
                                    'tempMaxValue': tempMaxValue,
                                    'pressMinValue': pressMinValue,
                                    'pressMaxValue': pressMaxValue,}))
            
        elif action == 'heating':
            await asyncio.sleep(3)
            await self.send(json.dumps({'status': 'HEATING',
                                    'tempMinValue': tempMinValue,
                                    'tempMaxValue': tempMaxValue,
                                    'pressMinValue': pressMinValue,
                                    'pressMaxValue': pressMaxValue,})) 
        