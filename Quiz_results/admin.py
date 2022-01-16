from django.contrib import admin

from .models import QuizResult, StudentResponse, StudentAnswer, ScoreCard

# Register your models here.
admin.site.register(QuizResult)
admin.site.register(StudentAnswer)
admin.site.register(StudentResponse)
admin.site.register(ScoreCard)

