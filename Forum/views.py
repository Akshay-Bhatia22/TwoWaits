from rest_framework import status, generics
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

# ---------Serializers--------
from .serializers import QuestionSerializer

from Profile.UserHelpers import UserTypeHelper
from .models import Question

from django.db.models import Prefetch

class ForumView(APIView):

    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        data = Question.objects.all().prefetch_related(Prefetch('answer', to_attr='answers_list'))
        serializer = QuestionSerializer(data, many=True)
        return Response(serializer.data)        
