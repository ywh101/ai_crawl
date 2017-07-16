# coding: utf8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import getpass
import os



class email_To(object):
    def __init__(self):
        pass

    def emailto(self, filename):
        sender = 'ywh101936@hotmail.com'
        receivers = input('请输入你要接收邮件的邮箱：')
        smtp_server = 'smtp-mail.outlook.com'

        username = input('请输入你要发送邮件的邮箱用户名：')
        password = getpass.getpass("请输入密码：")

        path = os.getcwd()
        path = os.path.join(path, 'text')
        F = open('%s/%s'%(path, filename))
        # f = str(F.readlines())

        msg = MIMEMultipart()
        msgbody = MIMEText('见附件', 'plain', 'utf-8')
        msg['To'] = formataddr(["收件人邮箱呢称：", receivers])
        msg['Subject'] = Header("Pythoh test email!", 'utf-8')
        msg.attach(msgbody)

        att1 = MIMEText(F.read(), 'base64', 'utf-8')
        att1['Content-Type'] = 'application/octet-stream'
        att1['Content-Disposition'] = 'attachment; filename = "test.txt"'
        msg.attach(att1)

        F.close()

        try:
            smtp = smtplib.SMTP(smtp_server)
            smtp.starttls()
            smtp.login(username, password)
            smtp.sendmail(sender, receivers, msg.as_string())
            smtp.quit()
            print("Emailing is OK!")
        except Exception as e:
            print(e)