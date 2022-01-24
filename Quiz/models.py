from django.db import models
from django.db.models.fields import related

from Accounts.models import UserAccount 

class Quiz(models.Model):
    author_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='quiz_faculty')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True, null=True)
    no_of_question = models.IntegerField()
    time_limit = models.IntegerField(blank=True, null=True)
    banner_firebase = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    @property
    def quiz_id(self):
        return self.id

class QuizQuestion(models.Model):
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='question')
    question_text = models.CharField(max_length=150)

    def __str__(self):
        # return self.question_text, self.option, self.correct
        return self.question_text

    @property
    def quiz_question_id(self):
        return self.id


# to enable multiple options 
class Option(models.Model):
    question_id = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='option')
    option = models.CharField(max_length=80)

    def __str__(self):
        return self.option
    
    @property
    def option_id(self):
        return self.id

    
# for multi correct answers
class CorrectOption(models.Model):
    question_id = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='correct')
    correct  = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='correct_option')
    # correct_option_text = models.CharField(max_length=80, default='null')
    def __str__(self):
        return str(self.correct)

