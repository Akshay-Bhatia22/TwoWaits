from django.db import models
from Accounts.models import UserAccount


class Faculty(models.Model):
    DEAPARTMENTS = (('CS', 'Computer Science'),
                    ('CS&IT', 'Computer Science and IT'),
                    ('IT', 'IT'),
                    ('ME', 'Mechanical Engineering'),
                    ('CE', 'Civil Engineering'),
                    ('EE', 'Electrical and Electronics'),
                    ('Humanities', 'Humanities'),
                    ('Others','Any other'))  

    GENDER = (('M','Male'),
            ('F','Female'),
            ('O','Others'))

    faculty_account_id = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name='faculty')
    
    name = models.CharField(max_length=30, blank=False)
    department = models.CharField(max_length=10, choices=DEAPARTMENTS, blank=True, null=True)
    college = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=8, choices=GENDER, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to = 'ProfilePic' ,default = 'ProfilePic/Avatar1.png')
    
    def __str__(self):
        return self.name
