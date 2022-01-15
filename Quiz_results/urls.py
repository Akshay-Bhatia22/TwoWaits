from django.urls import path

from . import views

# CUD Create Update Delete
urlpatterns = [
    path('attempt/', views.AttemptQuiz.as_view()),
    path('answer/', views.AnswerQuizQuestion.as_view()),
    # path('submit/', views.GenerateResult.as_view()),
]
