# coding:utf-8
'''
@Created on :2018-10-15
@function:定义店铺类、商品类
@author: jxc
'''
from django.db import models
from Product.listfield import ListField

# 店铺类
class shop(models.Model):
    shopId = models.CharField(
        primary_key=True, max_length=20, null=False)  # 店铺编号
    shopName = models.CharField(max_length=20, null=False)  # 店铺名称
    shopOwner = models.CharField(max_length=20, null=False)  # 开店人
    shopHoner = models.IntegerField(null=False)  # 店铺荣誉
    shopNotice = models.IntegerField(null=False)  # 店铺人气
    shopDesc = models.CharField(max_length=30, null=True)  # 店铺描述
    shopImg = models.ImageField(upload_to='img/shop/', null=False)  # 店铺图片
    shopTime = models.CharField(max_length=20, null=True)  # 开店时间

    class Meta:
        db_table = 'shop'

    def __str__(self):
        return models.Model.__str__(self)


# 商品类
class product(models.Model):
    proId = models.CharField(
        primary_key=True, max_length=20, null=False)  # 商品编号
    proName = models.CharField(max_length=20, null=False)  # 商品名称
    proPrice = models.CharField(max_length=10, null=False)  # 价格
    proStock = models.CharField(max_length=10, null=False)  # 库存量
    proSale = models.BooleanField()  # 是否上架
    proHot = models.BooleanField()  # 是否热卖
    proRmark = models.CharField(max_length=20, null=False)  # 评论数
    proTrade = models.CharField(max_length=20, null=False)  # 交易量
    proBrand = models.CharField(max_length=10, null=False)  # 所属品牌
    proSeries = models.CharField(max_length=10, null=False)  # 所属系列
    proDesc = models.CharField(max_length=30, null=False)  # 商品简介
    proShopId = models.CharField(max_length=20, null=False)  # 所属商店编号
    proShopName = models.CharField(max_length=20, null=False)  # 所属商店名称
    proImg = ListField()
    proTime = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return models.Model.__str__(self)
