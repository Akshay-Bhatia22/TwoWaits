from django.urls import path

from . import views

urlpatterns = [
    path('get-contacts/', views.ContactsView.as_view()),
    path('message-add-to-conversation/', views.AddToConversation.as_view()),
    path('conversation/', views.ConversationView.as_view()),
    # path('toggle-chat/', views.ToggleChat.as_view()),
    # path('check-contact/', views.CheckContact.as_view()),
]
