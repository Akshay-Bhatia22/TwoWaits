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

        elif 'faculty' in request.get_full_path():
            self.user_type = 'F'

        else:
            if hasattr(self.request.user, 'student'):
                print("STUDENT via get or put")
                self.user_type = 'S'
            elif hasattr(self.request.user, 'faculty'):
                self.user_type = 'F'
                print("FACULTY via get or put")



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
