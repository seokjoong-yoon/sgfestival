from django.urls import path
from foodtruck import views
from django.conf import settings
from django.conf.urls.static import static  

app_name = 'foodtruck'

urlpatterns = [
    path('', views.foodtruck, name='foodtruck'),
    path('detail_korean/', views.foodtruck_detail_korean, name='foodtruck_detail_korean'),
    path('detail_western', views.foodtruck_detail_western, name='foodtruck_detail_western'),
    path('detail_dessert', views.foodtruck_detail_dessert, name='foodtruck_detail_dessert'),
    path('detail_etc', views.foodtruck_detail_etc, name='foodtruck_detail_etc'),
    path('review/<int:index>', views.foodtruck_review_korean, name='foodtruck_review_korean'),
    path('review/<int:index>', views.foodtruck_review_western, name='foodtruck_review_western'),
    path('review/<int:index>', views.foodtruck_review_dessert, name='foodtruck_review_dessert'),
    path('review/<int:index>', views.foodtruck_review_etc, name='foodtruck_review_etc'),
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)