# coding:utf-8
'''
@Created on :2018-10-16
@function:前端获取图片的中间件
@author: jxc
'''
from django.utils.deprecation import MiddlewareMixin
from django.http.response import HttpResponse


class GetImageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if 'get-image' in request.path:
            name = request.GET.get('name')
            with open('static/img/' + name, 'rb')as f:
                return HttpResponse(f.read())
