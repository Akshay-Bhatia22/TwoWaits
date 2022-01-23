from django.contrib import admin

from .models import Answer, BookmarkQuestion, Comment, Question, LikeAnswer

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(LikeAnswer)
admin.site.register(BookmarkQuestion)



