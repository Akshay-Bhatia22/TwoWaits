from django.urls import path

from . import views

# CUD Create Update Delete
urlpatterns = [
    path('attempt/', views.AttemptQuiz.as_view()),

]
