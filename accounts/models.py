from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Myuser(AbstractUser):
    check=models.CharField(max_length=255)  #출석체크
    dpt=models.CharField(default='', max_length=255)    #학부
    score=models.FloatField(default=0)     #게임 점수