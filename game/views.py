from django.shortcuts import render, redirect, get_object_or_404
from .models import game1
from django.contrib.auth.models import User

# Create your views here.
def game1(request):
    count=0
    if request.method=="POST":
        # #user=User.objects.get(author=request.user)
        # one_tmp=request.POST['one']#일번
        # one=''
        # for i in range(len(one_tmp)):
        #     if one_tmp[i]!=' ':
        #         if ord(one_tmp[i])>=65 and ord(one_tmp[i])<=90:
        #             one=one+(chr(ord(one_tmp[i])+32))
        #         else:
        #             one=one+one_tmp[i]
        #          #one=one+one_tmp[i]
        # if one=="일번답":
        #     count=count+1
        # two_tmp=request.POST['two']#이번
        # two=''
        # for i in range(len(two_tmp)):
        #     if two_tmp[i]!=' ':
        #         two=two+two_tmp[i]
        # if two=="2번답":
        #     count=count+1

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
                    ans = ans + tmp[j]
            if ans == real_ans[i]:
                count = count+1

        return render(request, 'game/songresult.html', {'count':count})
    else:
        return render(request, 'game/song.html')

def game1result(request):
    return render(request, 'game/songresult.html', {'count': count})