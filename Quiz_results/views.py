from django.http.response import Http404
from rest_framework import mixins, status, generics
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from Quiz_results.models import QuizResult

# ---------Serializers--------
from .serializers import QuizResultSerializer
from Profile.UserHelpers import UserTypeHelper
# from .models import 

from django.db.models import Prefetch


class AttemptQuiz(generics.CreateAPIView, generics.GenericAPIView):

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
