from django.http.response import Http404
from rest_framework import status, generics
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

# ---------Serializers--------
from .serializers import QuizFacultySerializer

from Profile.UserHelpers import UserTypeHelper
from .models import Quiz

from django.db.models import Prefetch

from Forum import serializers


class QuizView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizFacultySerializer
    permission_classes = [AllowAny]