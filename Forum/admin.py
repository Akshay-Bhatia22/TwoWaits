from django.contrib import admin

from .models import Answer, Comment, Question

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
