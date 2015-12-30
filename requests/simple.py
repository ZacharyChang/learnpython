#-*-coding:utf8-*--
import requests

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
html=requests.get('http://www.gamersky.com/',headers=headers)
print(html.text)
