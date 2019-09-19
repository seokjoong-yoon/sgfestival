from django.shortcuts import render,redirect, get_object_or_404
from .models import Madang

# Create your views here.
def madang(request):
    madang = Madang.objects.all
    return render(request, 'madang/madang.html',{'madang':madang} )

def madang_detail(request, pk):
    madang = get_object_or_404(Madang, pk=pk)
    return render(request, 'madang/madang_detail.html', {'madang':madang})

def lineup(request):
    return render(request, 'madang/lineup.html')
    
def performtime(request):
    return render(request, 'madang/performtime.html')