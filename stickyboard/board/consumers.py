import json

from channels.generic.websocket import AsyncWebsocketConsumer

class BoardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        note_info = text_data_json['note_info']
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'board_update',
                'note_info': note_info
            }
        )

    async def board_update(self, event):
        note_info = event['note_info']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'note_info': note_info
        }))