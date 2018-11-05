# coding:utf-8
'''
@Created on :2018-11-03
@function:写需要异步进行的任务
@author: jxc
'''
import smtplib
from email.mime.text import MIMEText

'''
 邮件类
'''

class Mailer():
    def __init__(self):
        self.server = "smtp.139.com"  # 设置服务器
        self.user = "jxc516@139.com"  # 用户名
        self.pwd = "jxc13572468"  # 口令
        self.default_from = '易图表 <' + self.user + '>'  # 默认发件人
        self.subject = '默认主题'  # 默认主题
        self.content = '默认内容'  # 默认内容
        self.subtype = 'plain'  # 默认发送类型
        self.charset = 'utf-8'  # 默认编码
        self.debug = False  # 默认关闭调式模式
        self.ssl = True  # 默认安全连接

    # 发送邮件
    def send_mail(self, to_list):
        msg = MIMEText(self.content, self.subtype, self.charset)
        msg['Subject'] = self.subject
        msg['From'] = self.default_from
        msg['To'] = to_list
        try:
            if self.ssl:
                smtp = smtplib.SMTP_SSL(self.server, 465)
            else:
                smtp = smtplib.SMTP(self.server, 25)
            if self.debug:
                smtp.set_debuglevel(1)
            smtp.login(self.user, self.pwd)
            smtp.sendmail(self.default_from, [to_list], msg.as_string())
            smtp.close()
            return True
        except Exception as e:
            print(str(e))
            return False
