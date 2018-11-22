# coding:utf-8
from django.db import models


# Create your models here.

# 邮箱验证
class email_vertify(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='序号')  # 自增列
    email = models.EmailField(verbose_name='邮箱')  # 验证邮箱
    code = models.CharField(max_length=10, verbose_name='验证码')  # 验证码
    send_time = models.IntegerField(
        null=False, verbose_name='发送时间')  # 发送验证时间(存储时间戳)
    vertify_type = models.CharField(
        max_length=10, verbose_name='验证类型')  # 验证类型(激活账户\重置密码)
    is_live = models.BooleanField(verbose_name='是否失效')  # 是否有效

    class Meta:
        db_table = 'email_vertify'
        verbose_name = '邮箱验证'
        verbose_name_plural = '邮箱验证'


# 站内消息具体内容
class MessageText(models.Model):
    msgId = models.CharField(
        primary_key=True, max_length=8, verbose_name='内容编号')
    msgType = models.CharField(max_length=10, verbose_name='消息类型')  # 消息类型
    msgContent = models.CharField(max_length=200, verbose_name='具体内容')  # 消息内容
    msgTime = models.CharField(max_length=20, verbose_name='发送时间')  # 发送时间

    class Meta:
        db_table = 'messageText'
        verbose_name = '消息内容'
        verbose_name_plural = '消息内容'

    def __str__(self):
        return models.Model.__str__(self)

# 站内消息
class Message(models.Model):
    messageId = models.CharField(
        primary_key=True, max_length=8, verbose_name='消息编号')  # 消息编号
    recieveId = models.CharField(
        max_length=6, null=True, verbose_name='接收者编号')  # 接受者id
    sendId = models.CharField(max_length=6, verbose_name='发送者编号')  # 发送者id
    messageText = models.ForeignKey(
        to='MessageText', to_field='msgId', on_delete=models.CASCADE, related_name='message', verbose_name='内容对象')  # 消息内容编号
    replyed_messageId = models.CharField(
        max_length=8, null=True, verbose_name='回复对象')  # 回复的消息编号(即指明回复的是哪一条评论)
    msgStatue = models.BooleanField(verbose_name='状态')  # 消息状态 0:未读 1:已读

    class Meta:
        db_table = 'message'
        verbose_name = '站内消息'
        verbose_name_plural = '站内消息'

    def __str__(self):
        return models.Model.__str__(self)
