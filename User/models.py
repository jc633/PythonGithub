# coding:utf-8
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from CommonUtils.stringUtils import stringUtil
from celery.worker.strategy import default

# Create your models here.
# 用户类,继承自AbstractUser,扩展原有字段

stringutil = stringUtil()

class UserManager(BaseUserManager):
    def create_user(self, id, email, uName, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=UserManager.normalize_email(email),
            id=id,
            uName=uName,
            is_superuser=False,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, id, uName, password):
        user = self.create_user(
            id=id,
            email=email,
            uName=uName,
            password=password,
        )
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class user(AbstractBaseUser, PermissionsMixin):

    id = models.CharField(primary_key=True, max_length=6,
                          null=False, verbose_name='编号')  # 用户id
#     is_Active = models.BooleanField()  # 是否激活
    objects = UserManager()
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    uName = models.CharField(max_length=20, null=False,
                             verbose_name='昵称')  # 用户名
#     uPhone = models.CharField(max_length=15, null=True)  # 电话
    email = models.EmailField(unique=True, verbose_name='邮箱')  # 邮箱
    email_active = models.BooleanField(
        default=False, verbose_name='邮箱激活')  # 邮箱是否激活
    uSex = models.CharField(max_length=4, null=True, verbose_name='性别')  # 性别
    uImg = models.ImageField(upload_to='img/user/',  # 头像
                             default='img/user/default_user.png', verbose_name='头像')
    uTime = models.IntegerField(null=True, verbose_name='注册时间')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['id', 'uName']

    class Meta:
        db_table = 'user'
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'

    def __str__(self):
        return AbstractBaseUser.__str__(self)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser

    def set_password(self, raw_password):
        return AbstractBaseUser.set_password(self, raw_password)

    def check_password(self, raw_password):
        return AbstractBaseUser.check_password(self, raw_password)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
