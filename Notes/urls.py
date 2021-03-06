from django.urls import path

from . import views

# CUD Create Update Delete
urlpatterns = [
    # Create
    path('', views.NoteCreate.as_view()),
    # Update/delete
    path('<int:pk>/', views.NoteCreate.as_view()),
    # path('view/', views.NoteViewset.as_view()),
    path('view/', views.NoteView.as_view()),

    path('file/', views.FileAdd.as_view()),

    path('bookmark/', views.BookmarkNotesAdd.as_view()),
    path('your-bookmarked/', views.YourBookmarkedNotes.as_view()),
]
