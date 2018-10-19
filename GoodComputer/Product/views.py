# coding:utf-8
from django.shortcuts import render
from django.template.context_processors import request
from django.http.response import HttpResponse
from Product.productUtils import productManage

# 实例化操作类
proManage = productManage()

# 发布商品
def releaseProduct(request):
    msg = proManage.addProduct(request)
    return Message(request, msg)

# 查看库存列表
def listProduct(request):
    return HttpResponse('正在建设中')

# 信息提示页面
def Message(request, msg):
    return render(request, 'Message.html', {'msg': msg})
