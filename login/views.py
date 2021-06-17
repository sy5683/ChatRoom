from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    # GET请求访问登录界面
    if request.method == 'GET':
        return render(request, "login/login.html")
    # POST请求获取登录信息
    elif request.method == 'POST':
        # if User.objects.filter(username=request.POST['username']).exists():
        #     user_info = {'username': request.POST['username']}
        #     # return render(request, "Room/Room.html", user_info)
        #     return redirect("/room/")
        # else:
        #     return render(request, "Error/404.html")
        return render(request, "login/login.html")
    # 跳转至错误界面
    else:
        return render(request, "error/404.html")


def revise_login(request):
    return redirect("login/")  # 重定向url
