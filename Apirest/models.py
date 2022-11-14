from django.db import models

STATUS_CHOICES = (
    #("Select a Status", "Select a Status"),
    ("In Progress", "In Progress"),
    ("Waiting", "Waiting"),
    ("Approuved", "Approuved"),
    ("In Review", "In Review"),
    ("Finish", "Finish"),
)
# Create your models here.
class Task(models.Model):
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
        
    