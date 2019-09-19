from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import MyuserCreationForm
from .models import Myuser

class MyuserAdmin(UserAdmin):
    model = Myuser
    add_form = MyuserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', {
            'fields': ('dpt','check','songscore', 'insidescore', 'song_done', 'inside_done')}),
    )

admin.site.register(Myuser, MyuserAdmin)