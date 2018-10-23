# coding:utf-8
'''
@Created on :2018-10-18
@function:定义店铺管理类
@author: jxc
'''
from Product.models import shop
from CommonUtils.stringUtils import stringUtil
from CommonUtils.imgUtils import imgUtil
from CommonUtils.sqlUtils import sqlUtil
import os
from haystack.urls import url
# 操作类实例化
stringutil = stringUtil()
sqlutil = sqlUtil(shop)

class shopManage():
    # 商店注册
    def addShop(self, request):
        if self.isOpenShop(request):
            return '抱歉，你已经开过店了，一个人只能开一个店！'
        shopId = stringutil.getRnStr(10)
        shopName = request.POST.get('shopName')
        shopOwner = request.session.get('uName')
        shopDesc = request.POST.get('shopDesc')
        shopImg = request.FILES.get('shopImg')
        shopTime = stringutil.getDate()
        # 更改图片名
        filename = 'shop_' + shopId
        Dir = os.path.join('img/shop/', shopId + '/')  # 相对路径
        imgutil = imgUtil(Dir, str(shopImg.name))
        imgutil.imgName = imgutil.change_upImg_name(filename)
        s = shop(shopId, shopName, shopOwner, 0,
                 0, shopDesc, imgutil.imgDir + imgutil.imgName, shopTime)
        if sqlutil.add(s):
            imgutil.saveImg(shopImg)  # 保存图片
            return '开店成功,可以<a href="/user/enter/businessCenter?util=releaseProduct">发布商品</a>了！'
        return '开店失败'

    # 查询商店信息
    def selectShop(self, args):
        return sqlutil.select(args, 'OR', 'shopId')

    # 判断是否开过店
    def isOpenShop(self, request):
        uName = request.session['uName']
        if self.selectShop({'shopOwner': uName}):
            return True
        return False
