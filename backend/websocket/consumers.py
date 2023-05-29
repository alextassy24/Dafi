from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import asyncio
import json

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

class BaseConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.channel_layer = get_channel_layer()
        await self.channel_layer.group_add("my_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("my_group", self.channel_name)
    
    async def receive(self, text_data):

        data_values = json.loads(text_data)
        print(f"data:{data_values}")
        tempMinValue = data_values['tempMinValue']
        tempMaxValue = data_values['tempMaxValue']
        pressMinValue = data_values['pressMinValue']
        pressMaxValue = data_values['pressMaxValue']   
        machine = StateMachine(tempMinValue,tempMaxValue,pressMinValue,pressMaxValue)
        
        await self.channel_layer.group_send(
            "my_group",
            {
                "type": "send_data",
                "tempMinValue": tempMinValue,
                "tempMaxValue": tempMaxValue,
                "pressMinValue": pressMinValue,
                "pressMaxValue": pressMaxValue,
            },
        )
        async def send_data(self, event):
            tempMinValue = event["tempMinValue"]
            tempMaxValue = event["tempMaxValue"]
            pressMinValue = event["pressMinValue"]
            pressMaxValue = event["pressMaxValue"]
            
            print(f"Sending data: tempMinValue={tempMinValue}, tempMaxValue={tempMaxValue}, pressMinValue={pressMinValue}, pressMaxValue={pressMaxValue}")

class SendConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("my_group", self.channel_name)
        await self.accept()
        self.data = ''

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("my_group", self.channel_name)

    async def receive(self, text_data):
        self.data = json.loads(text_data)
        print(f"data:{self.data}")

        await self.send_data()

    async def send_data(self, event=None):
        print(event)
        if event:
            data_values = event['data']
            print(f"Received event data: {data_values}")
        else:
            data_values = {
                'tempMinValue': '0',
                'tempMaxValue': '0',
                'pressMinValue':'0',
                'pressMaxValue':'0',
            }
        
        tempMinValue = data_values['tempMinValue']
        tempMaxValue = data_values['tempMaxValue']
        pressMinValue = data_values['pressMinValue']
        pressMaxValue = data_values['pressMaxValue']
        
        
        if self.data['action'] == 'start':
            await asyncio.sleep(3)
            await self.send(json.dumps({'status': 'IDLE',
                                    'tempMinValue': tempMinValue,
                                    'tempMaxValue': tempMaxValue,
                                    'pressMinValue': pressMinValue,
                                    'pressMaxValue': pressMaxValue,}))
            
        elif self.data['action'] == 'stop':
            await asyncio.sleep(3)
            await self.send(json.dumps({'status': 'System stopped',
                                    'tempMinValue': tempMinValue,
                                    'tempMaxValue': tempMaxValue,
                                    'pressMinValue': pressMinValue,
                                    'pressMaxValue': pressMaxValue,}))
            
        elif self.data['action'] == 'cooling':
            await asyncio.sleep(3)
            await self.send(json.dumps({'status': 'COOLING',
                                    'tempMinValue': tempMinValue,
                                    'tempMaxValue': tempMaxValue,
                                    'pressMinValue': pressMinValue,
                                    'pressMaxValue': pressMaxValue,}))
            
        elif self.data['action'] == 'heating':
            await asyncio.sleep(3)
            await self.send(json.dumps({'status': 'HEATING',
                                    'tempMinValue': tempMinValue,
                                    'tempMaxValue': tempMaxValue,
                                    'pressMinValue': pressMinValue,
                                    'pressMaxValue': pressMaxValue,}))