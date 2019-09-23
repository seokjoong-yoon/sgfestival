from django.shortcuts import render, get_object_or_404
from .models import Schedule

# Create your views here.

def schedule(request):
    post_list = Schedule.objects.all
    return render(request, "schedule/schedule.html", {'post_list' : post_list})

def schedule_detail(request, index):
    post = get_object_or_404(Schedule, pk=index)
    return render(request, 'schedule/schedule_detail.html', {'post':post})
