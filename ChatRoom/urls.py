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
from cover.views import revise_cover, cover
from error.views import not_found, server_error, not_found_404, server_error_500

urlpatterns = [
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),

    path('admin/', admin.site.urls),
    path('cover_test/', cover) if DEBUG else path('admin/', cover),

    path('not_found', not_found),
    path('server_error', server_error),

    path('', RedirectView.as_view(url='cover/')),  # 空路径重定向至登录界面
    path('cover/', cover),
    path('cover', revise_cover),

]

handler404 = not_found_404
handler500 = server_error_500
