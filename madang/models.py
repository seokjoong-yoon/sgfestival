from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
CATEGORY_CHOICES=(
        ('1', '1'),
        ('2', '2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        )

class Madang(models.Model):
    title = models.CharField(max_length=100, default='')
    contents = models.CharField(max_length=100, default='')
    detail = models.CharField(max_length=1500, default='')
    price = models.CharField(max_length=100, default='')
    image1 = models.ImageField(upload_to='images/', blank=True)
    image2 = models.ImageField(upload_to='images/', blank=True)
    image3 = models.ImageField(upload_to='images/', blank=True)
    image4 = models.ImageField(upload_to='images/', blank=True)
    image5 = models.ImageField(upload_to='images/', blank=True)
    image6 = models.ImageField(upload_to='images/', blank=True)
    image7 = models.ImageField(upload_to='images/', blank=True)
    image8 = models.ImageField(upload_to='images/', blank=True)
    category = models.CharField(
        max_length =100,
        choices = CATEGORY_CHOICES,
        default  = '',
        )

class jooho(models.Model):
        title = models.CharField(max_length=100)

