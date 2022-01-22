from django.urls import path

from . import views

# CUD Create Update Delete
urlpatterns = [
    path('', views.ForumView.as_view()),
    path('question/', views.QuestionCUD.as_view()),
    path('answer/', views.AnswerCUD.as_view()),
    path('answer/like-unlike/', views.LikeUnlikeAnswer.as_view()),
    path('comment/', views.CommentCUD.as_view()),
    path('your-questions/', views.YourQuestions.as_view()),
    # add/remove bookmark on question
    # your bookmarked questions
    path('bookmark/', views.BookmarkQuestionAdd.as_view()),
    path('your-bookmarked/', views.YourBookmarkedQuestions.as_view()),
]
