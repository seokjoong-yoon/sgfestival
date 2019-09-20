from django.db import models

# Create your models here.

EVENTDAY_CHOICE = (
    ('mon', 'mon'),
    ('tue', 'tue'),
    ('wed', 'wed'),
    ('thu', 'thu'),
    ('fri', 'fri'),
)

class Schedule(models.Model):
    eventDay = models.CharField(max_length=100, choices = EVENTDAY_CHOICE, default='mon')
    eventImage = models.ImageField(upload_to='images/', blank=True)
    eventContent = models.CharField(max_length = 300)
    eventTitle = models.CharField(max_length = 200)
    