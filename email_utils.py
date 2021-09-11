# -*- coding: utf-8 -*-
# @Time   : 2021/3/7
# @Author : lorineluo 
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import parseaddr, formataddr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def timeStr():
    t = time.strftime(str("%Y-%m-%d %H:%M:%S"), time.localtime())
    s = '[%s]' % t
    return s

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def sendEmail(msg, sender, title):
    # send email
    from_addr = 'luoyu091@163.com'
    tok = 'ZIVRTJYTZTGODWUX'
    to_addr = ['381336925@qq.com', 'moonwalkings@vip.qq.com', '1015240649@qq.com']
    # to_addr = ['381336925@qq.com']
    smtp_server = 'smtp.163.com'
    stime = timeStr()  

    msg['From'] = _format_addr('%s <%s>' % (sender, from_addr))
    msg['To'] = ",".join(to_addr) 
    msg['Subject'] = Header('%s %s' % (title, stime), 'utf-8').encode()

    server = smtplib.SMTP_SSL(smtp_server, 465)
    # server.set_debuglevel(1)
    server.ehlo(smtp_server)
    server.login(from_addr, tok)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()

if __name__ == '__main__':
    msg = MIMEMultipart('mixed')

    # 1. dataframe
    display_df = pd.DataFrame(
        np.array([[1.0, '20210815', 3], [4.8, '20210816', 6], [7.0, '20210817', 9]]), 
        columns=['a', 'date', 'c'])
    print(display_df)
    # display_df['a'] = display_df['a'].apply(lambda x: format(x, ".2%"))
    display_df = display_df.round(3)
    ori_html = display_df.to_html()

    #set table style
    ori_html = ori_html.replace("<table", '<table style="border-collapse: collapse;"')

    # 可能有多个内容
    contents = [ori_html]

    for content in contents:
        context = MIMEText(content,_subtype='html', _charset='utf-8')
        msg.attach(context)

    # 2. 图
    x=list(range(display_df.index.size))
    name = 'test'
    # plt.legend(loc="upper left", bbox_to_anchor=(0, 0.85))
    plt.xticks(x, display_df.date, rotation=35)
    plt.title(name)
    plt.savefig("%s/%s.png" %("/tmp", name))
    
    items=[name]
    content = '<p> </p>'
    for item in  items:
        content += '<p> <img src="cid:%s" height="300" width="800"></p>' %item
        # 读图
        with open("%s/%s.png" %('/tmp', item), "rb") as f:
            img = MIMEImage(f.read())
            img.add_header('Content-ID', item) 
            msg.attach(img)
    context = MIMEText(content,_subtype='html', _charset='utf-8')
    msg.attach(context)

    #发送
    sendEmail(msg, "email test", "email test")
