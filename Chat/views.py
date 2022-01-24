from django.http.response import Http404
from rest_framework import mixins, status, generics
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

# ---------Serializers--------
from .serializers import ConversationSerializer, ContactSerializer

from .models import Conversation, Contact
from Accounts.models import UserAccount

# for fetching all conversations and messages
class ConversationView(generics.ListAPIView):
    serializer_class = ConversationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Conversation.objects.filter(participants__user=self.request.user.id)

class AddToConversation(APIView):
    
    # send contact id
    def post(self, request, format=None):
        data = request.data
        try:
            # if already exists
            try:
                user_contact_id = Contact.objects.get(user=request.user.id)
                c_user = Conversation.objects.filter(participants=user_contact_id)
                c_new = Conversation.objects.filter(participants=data['contact_id'])
                intersection = c_user & c_new
                return Response({'message':'Conversation already exists use this conversation id',
                                'conversation_id':intersection[0].id})
            # if conversation doesn't exist
            except:
                c = Conversation.objects.create()
                c.participants.add(Contact.objects.get(user=request.user.id))
                c.participants.add(Contact.objects.get(id=data['contact_id']))

                return Response({'message':'Conversation created use this conversation id',
                                'conversation_id': c.id})
        except:
            return Response({'message':'Either the user has no contact or given contact id doesn\'t exist'}, status=status.HTTP_400_BAD_REQUEST)


class ContactsView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

# class ToggleChat(APIView):
#     def post(self, request, format=None):
#         user = UserAccount.objects.get(id=request.user.id)
#         print(user)
#         flag = request.data['flag']
#         if flag==1:
#             try:
#                 print(request.user.id)
#                 c=Contact.objects.filter(user=request.user.id)
#                 print(c)
#                 return Response({'message':'Contact exists'}, status=status.HTTP_200_OK)
#             except:
#                 Contact.objects.create(user=user)
#                 return Response({'message':'Contact created'}, status=status.HTTP_201_CREATED)
#         elif flag==0:
#             # Reomve chat functionality
#             try:
#                 c = Contact.objects.get(user=request.user.id)
#                 c.delete()
#                 return Response({'message':'Contact deleted'}, status=status.HTTP_202_ACCEPTED)
#             except:
#                 return Response({'message':'Contact already deleted'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'message':'enter a flag 0 to delete 1 to create'}, status=status.HTTP_400_BAD_REQUEST)

