from django.contrib import admin

from .models import File, Note

admin.site.register(Note)
admin.site.register(File)
