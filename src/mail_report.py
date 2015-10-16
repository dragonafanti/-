#coding=utf-8
'''
自动发送邮件

@author: wanglong
'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time,base64

# class Mail():
def send_mail(file_new):
    #发信邮箱
#     mail_from='303546578@qq.com'
    mail_from='zentao_tjrd@163.com'
    #收信邮箱
    mail_to='wanglong@travelsky.com'
    
    mail_usr = 'zentao_tjrd@163.com'
    mail_pwd = 'ulivxulhsqfznyft'
#     mail_usr = '303546578@qq.com'
#     mail_pwd = '303546578mammoth'
#     post = "smtp.qq.com"
    post = "smtp.163.com"
    #定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    #定义标题
    msg['Subject']=u"自动化测试报告"
    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp=smtplib.SMTP()
    #连接SMTP 服务器，此处用的126 的SMTP 服务器
    smtp.connect(post)
    #用户名密码
    smtp.login(mail_usr,mail_pwd)
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print 'email has send out !'