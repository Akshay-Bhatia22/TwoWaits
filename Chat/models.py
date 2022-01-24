from django.db import models

from Accounts.models import UserAccount 

from django.utils import timezone
from Faculty.models import Faculty
from Student.models import Student
class Contact(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='contact')
    status = models.BooleanField(default=0)
    
    def __str__(self):
        try:
            return str(self.user.faculty)
        except:
            return str(self.user.student)


    @property
    def contact_id(self):
        return self.id
    
    def contact_name(self):
        try:
            return Faculty.objects.get(id=self.id).name
        except:
            try:
                return Student.objects.get(id=self.id).name
            except:
                return 'Anonymous' 
    def contact_dp(self):
        try:
            return str(Faculty.objects.get(id=self.id).profile_pic)
        except:
            try:
                return str(Student.objects.get(id=self.id).profile_pic)
            except:
                return 'Anonymous'
            

class Friend(models.Model):
    
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='contact_friend')
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='friend_account')
    
    def __str__(self):
        return str(self.account)

    @property
    def friend_id(self):
        return self.id

class Conversation(models.Model):
    participants = models.ManyToManyField(Contact, related_name='conversation')
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.id
    
    @property
    def conversation_id(self):
        return self.id
    
class Message(models.Model):
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='conv_message')
    msg_contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content