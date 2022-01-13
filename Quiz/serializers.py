from django.db.models import fields
from rest_framework.serializers import ModelSerializer, Serializer, CharField

from Faculty.models import Faculty
from Student.models import Student
from Accounts.models import UserAccount

from .models import CorrectOption, Option, Quiz, QuizQuestion

class FacultyAuthorSerializer(ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['name', 'profile_pic']

class AuthorSerializer(ModelSerializer):
    faculty = FacultyAuthorSerializer()

    class Meta:
        model = UserAccount
        fields = ['faculty']

class CorrectOptionSerializer(ModelSerializer):
    # correct_option_text = CharField(max_length=80)

    class Meta:
        model = CorrectOption
        # fields = ['question_id', 'correct', 'correct_option_text']
        fields = ['question_id', 'correct']
    
    # def to_representation(self, instance):
    #     data = super(CorrectOptionSerializer, self).to_representation(instance)
    #     quiz = QuizQuestion.objects.get(id=data['question_id'])
        
    #     data['correct_option_text'] = Option.objects.filter(question_id=quiz).get(id=data['correct'])
    #     print(quiz)
    #     # print(option)
    #     # print(data['correct_option_text'])
    #     return data

class OptionSerializer(ModelSerializer):
    # correct_option = CorrectOptionSerializer(many=True)

    class Meta:
        model = Option
        fields = ['option_id','option']

class QuizQuestionSerializer(ModelSerializer):
    option = OptionSerializer(many=True)
    correct = CorrectOptionSerializer(many=True)
    class Meta:
        model = QuizQuestion
        fields = ['quiz_question_id', 'question_text', 'option', 'correct']

# FOR FULL QUIZ VIEW  
class QuizFacultySerializer(ModelSerializer):
    question = QuizQuestionSerializer(many=True)
    author_id = AuthorSerializer()

    class Meta:
        model = Quiz
        fields = ['quiz_id', 'author_id', 'title', 'description', 'no_of_question', 'time_limit', 'question']



class QuizFacultyCreateSerializer(ModelSerializer):

    class Meta:
        model = Quiz
        fields = ['quiz_id', 'author_id', 'title', 'description', 'no_of_question', 'time_limit']
