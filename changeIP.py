import os
import random
import time
import requests

g_adsl_account = {"name" : "宽带连接名称","username" : "上网账户的用户名","password" : "用户名对应的密码"}
class Adsl(object):
    def __init__(self):
        self.name = g_adsl_account["name"]
        self.username = g_adsl_account["username"]
        self.password = g_adsl_account["password"]

    def connect(self):
        cmd_str = "rasdial %s %s %s" % (self.name,self.username,self.password)
        os.system(cmd_str)
        time.sleep(5)

    def disconnect(self):
        cmd_str = "rasdial %s /disconnect" % self.name
        os.system(cmd_str)
        time.sleep(5)

    def reconnect(self):
        self.disconnect()
        self.connect()

if __name__ == '__main__':
    A = Adsl()
    A.reconnect()



----------------------------------------------------------------------------------------------------------------------------------
#配合changeIP.py进行结合爬虫更换IP
link = "www.×××.com"
headers = {'User-agent' : '自己的浏览器头'}
#定义最大尝试次数为三次
def scrapy(url,num_try = 3):
    try:
        r = requests.get(link,headers = headers)
        html = r.text
        time.sleep(random.randint(0,2)+random.random())
    except Exception as e:
        print(e)
        html = None
        if num_try > 0:
            x = changeIP.adsl()
            x.reconnect()
            html = scrapy(url,num_try-1)
    return html
result = scrapy(link)
