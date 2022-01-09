from django.contrib import admin

from Forum.models import Question
from .models import Quiz, QuizQuestion, Option, CorrectOption

# Register your models here.
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(Option)
admin.site.register(CorrectOption)
