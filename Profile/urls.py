from django.urls import path

from . import views


urlpatterns = [
    path('faculty/', views.ProfileView.as_view()),
    path('student/', views.ProfileView.as_view()),
]
