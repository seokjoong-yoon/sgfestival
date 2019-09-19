from django.shortcuts import render, redirect, get_object_or_404
from .models import game1
from django.contrib.auth.models import User
from accounts.models import Myuser
# Create your views here.
def game1(request):
    if request.user.song_done == True:
        return render(request, 'game/songresult.html')
    if request.method=="POST":
        count=0
        real_ans = ['1번답', '2번답', '3번답', '4번답']
        ans_set = []
        for i in range(1, 5):           #(1,n) 1부터 n-1까지
            l = str(i)
            ans_set.append(request.POST[l])

        for i in range(4):
            tmp = ans_set[i]
            ans = ''
            for j in range(len(tmp)):
                if tmp[j] != ' ':
                    if ord(tmp[j]) >=65 and ord(tmp[j])<=90:
                        ans = ans+(chr(ord(tmp[j])+32))
                    else :
                        ans = ans + tmp[j]
            if ans == real_ans[i]:
                count = count+1
        myuser=Myuser.objects.get(username=request.user)
        myuser.songscore = count
        myuser.song_done = True
        myuser.save()
        return render(request, 'game/songresult.html', {'count':count})
    else:
        return render(request, 'game/song.html')

def inside(request):
    if request.user.inside_done == True:
        return render(request, 'game/insideresult.html')
    if request.method=="POST":
        count=0
        real_ans = ['1번답', '2번답', '3번답', '4번답']
        ans_set = []
        for i in range(1, 5):           #(1,n) 1부터 n-1까지
            l = str(i)
            ans_set.append(request.POST[l])

        for i in range(4):
            tmp = ans_set[i]
            ans = ''
            for j in range(len(tmp)):
                if tmp[j] != ' ':
                    if ord(tmp[j]) >=65 and ord(tmp[j])<=90:
                        ans = ans+(chr(ord(tmp[j])+32))
                    else :
                        ans = ans + tmp[j]
            if ans == real_ans[i]:
                count = count+1
        myuser=Myuser.objects.get(username=request.user)
        myuser.insidescore = count
        myuser.inside_done = True
        myuser.save()
        return render(request, 'game/insideresult.html', {'count':count})
    else:
        return render(request, 'game/inside.html')


def game1result(request):
    return render(request, 'game/songresult.html', {'count': count})