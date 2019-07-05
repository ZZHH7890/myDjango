'''
@Author: joker.zhang
@Date: 2019-06-28 13:59:05
@LastEditors: joker.zhang
@LastEditTime: 2019-07-04 11:10:04
@Description: For Automation
'''
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password= request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            request.session['user']=username
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})

        # if username =='admin' and password =='admin123':
        #     response = HttpResponseRedirect('/event_manage/')
        #     #response.set_cookie('user',username,3600)
        #     request.session['user']=username
        #     return response 
        # else:
        #     return render(request,'index.html',{'error':'username or password error!'})

@login_required
def event_manage(request):
    #username = request.COOKIES.get('user','')
    username = request.session.get('user','')
    return render(request,'event_manage.html',{'user':username})