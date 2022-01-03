from rest_framework.serializers import ModelSerializer

from Faculty.models import Faculty
from Student.models import Student
from Accounts.models import UserAccount

from .models import Question, Answer, Comment


class StudentAuthorSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'profile_pic']


class FacultyAuthorSerializer(ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['name', 'profile_pic']


class AuthorSerializer(ModelSerializer):
    student = StudentAuthorSerializer()
    faculty = FacultyAuthorSerializer()

    class Meta:
        model = UserAccount
        fields = ['student', 'faculty']


class CommentSerializer(ModelSerializer):
    author_id = AuthorSerializer()
    
    class Meta:
        model = Comment
        fields = ['comment_id', 'author_id', 'comment', 'commented']


class AnswerSerializer(ModelSerializer):
    comment = CommentSerializer(many=True)
    author_id = AuthorSerializer()

    class Meta:
        model = Answer
        fields = ['answer_id', 'author_id', 'answer', 'likes', 'answered', 'comment']


class QuestionSerializer(ModelSerializer):
    answer = AnswerSerializer(many=True)
    author_id = AuthorSerializer()

    class Meta:
        model = Question
        fields = ['question_id', 'author_id', 'question', 'raised', 'answer', ]
