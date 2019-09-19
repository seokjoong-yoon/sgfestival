from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.

class game1(models.Model):
    score=models.IntegerField(default=0)
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    userid=models.TextField(default='')
    university=models.TextField(default='')


# class Question(models.Model):
#     question = models.CharField(max_length=200)
#     answer = models.charField(max_length=200)

# class Answer(models.Model):
#     a1 = models.CharField(max_length=200)
#     a2 = models.CharField(max_length=200)
#     a3 = models.CharField(max_length=200)
#     a4 = models.CharField(max_length=200)
#     a5 = models.CharField(max_length=200)
#     a6 = models.CharField(max_length=200)
#     a7 = models.CharField(max_length=200)
#     a8 = models.CharField(max_length=200)
#     a9 = models.CharField(max_length=200)
#     a10 = models.CharField(max_length=200)
#     a11 = models.CharField(max_length=200)
#     a12 = models.CharField(max_length=200)
#     a13 = models.CharField(max_length=200)
#     a14 = models.CharField(max_length=200)
#     a15 = models.CharField(max_length=200)
#     a16 = models.CharField(max_length=200)
#     a17 = models.CharField(max_length=200)
#     a18 = models.CharField(max_length=200)
#     a19 = models.CharField(max_length=200)
#     a20 = models.CharField(max_length=200)

