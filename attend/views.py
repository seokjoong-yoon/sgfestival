from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from accounts.models import Myuser
import time
# Create your views here.
def attend(request):
    now=time.localtime()
    myuser=Myuser.objects.get(username=request.user)
    tue=myuser.tue
    wed=myuser.wed
    thur=myuser.thur
    fri=myuser.fri
    att=[]
    att.append(tue)
    att.append(wed)
    att.append(thur)
    att.append(fri)
    for i in range(1, 5):
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
        elif i==now.tm_wday:
            if att[i-1]==0:
                att[i-1]=1
                if i==2:
                    myuser.tue=1
                elif i==3:
                    myuser.wed=1
                elif i==4:
                    myuser.thur=1
                elif i==5:
                    myuser.fri=1
                myuser.attendcount=myuser.attendcount+1
        elif i>now.tm_wday:
            continue;
    myuser.save()
    return render(request, 'attend/attend.html', {'tue':int(att[0]), 'wed':int(att