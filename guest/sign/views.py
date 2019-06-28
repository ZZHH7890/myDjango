'''
@Author: joker.zhang
@Date: 2019-06-28 13:59:05
@LastEditors: joker.zhang
@LastEditTime: 2019-06-28 15:20:58
@Description: For Automation
'''
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
