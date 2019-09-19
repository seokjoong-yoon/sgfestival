
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
import madang.views as mviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('schedule/', include("schedule.urls")),
    path('madang/', include("madang.urls", namespace="madang")),
    path('madang/<int:pk>/', views.madang_detail, name="madang_detail"),
    path('lineup', mviews.lineup, name="lineup"),
    path('performtime', mviews.performtime, name="performtime"),
    path('foodtruck/', include("foodtruck.urls")),
]

