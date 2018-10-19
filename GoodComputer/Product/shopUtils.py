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

# 操作类实例化
stringutil = stringUtil()
sqlutil = sqlUtil(shop)

class shopManage():
    # 商店注册
    def addShop(self, request):
        shopOwner = request.session['uName']
        if self.selectShop({'shopOwner': shopOwner}):
            return '抱歉，你已经开过店了，一个人只能开一个店！'
        shopId = stringutil.getRnStr(10)
        shopName = request.POST.get('shopName')
        shopDesc = request.POST.get('shopDesc')
        shopImg = request.FILES.get('shopImg')
        shopTime = stringutil.getDate()
        # 更改图片名并保存图片
        filename = 'shop_' + shopId
        imgutil = imgUtil('img/shop/' + shopId, str(shopImg.name))
        imgutil.imgName = imgutil.change_upImg_name(filename)
        imgutil.saveImg(shopImg)
        s = shop(shopId, shopName, shopOwner, 0,
                 0, shopDesc, imgutil.imgDir + imgutil.imgName, shopTime)
        if sqlutil.add(s):
            return '开店成功,可以发布商品了！'
        return '开店失败,重新添加'

    # 查询商店信息
    def selectShop(self, args):
        return sqlutil.select(args, 'OR', 'shopId')