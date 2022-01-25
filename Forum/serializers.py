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
        fields = ['name', 'gender', 'profile_pic', 'profile_pic_firebase']


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
    

    def to_representation(self, instance):
        data = super(CommentSerializer, self).to_representation(instance)
        comment_id = data['comment_id']
        request=self.context.get("request")
        user = request.user.id

        obj=Comment.objects.filter(author_id=user).filter(id=comment_id)
        print(obj)
        if obj:
            # bookmarked  by current user
            data['commented_by_user'] = 'True'
        else:
            # not bookmarked by current answer
            data['commented_by_user'] = 'False'
        return data


class AnswerSerializer(ModelSerializer):
    comment = CommentSerializer(many=True)
    author_id = AuthorSerializer()

    class Meta:
        model = Answer
        fields = ['answer_id', 'author_id', 'answer', 'answered', 'comment']

    def to_representation(self, instance):
        data = super(AnswerSerializer, self).to_representation(instance)
        data['likes'] = LikeAnswer.objects.filter(
            answer_id=data['answer_id']).filter(like=1).count()
        
        request=self.context.get("request")
        user = request.user.id
        obj=LikeAnswer.objects.filter(answer_id=data['answer_id']).filter(author_id=user)
        if obj:
            if obj[0].like:
                # like registered by current user
                data['liked_by_user'] = 'True'
            else:
                data['liked_by_user'] = 'False'
        else:
            # like not registered on current answer
            data['liked_by_user'] = 'False'

        return data


class QuestionSerializer(ModelSerializer):
    answer = AnswerSerializer(many=True)
    author_id = AuthorSerializer()

    class Meta:
        model = Question
        fields = ['question_id', 'author_id', 'question', 'raised', 'answer',]

    def to_representation(self, instance):
        data = super(QuestionSerializer, self).to_representation(instance)
        question_id = data['question_id']
        request=self.context.get("request")
        user = request.user.id

        obj=BookmarkQuestion.objects.filter(user_id=user).filter(question_id=question_id)
        print(obj)
        if obj:
            # bookmarked  by current user
            data['bookmarked_by_user'] = 'True'
        else:
            # not bookmarked by current answer
            data['bookmarked_by_user'] = 'False'
        return data
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