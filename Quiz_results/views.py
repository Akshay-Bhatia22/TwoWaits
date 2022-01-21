from django.http.response import Http404
from rest_framework import mixins, status, generics
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from Quiz.models import Quiz, Option, QuizQuestion

from Quiz_results.models import QuizResult, StudentAnswer, StudentResponse

# ---------Serializers--------
from .serializers import QuizResultSerializer, QuizStudentDataSerializer
from Profile.UserHelpers import UserTypeHelper
# from .models import 

from django.db.models import Prefetch

from .score_card import generate_result

class QuizStudentDataView(APIView):

    def post(self, request, format=None):
        data=request.data
        try:
            quiz = Quiz.objects.get(id=data['quiz_id'])
        except:
            return Response({'message':'Quiz not found. Invalid quiz id'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = QuizStudentDataSerializer(instance=quiz)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AttemptQuiz(generics.CreateAPIView):

    serializer_class = QuizResultSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        # a student can attempt a quiz only once
        obj = QuizResult.objects.filter(student_id=request.user.id).filter(quiz_id=data['quiz_id'])
        if obj:
            # quiz already attempted
            return Response({'message':'Quiz already attempted'}, status=status.HTTP_208_ALREADY_REPORTED)
        data['student_id'] = request.user.id
        return self.create(request, *args, **kwargs)

class AnswerQuizQuestion(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data
        # check if options provided as else no need to register response
        if data['options']:
            # Options provided registre response
            try:
                # getting instance for foreign relationships
                quiz_result_id = QuizResult.objects.get(id=data['quiz_result_id'])
                question_id = QuizQuestion.objects.get(id=data['question_id'])
                
                # checking if already answered
                student_answer_instance = StudentAnswer.objects.filter(quiz_result_id=quiz_result_id).filter(question_id=question_id).first()
                
                if not student_answer_instance:
                    # create new answer instance
                    student_answer_instance = StudentAnswer.objects.create(quiz_result_id=quiz_result_id, question_id=question_id)

            except:
                return Response({'message':'Invalid data entered. Either quiz or question doesn\'t exist'}, status=status.HTTP_400_BAD_REQUEST)
            
            

            # ------------------------------FOR SINGLE CORRECT OPTIONS-----------------------------------------------------
            for option in data['options']:

                # getting option isntance for foreign relationship
                try:
                    option_id = Option.objects.get(id=option['option_id'])
                except:
                    return Response({'message':'Invalid option_id entered'}, status=status.HTTP_406_NOT_ACCEPTABLE)

                obj = StudentResponse.objects.filter(answer_id=student_answer_instance).filter(option_id=option_id)
                
                if obj:
                    # updating existing response
                    obj.update(answer_id=student_answer_instance, option_id=option_id)
                    return Response({'message':'Response updated. Question attempted'}, status=status.HTTP_200_OK)

                # if new response made
                StudentResponse.objects.create(answer_id=student_answer_instance, option_id=option_id)
                return Response({'message':'New response registered. Question attempted'}, status=status.HTTP_201_CREATED)
        return Response({'message':'No options provided. Question not attempted'}, status=status.HTTP_204_NO_CONTENT)

class GenerateResult(APIView):
    
    def post(self, request, format=None):
        data = request.data
        response = generate_result(data['quiz_id'], request.user.id)
        return response