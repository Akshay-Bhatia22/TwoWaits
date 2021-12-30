from rest_framework import status, generics
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

# ---------Models--------
from Faculty.models import Faculty
from Student.models import Student


# ---------Serializers--------
from .serializers import FacultyProfileSerializer, StudentProfileSerializer


class UserTypeHelper:

    def __init__(self, request):
        self.request = request
        if 'student' in self.request.get_full_path():
            self.user_type = 'S'

        if 'faculty' in request.get_full_path():
            self.user_type = 'F'

    def get_specific_user_by_id(self):
        if self.user_type == 'F':
            return Faculty.objects.get(faculty_account_id=self.request.user.id)
        if self.user_type == 'S':
            return Student.objects.get(student_account_id=self.request.user.id)

    def user_serializer(self, data):
        if self.user_type == 'F':
            return FacultyProfileSerializer(data, many=False)
        if self.user_type == 'S':
            return StudentProfileSerializer(data, many=False)

    def get_user_account_id(self):
        if self.user_type == 'F':
            return 'faculty_account_id'
        if self.user_type == 'S':
            return 'student_account_id'

    def user_type_exists(self):
        if self.user_type == 'F':
            return Faculty.objects.filter(faculty_account_id=self.request.user.id).exists()
        if self.user_type == 'S':
            return Student.objects.filter(student_account_id=self.request.user.id).exists()


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
