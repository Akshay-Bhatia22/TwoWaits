from django.http.response import Http404
from rest_framework import status, generics
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

# ---------Serializers--------
from .serializers import QuestionSerializer, QuestionGenericSerializer, AnswerGenericSerializer, CommentGenericSerializer, LikeAnswerSerializer

from Profile.UserHelpers import UserTypeHelper
from .models import Answer, Comment, LikeAnswer, Question

from django.db.models import Prefetch

from Forum import serializers


def override_request(request):
    data = request.data
    data['author_id'] = request.user.id
    return data


def check_save_serializer(serializer):
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response({'message': 'Invalid data entered'}, status=status.HTTP_400_BAD_REQUEST)


class ForumView(generics.ListAPIView):
    queryset = Question.objects.all().prefetch_related(
        Prefetch('answer', to_attr='answers_list'))
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]
    

class YourQuestions(generics.ListAPIView):
    
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Question.objects.filter(author_id=self.request.user.id).prefetch_related(
        Prefetch('answer', to_attr='answers_list'))
        return queryset


class QuestionCUD(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = override_request(request)
        serializer = QuestionGenericSerializer(data=data)
        return check_save_serializer(serializer)

    def put(self, request, format=None):
        data = override_request(request)
        try:
            obj = Question.objects.get(id=data['question_id'])
            if obj.author_id.id == data['author_id']:
                serializer = QuestionGenericSerializer(instance=obj, data=data)
                return check_save_serializer(serializer)
            return Response({'message': 'You can edit only your question'}, status=status.HTTP_403_FORBIDDEN)
        except:
            return Response({'message': 'Question not found'})

    def delete(self, request, format=None):
        data = override_request(request)
        try:
            obj = Question.objects.get(id=data['question_id'])
            if obj.author_id.id == data['author_id']:
                obj.delete()
                return Response({'message': 'Question deleted'}, status=status.HTTP_403_FORBIDDEN)
            return Response({'message': 'You can edit only your question'}, status=status.HTTP_403_FORBIDDEN)
        except:
            return Response({'message': 'Question not found'})


class AnswerCUD(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = override_request(request)
        serializer = AnswerGenericSerializer(data=data)
        return check_save_serializer(serializer)

    def put(self, request, format=None):
        data = override_request(request)
        try:
            obj = Answer.objects.get(id=data['answer_id'])
            if obj.author_id.id == data['author_id']:
                serializer = AnswerGenericSerializer(instance=obj, data=data)
                return check_save_serializer(serializer)
            return Response({'message': 'You can edit only your answer'}, status=status.HTTP_403_FORBIDDEN)
        except:
            return Response({'message': 'Answer not found'})

    def delete(self, request, format=None):
        data = override_request(request)
        try:
            obj = Answer.objects.get(id=data['answer_id'])
            if obj.author_id.id == data['author_id']:
                obj.delete()
                return Response({'message': 'Answer deleted'}, status=status.HTTP_403_FORBIDDEN)
            return Response({'message': 'You can edit only your answer'}, status=status.HTTP_403_FORBIDDEN)
        except:
            return Response({'message': 'Answer not found'})


class CommentCUD(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = override_request(request)
        serializer = CommentGenericSerializer(data=data)
        return check_save_serializer(serializer)

    def put(self, request, format=None):
        data = override_request(request)
        try:
            obj = Comment.objects.get(id=data['comment_id'])
            if obj.author_id.id == data['author_id']:
                serializer = CommentGenericSerializer(instance=obj, data=data)
                return check_save_serializer(serializer)
            return Response({'message': 'You can edit only your comment'}, status=status.HTTP_403_FORBIDDEN)
        except:
            return Response({'message': 'Comment not found'})

    def delete(self, request, format=None):
        data = override_request(request)
        try:
            obj = Comment.objects.get(id=data['comment_id'])
            if obj.author_id.id == data['author_id']:
                obj.delete()
                return Response({'message': 'Comment deleted'}, status=status.HTTP_403_FORBIDDEN)
            return Response({'message': 'You can edit only your comment'}, status=status.HTTP_403_FORBIDDEN)
        except:
            return Response({'message': 'Comment not found'})

class LikeUnlikeAnswer(APIView):

    def post(self, request, format=None):
        data = override_request(request)
        try:
            obj = LikeAnswer.objects.filter(author_id=data['author_id']).filter(answer_id=data['answer_id'])
            # if queryset not empty i.e user has already registered a like
            if obj:
                obj = obj[0]
                if obj.likes == 1:
                    data['likes'] = 0

                elif obj.likes == 0:
                    data['likes'] = 1                

                serializer = LikeAnswerSerializer(instance=obj, data=data)
                return check_save_serializer(serializer)

            else:
                data['likes'] = 1
                serializer = LikeAnswerSerializer(data=data)
                return check_save_serializer(serializer)
        except:
            return Response({'message':'Error maybe answer doesn\'t exist'}, status=status.HTTP_400_BAD_REQUEST)

# class QuestionCreate(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Question.objects.all().prefetch_related(Prefetch('answer', to_attr='answers_list'))
#     serializer_class = QuestionSerializer
#     permission_classes = [IsAuthenticated]
#     # lookup_field = 'id'

#     def get_queryset(self):
#         return self.queryset.filter(author_id=self.request.user)
