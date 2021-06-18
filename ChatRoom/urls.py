"""ChatRoom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views import static
from django.views.generic import RedirectView

from ChatRoom.settings import DEBUG
from error.views import not_found, server_error, not_found_404, server_error_500
from login.views import login
from room.views import room, room_test

urlpatterns = [
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),

    # 登录界面
    url(r'^login/', login),
    # 空路径重定向至封面界面
    path('', RedirectView.as_view(url='login')),
    # 聊天室界面
    url(r'^room/', room),

    # 错误路径
    url(r'^not_found/', not_found),
    url(r'^server_error/', server_error),
]
# 添加debug下特殊访问界面
if DEBUG:
    urlpatterns.append(url(r'^admin/', admin.site.urls))
    urlpatterns.append(url(r'^room_test/', room_test))

# 更改错误跳转
handler404 = not_found_404
handler500 = server_error_500
