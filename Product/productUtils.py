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
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger  # 导入结果集分页类
import os
# 操作类实例化
stringutil = stringUtil()
sqlutil = sqlUtil(product)
shopmanage = shopManage()

class productManage():
    # 发布商品
    def addProduct(self, request):
        uName = request.session.get('uName')
        s = shopmanage.selectShop({'shopOwner': uName})
        if not s:
            return '先<a href="/user/enter/businessCenter?util=freeOpenShop">免费开店</a>,再发布商品吧'
        proShopId = s[0].shopId
        proShopName = s[0].shopName
        proId = stringutil.getRnStr(12)
        proName = request.POST.get('proName')
        proPrice = request.POST.get('proPrice')
        proStock = request.POST.get('proStock')
        proBrand = request.POST.get('proBrand')
        proSeries = request.POST.get('proSeries')
        proDesc = request.POST.get('proDesc')
        proImg = request.FILES.getlist('proImg')  # 获取上传的图片列表
        imgPath = []  # 将图片的相对路径以列表的形式存入数据库
        imgs = []  # 存储图片对象
        for i in range(len(proImg)):
            Dir = os.path.join('img/shop/', proShopId + '/', proId + '/')
            img = imgUtil(Dir, proImg[i].name)
            img.imgName = img.change_upImg_name('pro_' + proId + str(i + 1))
            imgPath.append(img.imgDir + img.imgName)
            imgs.append(img)
        proTime = stringutil.getDate()
        p = product(proId, proName, proPrice, proStock, '1', '0', 0, 0,
                    proBrand, proSeries, proDesc, proShopId, proShopName, imgPath, proTime)
        if sqlutil.add(p):
            for j in range(len(proImg)):  # 保存图片
                imgs[j].saveImg(proImg[j])
            return '发布成功,<a href="/user/enter/businessCenter?util=releaseProduct">继续添加?</a>|<a href="/product/list-product?page=1">查看库存</a>'
        return '发布失败'

    # 商品列表及分页显示
    def product_list(self, request, args, connect_type, order_by):
        num = request.GET.get('page')  # 获取页数参数
        try:
            data = self.selectProduct(args, connect_type, order_by)
            # 将结果按每页15条数据进行分页，当后一页记录低于2条时归于上一页
            paginator = Paginator(data, 15, 2)
            page = paginator.page(num)
        except PageNotAnInteger:  # 当页数不为整数
            page = paginator.page(1)
        except EmptyPage:  # 当页数为空
            page = paginator.page(1)
        except InvalidPage:  # 当页数无效
            page = paginator.page(1)
        return locals()

     # 商品查询
    def selectProduct(self, args=None, connect_type='OR', order_by='proId'):
        return sqlutil.select(args, connect_type, order_by)
