import requests

cook = {
    # Cookie got from fiddler
    'Cookie': ''}
url = "https://www.zhihu.com/"
html = requests.get(url, cookies=cook).content
# html = bytes(bytearray(requests.get(url, cookies=cook).text, encoding='utf-8'))
print(html.decode())
