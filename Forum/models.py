from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

from Accounts.models import UserAccount


class Question(models.Model):
    # User account id which will be used to access student/faculty name and profile pic
    # CHANGE TO PROTECT or SET DEFAULT
    author_id = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name='question')
    question = models.CharField(max_length=150)
    raised = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question

    @property
    def question_id(self):
        return self.id
    
    class Meta:
        ordering = ['-raised']


class Answer(models.Model):
    question_id = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answer')
    author_id = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name='answer_author')
    answer = models.CharField(max_length=150)
    answered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.answer

    @property
    def answer_id(self):
        return self.id

    # class Meta:
    #     ordering = ['-likes']


class Comment(models.Model):
    answer_id = models.ForeignKey(
        Answer, on_delete=models.CASCADE, related_name='comment')
    author_id = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name='comment_author')
    comment = models.CharField(max_length=150)
    commented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment

    @property
    def comment_id(self):
        return self.id

    class Meta:
        ordering = ['-commented']

class LikeAnswer(models.Model):
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='like')
    author_id = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name='like_author')
    likes = models.IntegerField(default=0)

class BookmarkQuestion(models.Model):
    user_id = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name='user_bookmark_question')
    question_id = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='bookmark_question_id')
    
    def __str__(self):
        return str(self.question_id)