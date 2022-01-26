from django.forms import fields
from rest_framework.serializers import ModelSerializer

from Accounts.models import UserAccount

from .models import Contact, Message, Conversation

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['contact_id', 'status', 'contact_name', 'contact_dp'] 

class MessageSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = ['msg_contact', 'content', 'time']

class ConversationSerializer(ModelSerializer):
    conv_message = MessageSerializer(many=True)
    participants = ContactSerializer(many=True)
    
    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'name', 'conv_message']
