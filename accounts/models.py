from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Myuser(AbstractUser):
    check=models.CharField(max_length=255)  #출석체크
    dpt=models.CharField(default='', max_length=255)    #학부
    songscore=models.IntegerField(default=0)     #노래 게임 점수
    insidescore=models.IntegerField(default=0)     #인싸 게임 점수
    song_done=models.BooleanField(default=False)    #노래 게임 완료
    inside_done=models.BooleanField(default=False)  #인싸 게임 완료
    tue=models.IntegerField(default=0)
    wed=models.IntegerField(default=0)
    thur=models.IntegerField(default=0)
    fri=models.IntegerField(default=0)
    sat=models.IntegerField(default=0)
    sun=models.IntegerField(default=0)
    attendcount=models.IntegerField(default=0)
