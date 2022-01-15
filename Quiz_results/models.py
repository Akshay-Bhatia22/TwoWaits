from django.db import models

from Accounts.models import UserAccount 
from Quiz.models import Quiz, QuizQuestion, Option

class QuizResult(models.Model):
    student_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='quiz_student')
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='attempted_quiz')
    
    def __str__(self):
        return 'student'+ str(self.student_id)+ 'attempted quiz ' + str(self.quiz_id)
    
    @property
    def quiz_result_id(self):
        return self.id

class StudentAnswer(models.Model):
    quiz_result_id = models.ForeignKey(QuizResult, on_delete=models.CASCADE, related_name='student_quiz_result_id')
    question_id = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='attempted_question')

    def __str__(self):
        return str(self.question_id)

    @property
    def student_answer_id(self):
        return self.id

class StudentResponse(models.Model):
    answer_id = models.ForeignKey(StudentAnswer, on_delete=models.CASCADE, related_name='marked_answer')
    option_id = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='marked_option')

    def __str__(self):
        return str(self.answer_id)

    @property
    def response_id(self):
        return self.id