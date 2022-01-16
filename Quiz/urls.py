from django.urls import path

from . import views

# CUD Create Update Delete
urlpatterns = [
    # FOR create
    path('', views.QuizMain.as_view()),
    # For Update/delete
    path('<int:pk>/', views.QuizMain.as_view()),

    path('question/', views.QuizQuestionCreate.as_view()),
    path('question/correct/', views.QuizCorrectOption.as_view()),
    path('full-view/', views.CreatedQuizView.as_view()),

    path('my-quizzes/', views.MyCreatedQuizzes.as_view()),

    path('testing/', views.QuizView.as_view()),

]
