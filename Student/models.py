from django.db import models
from Accounts.models import UserAccount

class Student(models.Model):
    COURSE = (('BTECH', 'BTECH'),
            ('MTECH','MTECH'),
            ('BCA','BCA'),
            ('MCA','MCA'),
            ('MBA','MBA'),
            ('BBA','BBA'),
            ('BA','BA'),
            ('MA','MA'),)
            
    BRANCH = (('CS', 'Computer Science'),
            ('CS&IT', 'Computer Science and IT'),
            ('IT', 'IT'),
            ('ME', 'Mechanical Engineering'),
            ('CE', 'Civil Engineering'),
            ('EE', 'Electrical and Electronics'),
            ('Humanities', 'Humanities'),
            ('Others','Any other'))  

    YEAR = (('1','1st year'), ('2','2nd year'), ('3','3rd year'), ('4','4th year'))

    # INTEREST = (('Job','Job'),
    #             ('GATE','GATE'),
    #             ('GRE','GRE'),
    #             ('CAT','CAT'),
    #             ('MBA','MBA'),
    #             ('MS','MS'),)

    GENDER = (('M','Male'),
              ('F','Female'),
              ('O','Others'))

    student_account_id = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name='student')
    
    name = models.CharField(max_length=30, blank=False)
    college = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=10, choices=COURSE, blank=True, null=True)
    branch = models.CharField(max_length=10, choices=BRANCH, blank=True, null=True)
    year = models.CharField(max_length=1, choices=YEAR, blank=True, null=True)
    gender = models.CharField(max_length=8, choices=GENDER, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to = 'ProfilePic' ,default = 'ProfilePic/Avatar1.png')
    profile_pic_firebase = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name
