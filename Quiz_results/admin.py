from django.contrib import admin

from .models import QuizResult, Response, StudentAnswer

# Register your models here.
admin.site.register(QuizResult)
admin.site.register(StudentAnswer)
admin.site.register(Response)
