from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def cover_test(request):
    return HttpResponse("Hello World!!")  # 通过HttpResponse模块直接返回字符串到前端页面


def cover(request):
    # GET请求访问登录界面Login.html
    if request.method == 'GET':
        return render(request, "cover/cover.html")
    # POST请求获取登录信息
    elif request.method == 'POST':
        # if User.objects.filter(username=request.POST['username']).exists():
        #     user_info = {'username': request.POST['username']}
        #     # return render(request, "Room/Room.html", user_info)
        #     return redirect("/room/")
        # else:
        #     return render(request, "Error/404.html")
        return render(request, "cover/cover.html")
    # 跳转至错误界面
    else:
        # return render(request, "Error/404.html")
        return render(request, "cover/cover.html")


def revise_cover(request):
    return redirect("cover/")  # 重定向url
