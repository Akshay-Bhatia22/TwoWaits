from django.urls import path

from . import views

# CUD Create Update Delete
urlpatterns = [
    # Create
    path('add/', views.LectureCreateView.as_view()),

    # # Update/delete
    path('<int:pk>/', views.LectureCreateView.as_view()),

    path('view/', views.LectureView.as_view()),
    path('your-lectures/', views.LectureCreateView.as_view()),

    path('wishlist/', views.WishlistAdd.as_view()),
    path('your-wishlist/', views.YourWishlist.as_view()),
]
