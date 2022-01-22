from rest_framework.serializers import ModelSerializer

from Faculty.models import Faculty
from Student.models import Student
from Accounts.models import UserAccount

from .models import BookmarkQuestion, LikeAnswer, Question, Answer, Comment


class StudentAuthorSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'profile_pic', 'profile_pic_firebase']


class FacultyAuthorSerializer(ModelSerializer):
    class Meta:
        model = Faculty
        # Gender so that sir/ma'am can be appended to the name
        fields = ['name', 'gender', 'profile_pic']


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
        fields = ['answer_id', 'author_id', 'answer', 'answered', 'comment']

    def to_representation(self, instance):
        data = super(AnswerSerializer, self).to_representation(instance)
        data['likes'] = LikeAnswer.objects.filter(
            answer_id=data['answer_id']).filter(likes=1).count()

        return data


class QuestionSerializer(ModelSerializer):
    answer = AnswerSerializer(many=True)
    author_id = AuthorSerializer()

    class Meta:
        model = Question
        fields = ['question_id', 'author_id', 'question', 'raised', 'answer', ]

# Exculdes nested serializers


class QuestionGenericSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerGenericSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class CommentGenericSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikeAnswerSerializer(ModelSerializer):
    class Meta:
        model = LikeAnswer
        fields = '__all__'

class BookmarkQuestionsSerializer(ModelSerializer):
    class Meta:
        model = BookmarkQuestion
        fields = '__all__'