from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from accounts.models import Myuser
import time
# Create your views here.
def attend(request):
    # 0은 공백 , 아직 날짜가 오지 않은 상황
    # 1은 출석체크 버튼을 누른 상황
    # -1은 날짜가 지났는데 안 누른 상황
    # 2는 오늘인데 아직 안 누른 상황
    if request.method=="POST":
        now=time.localtime()
        myuser=Myuser.objects.get(username=request.user)
        if now.tm_wday==1:
            myuser.tue=1
        elif now.tm_wday==2:
            myuser.wed=1
        elif now.tm_wday==3:
            myuser.thur=1
        elif now.tm_wday==4:
            myuser.fri=1
        elif now.tm_wday==5:
            myuser.sat=1
        elif now.tm_wday==6:
            myuser.sun=1
        myuser.attendcount=myuser.attendcount+1
        att=[]
        tue=myuser.tue
        wed=myuser.wed
        thur=myuser.thur
        fri=myuser.fri
        sat=myuser.sat
        sun=myuser.sun

        att.append(tue)
        att.append(wed)
        att.append(thur)
        att.append(fri)
        att.append(sat)
        att.append(sun)

        myuser.save()
        return render(request, 'attend/attend.html', {'tue':int(att[0]), 'wed':int(att[1]), 'thur':int(att[2]), 'fri':int(att[3]), 'sat':int(att[4]), 'sun':int(att[5])})
    else:
        now=time.localtime()
        myuser=Myuser.objects.get(username=request.user)
        tue=myuser.tue
        wed=myuser.wed
        thur=myuser.thur
        fri=myuser.fri
        sat=myuser.sat
        sun=myuser.sun

        att=[]
        att.append(tue)
        att.append(wed)
        att.append(thur)
        att.append(fri)
        att.append(sat)
        att.append(sun)
        for i in range(1, 8):
            if i<now.tm_wday:
                if att[i-1]==0:
                    att[i-1]=-1
                    if i==2:
                        myuser.tue=-1
                    elif i==3:
                        myuser.wed=-1
                    elif i==4:
                        myuser.thur=-1
                    elif i==5:
                        myuser.fri=-1
                    elif i==6:
                        myuser.sat=-1
                    elif i==7:
                        myuser.sun=-1
            elif i==now.tm_wday:
                if att[i-1]==0:
                    att[i-1]=2
        myuser.save()
        return render(request, 'attend/attend.html', {'tue':int(att[0]), 'wed':int(att[1]), 'thur':int(att[2]), 'fri':int(att[3]), 'sat':int(att[4]), 'sun':int(att[5])})