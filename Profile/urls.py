from django.urls import path

from . import views


urlpatterns = [
    # ---- for POST request--------
    path('faculty/', views.ProfileView.as_view()),
    path('student/', views.ProfileView.as_view()),
    # ---- for GET and PUT---------
    path('', views.ProfileView.as_view()),
    path('people-you-might-know/', views.RelatedPeopleProfile.as_view()),
    path('faculty-you-might-know/', views.RelatedFacultyProfile.as_view()),
    path('student-you-might-know/', views.RelatedStudentProfile.as_view()),
    
]
