from rest_framework import status, generics
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

# ---------Serializers--------
from .serializers import FacultyProfileSerializer, StudentProfileSerializer

from Profile.UserHelpers import UserTypeHelper


class ProfileView(APIView):

    permission_classes = [IsAuthenticated, ]

    def get(self, request, format=None):
        helper = UserTypeHelper(request)
        try:
            data = helper.get_specific_user_by_id()
            serializer = helper.user_serializer(data)
            return Response(serializer.data)
        except:
            return Response({'message': 'User not found'}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, format=None):
        helper = UserTypeHelper(request)
        data = request.data
        data[helper.get_user_account_id()] = request.user.id
        if helper.user_type_exists():
            return Response(data={'message': 'Profile already exists use PUT instead'}, status=status.HTTP_400_BAD_REQUEST)
        if helper.user_type == 'F':
            serializer = FacultyProfileSerializer(data=data)
        if helper.user_type == 'S':
            serializer = StudentProfileSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(data={'message': 'Invalid data entered'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        helper = UserTypeHelper(request)
        data = request.data

        data[helper.get_user_account_id()] = request.user.id
        try:
            print(helper.get_specific_user_by_id())
            profile = helper.get_specific_user_by_id()
        except:
            return Response({'message': 'Profile not found'}, status=status.HTTP_403_FORBIDDEN)
        if helper.user_type == 'F':
            serializer = FacultyProfileSerializer(instance=profile, data=data)
        if helper.user_type == 'S':
            serializer = StudentProfileSerializer(instance=profile, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message': 'Invalid data entered'}, status=status.HTTP_400_BAD_REQUEST)
