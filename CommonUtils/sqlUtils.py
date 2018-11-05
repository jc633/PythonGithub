# coding:utf-8
'''
@Created on :2018-10-18
@function:定义sql操作类
@author: jxc
'''
from django.db.models import Q

class sqlUtil():
    def __init__(self, model):
        self.model = model
        self.order_by = None

    # 添加记录
    def add(self, obj):
        try:
            obj.save()
            return True
        except Exception as e:
            print(e)
            return False

    # 查询记录
    def select(self, args, **kwargs):
        if args:
            if isinstance(args, dict):
                q = Q()  # 创建Q对象
                if 'connect_type' in kwargs:
                    q.connector = kwargs['connect_type']
                if 'order_by' in kwargs:
                    self.order_by = kwargs['order_by']
                for k, v in args.items():
                    q.children.append((k, v))  # 组合查询条件
                try:
                    data = self.model.objects.filter(q).order_by(self.order_by)
                    return data
                except Exception as e:
                    print(e)
                    return None
            raise TypeError('请输入一个字典参数,如{"id":id}')
        return self.model.objects.all()
