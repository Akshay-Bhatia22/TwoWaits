from pyexpat import model
from rest_framework.serializers import ModelSerializer
from Accounts.models import UserAccount

from Faculty.models import Faculty
from Student.models import Student

class UserAccountSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id']


class FacultyProfileSerializer(ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['faculty_account_id', 'name', 'department','college', 'gender','dob', 'profile_pic']


class StudentProfileSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_account_id', 'name', 'college',
                  'course', 'branch', 'year', 'gender','dob', 'profile_pic', 'profile_pic_firebase']

class FacultyProfileGenericSerializer(ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class StudentProfileGenericSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'