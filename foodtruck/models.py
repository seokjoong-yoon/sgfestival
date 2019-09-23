from django.db import models
from django.utils import timezone

# Create your models here.

FOOD_CATEGORY = (
('korean','한식'),
('western','양식'),
('dessert','디저트'),
('etc','기타'),
)

FOODTRUCK_RATING = (
    (5, '5'),
    (4, '4'),
    (3, '3'),
    (2, '2'),
    (1, '1'),
)

class Foodtruck(models.Model):
    ftName = models.CharField(max_length=100, blank=True)
    ftImage = models.ImageField(upload_to = 'images/', blank=True)
    ftCategory = models.CharField(max_length = 100, choices=FOOD_CATEGORY, default='')
    generalRating = models.FloatField(max_length=10, default="0.0")
    ftMenu1 = models.CharField(max_length=100, blank=True)
    ftMenu2 = models.CharField(max_length=100, blank=True)
    ftMenu3 = models.CharField(max_length=100, blank=True)
    ftMenu4 = models.CharField(max_length=100, blank=True)
    ftMenu5 = models.CharField(max_length=100, blank=True)
    ftMenu6 = models.CharField(max_length=100, blank=True)
    ftMenu7 = models.CharField(max_length=100, blank=True)
    ftMenu8 = models.CharField(max_length=100, blank=True)
    ftMenu9 = models.CharField(max_length=100, blank=True)
    ftMenu10 = models.CharField(max_length=100, blank=True)

class FoodtruckComment(models.Model):
    foodtruck = models.ForeignKey(Foodtruck, on_delete=models.CASCADE)
    ftRating = models.FloatField(max_length=10, choices=FOODTRUCK_RATING, default="5")
    ftCommentImage = models.ImageField(upload_to='images/', blank=True)
    ftComment = models.CharField(max_length=300, blank=True)
    ftCommentAuthor = models.CharField(max_length=100, default='Anonymous')
    ftCommentTimeStamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-ftCommentTimeStamp',)





    
