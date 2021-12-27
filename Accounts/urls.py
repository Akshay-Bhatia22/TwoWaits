from django.urls import path

from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', views.NewAccount.as_view()),
    path('login/', views.LoginAccount.as_view()),
    path('otp-verify/', views.OtpVerify.as_view()),
    path('send-otp/', views.SendOTP.as_view()),
    path('forgot-reset/', views.ForgotResetPassword.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
