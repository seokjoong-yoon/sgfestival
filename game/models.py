from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.

class game1(models.Model):
    score=models.IntegerField(default=0)
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    userid=models.TextField(default='')
    university=models.TextField(default='')
