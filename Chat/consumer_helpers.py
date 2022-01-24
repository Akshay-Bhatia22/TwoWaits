import jwt
from Project_TwoWaits.settings import SIMPLE_JWT, SECRET_KEY
from rest_framework.exceptions import ValidationError, AuthenticationFailed

from channels.db import database_sync_to_async

from Accounts.models import UserAccount
from .models import Contact, Conversation, Message

@database_sync_to_async
def token_userid_helper(decoded):
# get user from database
    usr = UserAccount.objects.get(id=decoded)
    return usr.id

@database_sync_to_async
def send_msg(user_id, message, conversation_id):
    try:
        contact_instance = UserAccount.objects.get(id = user_id).contact.first()
    except:
        return "create contact first"
    try:
        conversation_instance = Conversation.objects.get(id = conversation_id)
    except:
        return "conversation not started"

    try:
        msg = Message.objects.create(
            conversation_id=conversation_instance,
            msg_contact = contact_instance,
            content = message)
        return msg
    except:
        return 'fail'

@database_sync_to_async
def status(user_id, flag):
    try:
        c = Contact.objects.get(user = user_id)
        print('got user')
        try:
            if flag=='connect':
                c.status=1
            elif flag=='disconnect':
                c.status=0
            c.save()
            print(f'status changed {user_id}')
        except:
            pass
    except:
        pass

def token_user(scope):
    # extract token 
    headers = scope['headers']
    # extract user_id
    token = ''
    for header in headers:
        if header[0] == b'authorization':
            token = header[1]
            break
    if token:
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=[SIMPLE_JWT['ALGORITHM']]).get(SIMPLE_JWT['USER_ID_CLAIM'])
            user = token_userid_helper(decoded)
            return user
        
        except jwt.ExpiredSignatureError:
            # set to raise for json response
            return ValidationError({"error": ["Token has Expired"]})

        except jwt.exceptions.DecodeError:
            return AuthenticationFailed('Invalid Token')
    return 'Token not supplied'
    
    

