from django.contrib import admin

# Register your models here.
from .models import Contact, Conversation, Friend, Message

admin.site.register(Contact)
admin.site.register(Conversation)
admin.site.register(Friend)
admin.site.register(Message)
