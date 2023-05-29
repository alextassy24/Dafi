from channels.generic.websocket import AsyncWebsocketConsumer
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
        pass
    
    def cooling(self):
        pass
    
    def heating(self):
        pass

class BaseConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass
    
    async def receive(self, text_data):

        data = json.loads(text_data)
        print(f"data:{data}")
        tempMinValue = data['tempMinValue']
        tempMaxValue = data['tempMaxValue']
        pressMinValue = data['pressMinValue']
        pressMaxValue = data['pressMaxValue']   
        machine = StateMachine(tempMinValue,tempMaxValue,pressMinValue,pressMaxValue)

    async def send(self, text_data):
        pass