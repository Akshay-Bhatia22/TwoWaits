from django.urls import path

from . import views

# CUD Create Update Delete
urlpatterns = [
    path('', views.QuizView.as_view()),

]
