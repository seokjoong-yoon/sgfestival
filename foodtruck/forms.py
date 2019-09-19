from django import forms
from .models import FoodtruckComment, Foodtruck

class FoodtruckCommentForm(forms.ModelForm):
    class Meta:
        model = FoodtruckComment
        exclude=['foodtruck', 'ftCommentTimeStamp']