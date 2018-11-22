# from django.contrib import admin
import xadmin as admin
# from django.contrib import admin
# Register your models here.
from Inform.models import email_vertify, Message, MessageText

# 邮箱验证管理
class EmailVertifyAdmin(object):
    list_display = ('id', 'email', 'code', 'send_time',
                    'vertify_type', 'is_live')
    list_filter = ('email', 'vertify_type', 'is_live')
    search_fields = ('email', 'vertify_type', 'is_live')
    ordering = ('send_time',)
    filter_horizontal = ()

#
class MessageAdmin(object):
    list_display = ('messageId', 'recieveId', 'sendId',
                    'messageText', 'replyed_messageId', 'msgStatue')
    list_filter = ('recieveId', 'sendId', 'msgStatue')
    search_fields = ('recieveId', 'sendId')
    ordering = ('messageId',)
    filter_horizontal = ()

class MessageTextAdmin(object):
    list_display = ('msgId', 'msgType', 'msgContent', 'msgTime')
    list_filter = ('msgType', 'msgContent', 'msgTime')
    search_fields = ('msgType', 'msgContent')
    ordering = ('msgTime',)
    filter_horizontal = ()


admin.site.register(email_vertify, EmailVertifyAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(MessageText, MessageTextAdmin)
