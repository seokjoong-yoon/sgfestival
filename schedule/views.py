from django.shortcuts import render

# Create your views here.

def schedule(request):
    return render(request, "schedule/schedule.html")