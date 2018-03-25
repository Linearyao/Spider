#coding:utf-8
import requests
from lxml import etree

link = "http://nebula-storm.blogchina.com/archive/201803_1.html"
headers = {'User-agent':'headers'}
r = requests.get(link,headers = headers)
html = etree.HTML(r.text)
title_list = html.xpath('//h3[@class="qrcode-bd3"]/a/text()')
