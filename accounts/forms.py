from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Myuser

class MyuserCreationForm(UserCreationForm):
    CHOICE = (('1', '국제인문학부'), ('2', '사회과학부'), ('3', '지식융합미디어학부'), ('4', '자연과학부'), ('5', '공학부'), ('6', '경제학부'), ('7', '경영학부'), ('8', '커뮤니케이션학부'))
    dpt = forms.ChoiceField(choices=CHOICE, label='학부',widget=forms.Select)

    class Meta(UserCreationForm):
        model = Myuser
        fields = ('username', 'password1', 'password2', 'dpt')
