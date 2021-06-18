from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def room(request):
    return HttpResponse("Hello World")  # 通过HttpResponse模块直接返回字符串到前端页面
    # user_info = {}
    # # GET请求访问登录界面
    # if request.method == 'GET':
    #     return render(request, "error/500.html")
    # # POST请求获取登录信息
    # elif request.method == 'POST':
    #     user_info['username'] = request.POST['username']
    #     return render(request, "room/room.html", user_info)
    # # 跳转至错误界面
    # else:
    #     return render(request, "error/404.html")


def room_test(request):
    return HttpResponse("Hello World!!")  # 通过HttpResponse模块直接返回字符串到前端页面
