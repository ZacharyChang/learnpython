# -*-coding:utf8-*--
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
html = requests.get('http://dmxz.zerodm.com/', headers=headers)
html.encoding = 'utf-8'

title = re.findall('target="_blank">(.*?)</a>', html.text, re.S)
# title=re.findall('<p id="name"><a href="([\s\S]*)" title="(.*?)" target="_blank">',html.text,re.S)
for each in title:
    print(each)
