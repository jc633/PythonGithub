# coding:utf-8
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
# Create your models here.
# 用户类,继承自AbstractUser,扩展原有字段

class user(AbstractBaseUser):
    uId = models.CharField(primary_key=True, max_length=6,
                           null=False, unique=True)  # 用户id
    is_Active = models.BooleanField()  # 是否激活
    uName = models.CharField(max_length=20, null=False)  # 用户名
    uPhone = models.CharField(max_length=15, null=False,)  # 电话
    uEmail = models.EmailField()  # 邮箱
    email_active = models.BooleanField(default=False)  # 邮箱是否激活
    uSex = models.CharField(max_length=4, null=True)  # 性别
    uImg = models.ImageField(upload_to='img/user/',  # 头像
                             default='img/user/default_user.png')
    uTime = models.CharField(max_length=20, null=True)
    USERNAME_FIELD = 'uId'

    class Meta:
        db_table = 'user'
        verbose_name = '用户信息'

    def __str__(self):
        return AbstractBaseUser.__str__(self)

# 邮箱验证
class email_vertify(models.Model):
    id = models.AutoField(primary_key=True)  # 自增列
    email = models.EmailField()  # 验证邮箱
    code = models.CharField(max_length=10)  # 验证码
    send_time = models.CharField(max_length=30)  # 发送验证时间(存储时间戳)
    vertify_type = models.CharField(max_length=10)  # 验证类型(激活账户\重置密码)
    is_live = models.BooleanField()  # 是否有效

    class Meta:
        db_table = 'email_vertify'
        verbose_name = '邮箱验证'
