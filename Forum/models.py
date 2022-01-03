from django.db import models
from django.utils import timezone

from Accounts.models import UserAccount

class Question(models.Model):
    # User account id which will be used to access student/faculty name and profile pic
    # CHANGE TO PROTECT or SET DEFAULT
    author_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='question')
    question = models.CharField(max_length=150)
    raised = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question

class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    author_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='answer_author')
    answer = models.CharField(max_length=150)
    answered = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.answer
        
class Comment(models.Model):
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='comment')
    author_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='comment_author')
    comment = models.CharField(max_length=150)
    commented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment