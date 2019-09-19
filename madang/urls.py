
from django.urls import path
from madang import views
from django.conf import settings
from django.conf.urls.static import static  
app_name = 'madang'

urlpatterns = [
    path('', views.madang, name='madang'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)