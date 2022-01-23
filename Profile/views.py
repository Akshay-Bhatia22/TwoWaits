from django.http import response
from rest_framework import status, generics
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from Faculty.models import Faculty
from Student.models import Student

# ---------Serializers--------
from .serializers import FacultyProfileSerializer, StudentProfileSerializer, FacultyProfileGenericSerializer, StudentProfileGenericSerializer

from Profile.UserHelpers import UserTypeHelper
from Accounts.models import UserAccount

from Profile import serializers

class ProfileView(APIView):

    permission_classes = [IsAuthenticated, ]

    def get(self, request, format=None):
        helper = UserTypeHelper(request, path=False)
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


# ------------------------------------------------TESTING REQUIRED-----------------------------------------------------------------------------
# ----------------filter(on college name)

# from itertools import chain 
# combined_list = list(chain(q1,q2))


class RelatedFacultyProfile(generics.ListAPIView):
    serializer_class = FacultyProfileGenericSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        helper = UserTypeHelper(self.request, path=False)
        if helper.user_type == 'F':
            queryset = Faculty.objects.filter(department=self.request.user.faculty.department)
        if helper.user_type == 'S':
            queryset = Faculty.objects.filter(department=self.request.user.student.branch)        
        return queryset


class RelatedStudentProfile(generics.ListAPIView):
    serializer_class = StudentProfileGenericSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        helper = UserTypeHelper(self.request, path=False)
        if helper.user_type == 'F':
            queryset = Student.objects.filter(branch=self.request.user.faculty.department)
        if helper.user_type == 'S':
            queryset = Student.objects.filter(branch=self.request.user.student.branch)        
        return queryset

class RelatedPeopleProfile(APIView):

    def get(self, request, format=None):
        # helper = UserTypeHelper(self.request, path=False)
        # print(helper.user_type)
        # if helper.user_type == 'F':
        #     queryset = Student.objects.filter(branch=self.request.user.faculty.department)
        #     print(queryset)
        #     serializer = StudentProfileGenericSerializer(queryset)
        #     print(serializer.data)

        return Response({'message':'testing'})
# ----------------------------------------------------------------------------------------------------------------------------------