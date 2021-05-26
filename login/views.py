from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def login_revise(request):
    return redirect("login")  # 重定向url


def login(request):
    return HttpResponse("Hello World!!")  # 通过HttpResponse模块直接返回字符串到前端页面
