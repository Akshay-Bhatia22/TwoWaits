from django.urls import path

from . import views


urlpatterns = [
    # ---- for POST request--------
    path('faculty/', views.ProfileView.as_view()),
    path('student/', views.ProfileView.as_view()),
    # ---- for GET and PUT---------
    path('', views.ProfileView.as_view()),
]
