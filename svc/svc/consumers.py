# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from clients.models import ChatRecord, User
# from asgiref.sync import sync_to_async
# from channels.db import database_sync_to_async
#
#
# class ChatConsumer(AsyncWebsocketConsumer):
#
#
#     @database_sync_to_async
#     def create_record(self, message, client_id, professional_id, senderId, roomName):
#         if self.user.id == client_id:
#             bool=False
#         else:
#             bool=True
#         ChatRecord.objects.create(client_id=client_id, professional_id=professional_id, message=message, room_name=roomName, side=bool)
#
#     async def connect(self):
#         self.user = self.scope['user']
#         self.to_user_id = self.scope['url_route']['kwargs']['to_user_id']
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = self.room_name
#         print(self.user, self.room_group_name)
#         # Join room group
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         await self.accept()
#
#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     # Receive message from WebSocket
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         senderId = text_data_json['senderId']
#         roomName = text_data_json['roomName']
#         client_id= text_data_json['client_id']
#         professional_id = text_data_json['professional_id']
#         await self.create_record(message, client_id, professional_id, senderId, roomName)
#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message,
#                 'senderId': senderId,
#                 'roomName': roomName
#             }
#         )
#
#     # Receive message from room group
#     async def chat_message(self, event):
#         message = event['message']
#         sender = event['senderId']
#         print("sending", message, event)
#         await self.send(text_data=json.dumps({
#             'message': message,
#             'id':sender
#         }))
