# coding:utf-8
"""EasyChart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from User import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
import xadmin
xadmin.autodiscover()

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('index', views.index, name='index'),
    path('user/', include('User.urls')),
    path('Inform/', include('Inform.urls')),
    #     url(r'^static/(?P<path>.*)$', serve,
    #         {'document_root': settings.STATIC_ROOT}),  # debug=true时的static配置方式
    #     url(r'^media/(?P<path>.*)$', serve,
    #         {'document_root': settings.MEDIA_ROOT})  # debug=true时的media配置方式
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Debug=true时，添加media路径的方式
