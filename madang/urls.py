from django.urls import path
from madang import views

app_name = 'madang'

urlpatterns = [
    path('', views.main, name='madang'),   
    path('', views.main, name='madang'),
]