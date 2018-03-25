#coding:utf-8
import requests
from bs4 import BeautifulSoup
import re

link = """http://nebula-storm.blogchina.com/archive/201803_1.html"""
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
r = requests.get(link,headers = headers)
soup = BeautifulSoup(r.text,"html.parser")
print(soup)
print(soup.select("div > a"))
print(soup.select("h3")) #查找所有h3标题的内容
for child in soup.header.div.children:
    print(child)
for tag in soup.find_all(re.compile("^h")):
    print(tag.name)
