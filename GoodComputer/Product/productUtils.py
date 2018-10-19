# coding:utf-8
'''
@Created on :2018-10-19
@function:定义商品管理类
@author: jxc
'''
from Product.models import product
from CommonUtils.stringUtils import stringUtil
from CommonUtils.imgUtils import imgUtil
from CommonUtils.sqlUtils import sqlUtil
from Product.shopUtils import shopManage
# 操作类实例化
stringutil = stringUtil()
sqlutil = sqlUtil(product)
shopmanage = shopManage()

class productManage():
    def addProduct(self, request):
        uName = request.session['uName']
        shop = shopmanage.selectShop({'shopOwner': uName})
        if shop:
            proShopId = shop.shopId
        else:
            proShopId = None
        proShopName = uName
        proId = stringutil.getRnStr(12)
        proName = request.POST.get('proName')
        proPrice = request.POST.get('proPrice')
        proStock = request.POST.get('proStock')
        proBrand = request.POST.get('proBrand')
        proSeries = request.POST.get('proSeries')
        proDesc = request.POST.get('proDesc')
        proImg = request.POST.getlist('proImg')  # 获取上传的图片列表
        imgs = []
        for i in range(len(proImg)):
            dir = 'img/shop/' + proShopId + '/' + proId
            img = imgUtil(dir, proImg[i].name)
            img.imgName = img.change_upImg_name('pro_' + proId + str(i + 1))
            imgs.append(img.imgDir + img.imgName)
            img.saveImg(proImg[i])
        proTime = stringutil.getDate()
        p = product(proId, proName, proPrice, proStock, '1', '0', 0, 0,
                    proBrand, proSeries, proDesc, proShopId, proShopName, imgs, proTime)
        if sqlutil.add(p):
            return '发布成功,<a href="/user/enter/businessCenter?util=releaseProduct">继续添加?</a>|<a href="/product/act=/list-product?page=1">查看库存</a>'
        return '发布失败'
