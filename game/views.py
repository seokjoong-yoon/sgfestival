from django.shortcuts import render, redirect, get_object_or_404
from .models import game1
from django.contrib.auth.models import User
from accounts.models import Myuser
from collections import OrderedDict
import json
from django.http import HttpResponse, JsonResponse
# Create your views here.
def game1(request):
    if request.user.song_done == True:
        total=Myuser.objects.filter(song_done=True).count()
        userscore=Myuser.objects.filter(song_done=True).order_by('-songscore')
        rankD = OrderedDict()
        for user in userscore:
            if user.songscore in rankD.keys():
                rankD[user.songscore].append(user)
            else:
                rankD[user.songscore]=[user]
        rank=list(rankD.keys()).index(request.user.songscore)        
        return render(request, 'game/songresult.html', {"rank":rank+1, "total":total})
    if request.method=="POST":
        count=0
        real_ans = ['위아래', '빠빠빠', '비밀번호486', '내귀에캔디', '거북선',
                    '눈코입', 'bopeepbopeep', 'tellme', 'gentleman', 'hotsummer',
                    '10점만점에10점', '샤방샤방', '벚꽃엔딩', 'goodbyebaby', 'honey',
                    'callmebaby', '로꾸거', '나혼자', 'rose', 'nonono']
        ans_set = []
        for i in range(1, 21):           #(1,n) 1부터 n-1까지
            l = str(i)
            ans_set.append(request.POST[l])

        for i in range(20):
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
        return render(request, 'game/songresult.html', {"count":count})
    else:
        return render(request, 'game/song.html')

def songrank(request):
    if request.method == "GET":
        total=Myuser.objects.filter(song_done=True).count()
        userscore=Myuser.objects.filter(song_done=True).order_by('-songscore')
        rankD = OrderedDict()        
        for user in userscore:
            if user.songscore in rankD.keys():
                rankD[user.songscore].append(user)
            else:
                rankD[user.songscore]=[user]
        rank=list(rankD.keys()).index(request.user.songscore)
        context={"rank":rank+1, "total":total}
        return JsonResponse(context)

def inside(request):
    if request.user.inside_done == True:
        total=Myuser.objects.filter(inside_done=True).count()
        userscore=Myuser.objects.filter(inside_done=True).order_by('-insidescore')
        rankD = OrderedDict()
        for user in userscore:
            if user.insidescore in rankD.keys():
                rankD[user.insidescore].append(user)
            else:
                rankD[user.insidescore]=[user]
        rank=list(rankD.keys()).index(request.user.insidescore)

        return render(request, 'game/insideresult.html', {"rank":rank+1,"total":total})
    if request.method=="POST":
        count=0
        real_ans = ['응답하라1994', '별에서온그대', '꽃보다남자', 'gee', '으르렁',
                    '루시퍼', 'nonono', '내꺼하자', 'sohot', '차카니',
                    '멜짱', '쿠우', '텐텐', '미니벨', '아폴로']
        ans_set = []
        for i in range(1, 16):           #(1,n) 1부터 n-1까지
            l = str(i)
            ans_set.append(request.POST[l])

        for i in range(15):
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
        
def insiderank(request):
    total=Myuser.objects.filter(inside_done=True).count()
    userscore=Myuser.objects.filter(inside_done=True).order_by('-insidescore')
    rankD = OrderedDict()
    for user in userscore:
        if user.insidescore in rankD.keys():
            rankD[user.insidescore].append(user)
        else:
            rankD[user.insidescore]=[user]
    rank=list(rankD.keys()).index(request.user.insidescore)
    context={"rank":rank+1, "total":total}
    return JsonResponse(context)


def game1result(request):
    return render(request, 'game/songresult.html', {'count': count})

def dptsongrank(request):
    users=Myuser.objects.filter(song_done=True).order_by('dpt')
    L=[0]*9
    for user in users:
        if user.dpt == '':
            continue
        if int(user.dpt)>0:
            L[int(user.dpt)]+=1
    
    D={1:'국제인문학부', 2:'사회과학부', 3:'지식융합미디어학부', 4:'자연과학부', 5:'공학부', 6:'경제학부', 7:'경영학부', 8:'커뮤니케이션학부'}
    result = OrderedDict()
    i=0
    while sum(L) :
        maxi=L.index(max(L))   
        if maxi==0:
            continue
        result[D[maxi]]=max(L)
        L[maxi]=0
    return render(request, 'game/dptsong.html', {"result":result})

def dptinsiderank(request):
    users=Myuser.objects.filter(inside_done=True).order_by('dpt')
    L=[0]*9
    for user in users:
        if user.dpt == '':
            continue
        if int(user.dpt)>0:
            L[int(user.dpt)]+=1
    
    D={1:'국제인문학부', 2:'사회과학부', 3:'지식융합미디어학부', 4:'자연과학부', 5:'공학부', 6:'경제학부', 7:'경영학부', 8:'커뮤니케이션학부'}
    result = OrderedDict()
    i=0
    while sum(L) :
        maxi=L.index(max(L))   
        if maxi==0:
            continue
        result[D[maxi]]=max(L)
        L[maxi]=0
    return render(request, 'game/dptinside.html', {"result":result})

