from django.db import models

# Create your models here.

class Schedule(models.Model):
    eventImage = models.ImageField(upload_to='images/', blank=True)
    eventContent = models.CharField(max_length = 300)
    eventTitle = models.CharField(max_length = 200)
