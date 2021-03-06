from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

from Accounts.models import UserAccount


class Note(models.Model):
    # User account id which will be used to access student/faculty name and profile pic
    # CHANGE TO PROTECT or SET DEFAULT
    author_id = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name='note')
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    file_obj_firebase = models.CharField(max_length=300, blank=True, null=True)
    
    uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    @property
    def note_id(self):
        return self.id
    
    class Meta:
        ordering = ['-uploaded']


class File(models.Model):
    note_id = models.ForeignKey(
        Note, on_delete=models.CASCADE, related_name='note_file')
    file_obj = models.FileField(upload_to = 'Note_files', blank=True, null=True)
    file_obj_firebase = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.file_obj).split('/')[2]

    @property
    def file_id(self):
        return self.id

class BookmarkNotes(models.Model):
    user_id = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name='user_note')
    note_id = models.ForeignKey(
        Note, on_delete=models.CASCADE, related_name='bookmark_note_id')
    
    def __str__(self):
        return str(self.note_id)