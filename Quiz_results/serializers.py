from django.db.models import fields
from rest_framework.serializers import ModelSerializer, Serializer, CharField

from Faculty.models import Faculty
from Student.models import Student
from Accounts.models import UserAccount

from .models import QuizResult

class QuizResultSerializer(ModelSerializer):
    class Meta:
        model = QuizResult
        fields = ['quiz_result_id', 'student_id', 'quiz_id']

