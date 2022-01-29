from django.db import models
from django.utils import timezone

from Accounts.models import UserAccount


class Lecture(models.Model):
    # User account id which will be used to access student/faculty name and profile pic
    # CHANGE TO PROTECT or SET DEFAULT
    author_id = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name='lecture')
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    video_firebase = models.CharField(max_length=300, blank=True, null=True)
    
    uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    @property
    def lecture_id(self):
        return self.id
    
    class Meta:
        ordering = ['-uploaded']

class Wishlist(models.Model):
    user_id = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name='user_wishlist')
    lecture_id = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, related_name='wishlist_lecture_id')
    
    def __str__(self):
        return str(self.lecture_id)