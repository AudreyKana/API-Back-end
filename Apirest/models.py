from django.db import models
from django.conf import  settings
# from django.contrib.auth.models import User
# from django.contrib.auth.models import(BaseUserManager, AbstractBaseUser)

STATUS_CHOICES = (
    #("Select a Status", "Select a Status"),
    ("In Progress", "In Progress"),
    ("Waiting", "Waiting"),
    ("Approuved", "Approuved"),
    ("In Review", "In Review"),
    ("Finish", "Finish"),
)

User = settings.AUTH_USER_MODEL 

# Create your models here.
class Task(models.Model):
    user= models.ForeignKey(User, default=1, null=True,  on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    date = models.DateField(null = True)
    periode = models.TimeField(null = True)
    status = models.CharField(
        max_length = 200,
        choices = STATUS_CHOICES,
        #default = 'Select a Status'
    )
    #completed = models.BooleanField(default=False, blank=True, null=True)
    important = models.BooleanField(default = False)
    logo = models.ImageField(blank=True, null = True, upload_to='images/')
    is_deleted = models.BooleanField(default= False)
    objects = models.Manager()
   
    def __str__(self):
        return self.title
    

# class User(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
    
#     def __str__(self):
#         return self.name

# class Entry(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.user