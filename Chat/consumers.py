import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .consumer_helpers import token_user, status, send_msg

# 1. FETCH all conversations (id's)
# 2. FETCH messages from all conversations
# 3. CONNECT to n conversations' n socket connections using conversation id's (Step 1)
# 3.a. Update contact status to active
# 4. Send and receive messages on socket connections
# 5. DISCONNECT 
# 5.a. Update contact status to inactive

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # set user active 
        try:
            user_id = await token_user(self.scope)
            await status(user_id, flag='connect')
        except:
            pass

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        # set user inactive 
        try:
            user_id = await token_user(self.scope)
            await status(user_id, flag='disconnect')
        except:
            pass
        

    # Receive message from WebSocket
    async def receive(self, text_data):
        user_id = await token_user(self.scope)

        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        conversation_id = self.room_name
        
        # Save message to database
        await send_msg(user_id, message, conversation_id)
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            # chat_message sends message to socket
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        conversation_id = self.room_name

        # Send message to WebSocket        
        await self.send(text_data=json.dumps({
            'message': message
        }))
