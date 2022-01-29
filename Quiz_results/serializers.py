from django.db.models import fields
from rest_framework.serializers import ModelSerializer, Serializer, CharField

from Faculty.models import Faculty
import Quiz
from Student.models import Student
from Accounts.models import UserAccount

from .models import QuizResult, ScoreCard
from Quiz.serializers import CorrectOptionSerializer, QuizFacultySerializer, QuizQuestionSerializer, AuthorSerializer, OptionSerializer
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

# FULL QUIZ VIEW WITH USER ANSWERS
class QuizQuestionSerializer(ModelSerializer):
    option = OptionSerializer(many=True)
    correct = CorrectOptionSerializer(many=True)
    class Meta:
        model = QuizQuestion
        fields = ['quiz_question_id', 'question_text', 'option', 'correct']
    
    def to_representation(self, instance):
        data = super(QuizQuestionSerializer, self).to_representation(instance)
        request=self.context.get("request")
        user_id = request.user.id
        try:
            quiz_id = QuizQuestion.objects.get(id=data['quiz_question_id']).quiz_id.id
        except:
            data['user_option'] = 'Quiz not found' 
        q = QuizResult.objects.filter(student_id=user_id).filter(quiz_id=quiz_id)
        if q:
            try:  
                data['user_option'] = q[0].student_quiz_result_id.first().marked_answer.first().option_id.id
            except:
                data['user_option'] = 'null'
        else:
            data['user_option'] = 'Question not attempted'
        return data


class FullQuizResultSerializer(ModelSerializer):
    question = QuizQuestionSerializer(many=True)
    author_id = AuthorSerializer()

    class Meta:
        model = Quiz
        fields = ['quiz_id', 'author_id', 'title', 'description', 'no_of_question', 'time_limit', 'question']

