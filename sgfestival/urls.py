
"""sgfestival URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import views as userviews
from game import views as gameviews
from attend import views as attendviews
from django.conf import settings
from django.conf.urls.static import static
import madang.views as mviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userviews.home, name='home'), 
    path('register/', userviews.register, name="register"), 
    path('login/', userviews.login, name="login"), 
    path('logout/', userviews.logout, name="logout"), 
    path('song/', gameviews.game1, name="game1"),
    path('inside/', gameviews.inside, name="inside"),
    path('songresult/', gameviews.game1result, name="game1result"),
    path('dptsongrank/', gameviews.dptsongrank, name="dptsongrank"), 
    path('dptinsiderank/', gameviews.dptinsiderank, name='dptinsiderank'),
    path('song/songrank/', gameviews.songrank, name="songrank"),
    path('inside/insiderank/', gameviews.insiderank, name="insiderank"),
    path('attend/', attendviews.attend, name='attend'),
    path('guide/', userviews.guide, name="guide"),
    path('schedule/', include("schedule.urls", namespace="schedule")),
    path('madang/', include("madang.urls", namespace="madang")),
    path('madang/<int:pk>/', mviews.madang_detail, name="madang_detail"),
    path('lineup', mviews.lineup, name="lineup"),
    path('performtime', mviews.performtime, name="performtime"),
    path('foodtruck/', include("foodtruck.urls", namespace="foodtruck")),
    path('timetable/',mviews.timetable,name="timetable"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
