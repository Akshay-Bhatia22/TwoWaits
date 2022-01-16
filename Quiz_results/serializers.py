from django.db.models import fields
from rest_framework.serializers import ModelSerializer, Serializer, CharField

from Faculty.models import Faculty
import Quiz
from Student.models import Student
from Accounts.models import UserAccount

from .models import QuizResult, ScoreCard
from Quiz.serializers import QuizQuestionSerializer, AuthorSerializer, OptionSerializer
from Quiz.models import Quiz, QuizQuestion


class QuizResultSerializer(ModelSerializer):
    class Meta:
        model = QuizResult
        fields = ['quiz_result_id', 'student_id', 'quiz_id']

# FOR FULL QUIZ DATA FOR STUDENT (Correct options hidden)  
class QuizQuestionSerializer(ModelSerializer):
    option = OptionSerializer(many=True)

    class Meta:
        model = QuizQuestion
        fields = ['quiz_question_id', 'question_text', 'option']


class QuizStudentDataSerializer(ModelSerializer):
    question = QuizQuestionSerializer(many=True)
    author_id = AuthorSerializer()

    class Meta:
        model = Quiz
        fields = ['quiz_id', 'author_id', 'title', 'description', 'no_of_question', 'time_limit', 'question']

class ScoreCardSerializer(ModelSerializer):
    class Meta:
        model = ScoreCard
        fields = '__all__'