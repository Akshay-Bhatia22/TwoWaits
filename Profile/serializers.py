from rest_framework.serializers import ModelSerializer

from Faculty.models import Faculty
from Student.models import Student


class FacultyProfileSerializer(ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['faculty_account_id', 'name', 'department', 'profile_pic']


class StudentProfileSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_account_id', 'name', 'college',
                  'course', 'branch', 'year', 'interest', 'profile_pic', 'profile_pic_firebase']
