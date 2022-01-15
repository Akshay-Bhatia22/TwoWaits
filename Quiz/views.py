from django.http.response import Http404
from rest_framework import mixins, status, generics
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

# ---------Serializers--------
from .serializers import QuizFacultySerializer, QuizFacultyCreateSerializer, QuizQuestionSerializer

from Profile.UserHelpers import UserTypeHelper
from .models import CorrectOption, Option, Quiz, QuizQuestion

from django.db.models import Prefetch




def override_request(request):
    data = request.data
    data['author_id'] = request.user.id
    # return data

# For testing
class QuizView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizFacultySerializer
    permission_classes = [AllowAny]

class QuizMain(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, generics.GenericAPIView):

    serializer_class = QuizFacultyCreateSerializer
    permission_classes = [IsAuthenticated]
    # so that users can only update/delete their quizzes
    # queryset = Quiz.objects.filter(author_id=request)
    def get_queryset(self):
        return Quiz.objects.filter(author_id=self.request.user.id) 

    def post(self, request, *args, **kwargs):
        override_request(request)
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        override_request(request)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        override_request(request)
        return self.destroy(request, *args, **kwargs)

class QuizQuestionCreate(APIView):
    permission_classes = [IsAuthenticated]


    def post(self, request, format=None):
        data = request.data
        try:
            quiz_instance = Quiz.objects.get(id=data['quiz_id'])
        except:
            return Response({'message':'Quiz object not found'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            quiz_question_instance = QuizQuestion.objects.create(quiz_id=quiz_instance, question_text=data['question_text'])
            if data['options']:
                for option in data['options']:
                    Option.objects.create(question_id=quiz_question_instance, option=option['option'])
                serializer = QuizFacultySerializer(instance=quiz_instance)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                # return Response({'message':'ok'})
        except:
            return Response({'message':'Invalid data entered'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                
class QuizCorrectOption(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        data = request.data
        try:
            quiz_question_instance = QuizQuestion.objects.get(id=data['question_id'])
            if data['correct_options']:
                for option in data['correct_options']:
                    option_instance = Option.objects.get(id=option['option_id'])
                    CorrectOption.objects.create(question_id=quiz_question_instance, correct=option_instance)
                return Response({'message':'ok'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'message':'Invalid data entered'}, status=status.HTTP_406_NOT_ACCEPTABLE)

class CreatedQuizView(APIView):
    def get(self, request, format=None):
        data=request.data
        quiz = Quiz.objects.get(id=data['quiz_id'])
        serializer = QuizFacultySerializer(instance=quiz)
        return Response(serializer.data)

class MyCreatedQuizzes(APIView):
    def get(self, request, format=None):
        quiz = Quiz.objects.filter(author_id=self.request.user.id)
        serializer = QuizFacultySerializer(instance=quiz, many=True)
        return Response(serializer.data)

# class QuizCreate(APIView):

#     def post(self, request, format=None):
#         data = override_request(request)
#         serializer = QuizFacultyCreateSerializer(data=data)
#         if serializer.is_valid():
#             quiz = serializer.save()
#             questions = [question for question in data['question']]
#             for i in questions:
#                 question_text = i['question_text']
#                 quiz_question = QuizQuestion.objects.create(quiz_id=quiz, question_text=question_text)
#                 for j in i['option']:
#                     print(j)
#                     option = Option.objects.create(question_id=quiz_question, option=j['option'])
#                 print('\n')
#                 # for k in i['correct']:
#                 #     correct = CorrectOption.objects.create(question_id=quiz_question, correct=k['correct'])

#         # ques = [Question(quiz_id=quiz, question_text=question['']) for photo in photos]
#         # Image.objects.bulk_create(img)
#             return Response(serializer.data)
#         return Response({'message':'Error'})
        
#         # return check_save_serializer(serializer)