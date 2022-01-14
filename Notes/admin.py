from django.contrib import admin

from .models import BookmarkNotes, File, Note

admin.site.register(Note)
admin.site.register(File)
admin.site.register(BookmarkNotes)
