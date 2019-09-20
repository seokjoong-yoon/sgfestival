from django.db import models

# Create your models here.

EVENTDAY_CHOICE = (
        ('1', '1'),
        ('2', '2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
)

class Schedule(models.Model):
    eventDay = models.CharField(max_length=100, choices = EVENTDAY_CHOICE, default='mon')
    eventImage = models.ImageField(upload_to='images/', blank=True)
    eventContent = models.CharField(max_length = 300)
    eventTitle = models.CharField(max_length = 200)
    when = models.CharField(max_length=200, default='')
    where = models.CharField(max_length=200, default='')
    what = models.CharField(max_length=200, default='')
    