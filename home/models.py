from django.db import models

# Create your models here.
class UserInput  (models.Model):
    date = models.DateField(null=True);
    time = models.TimeField(null=True);
    date_time = models.DateTimeField(null=True);
    userinput = models.CharField(max_length=200);