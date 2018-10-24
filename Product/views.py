# coding:utf-8
from django.shortcuts import render
from django.template.context_processors import request
from django.http.response import HttpResponse
from Product.productUtils import productManage
from Product.shopUtils import shopManage
# 实例化操作类
proManage = productManage()
shopmanage = shopManage()

# 发布商品
def releaseProduct(request):
    msg = proManage.addProduct(request)
    return Message(request, msg)

# 查看库存列表
def listProduct(request):
    uName = request.session['uName']
    shop = shopmanage.selectShop({'shopOwner': uName})
    if not shop:
        return Message(request, '你还没有开店！')
    shopId = shop[0].shopId
    data = proManage.product_list(
        request, {'proShopId': shopId}, 'OR', 'proId')
    return render(request, 'ProductList.html', locals())

# 信息提示页面
def Message(request, msg):
    return render(request, 'Message.html', {'msg': msg})

# 处理商品操作
def productAct(request, act, proId):
    pass
