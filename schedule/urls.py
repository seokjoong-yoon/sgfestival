from django.urls import path
from schedule import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'schedule'

urlpatterns = [
    path('', views.schedule, name='schedule'),
    path('detail/<int:index>', views.schedule_detail, name='schedule_detail'),   
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)