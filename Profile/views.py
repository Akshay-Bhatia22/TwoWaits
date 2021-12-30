from rest_framework import status, generics
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

# ---------Models--------
from Faculty.models import Faculty
import Profile

# ---------Serializers--------
from .serializers import FacultyProfileSerializer
from Profile import serializers


def user_url(request):
    if 'student' in request.get_full_path():
        return 'S'
    if 'faculty' in request.get_full_path():
        return 'F'


def get_specific_user_by_id(request, user_type):
    if user_type == 'F':
        return Faculty.objects.get(faculty_account_id=request.user.id)
    if user_type == 'S':
        pass


def user_serializer(data, user_type):
    if user_type == 'F':
        return FacultyProfileSerializer(data, many=False)
    if user_type == 'S':
        pass


def get_user_account_id(user_type):
    if user_type == 'F':
        return 'faculty_account_id'
    if user_type == 'S':
        pass

def user_type_exists(request, user_type):
    if user_type == 'F':
        return Faculty.objects.filter(faculty_account_id=request.user.id).exists()
    if user_type == 'S':
        pass
# FACULTY


class ProfileView(APIView):

    permission_classes = [IsAuthenticated, ]

    def get(self, request, format=None):
        user_type = user_url(request)
        try:
            data = get_specific_user_by_id(request, user_type)
            # data = Faculty.objects.get(faculty_account_id=request.user.id)
            serializer = user_serializer(data, user_type)
            # serializer = FacultyProfileSerializer(data, many=False)
            return Response(serializer.data)
        except:
            return Response({'message': 'User not found'}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, format=None):
        data = request.data
        user_type = user_url(request)
        data[get_user_account_id(user_type)] = request.user.id
        # if Faculty.objects.filter(faculty_account_id=request.user.id).exists():
        if user_type_exists(request, user_type):
            return Response(data={'message': 'Profile already exists use PUT instead'}, status=status.HTTP_400_BAD_REQUEST)
        if user_type == 'F':
            serializer = FacultyProfileSerializer(data=data)
        if user_type == 'S':
            pass
        
        # serializer = user_serializer(data, user_type)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(data={'message': 'Invalid data entered'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        data = request.data
        user_type = user_url(request)

        data[get_user_account_id(user_type)] = request.user.id
        try:
            profile = get_specific_user_by_id(request, user_type)
        except:
            return Response({'message': 'Profile not found'}, status=status.HTTP_403_FORBIDDEN)
        if user_type == 'F':
            serializer = FacultyProfileSerializer(instance=profile, data=data)
        if user_type == 'S':
            pass
        # serializer = FacultyProfileSerializer(instance=profile, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message': 'Invalid data entered'}, status=status.HTTP_400_BAD_REQUEST)
