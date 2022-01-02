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
