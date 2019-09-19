from django.urls import path
from madang import views
from django.conf import settings
from django.conf.urls.static import static  
app_name = 'madang'

urlpatterns = [
    path('', views.madang, name='madang'),
    path('<int:pk>/', views.madang_detail, name="madang_detail"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)