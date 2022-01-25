from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

from Accounts.models import UserAccount


class Feedback(models.Model):
    RATING = ((1, 'Poor'),
              (2, 'Average'),
              (3, 'Good'),
              (4, 'Excellent'),
              (5, 'Exceptional'))
    author_id = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name='feedback')
    rating = models.IntegerField(choices=RATING)
    message = models.CharField(max_length=150)

    recorded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (self.author_id.email).split('@')[0] + ' rated '+ str(self.rating)

    @property
    def feedback_id(self):
        return self.id
