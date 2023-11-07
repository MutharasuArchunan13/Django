import json
from channels.generic.websocket import AsyncWebsocketConsumer

class Publisher(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    
    async def disconnect(self,close_code):
        pass

    @staticmethod
    async def publish_task_status(task_id):
        status = Task.objects.get(pk=task_id).status
        await Publisher.send_status_update(task_id,status)
    
    @staticmethod
    async def send_status_update(task_id,status):
        await Publisher(f"/ws/task/{task_id}").send(text_data=json.dumps({'status':status}))