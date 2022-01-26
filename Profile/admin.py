from django.contrib import admin

from Forum.models import Question
from .models import Feedback

# Register your models here.
admin.site.register(Feedback)