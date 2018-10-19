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

    # 添加记录
    def add(self, obj):
        try:
            obj.save()
            return True
        except Exception as e:
            print(e)
            return False

    # 查询记录
    def select(self, args, connect_type, order_by):
        if args:
            if isinstance(args, dict):
                q = Q()  # 创建Q对象
                if connect_type:
                    q.connector = connect_type
                for k, v in args.items():
                    q.children.append((k, v))  # 组合查询条件
                try:
                    data = self.model.objects.filter(q).order_by(order_by)
                    if len(data) == 1:  # 只有一条数据时
                        return data[0]
                    return data
                except Exception as e:
                    print(e)
                    return None
            raise TypeError('请输入一个字典参数,如{"id":id}')
        raise TypeError('Invild argument:', args)
