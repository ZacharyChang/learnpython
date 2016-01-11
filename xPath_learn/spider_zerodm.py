# -*-coding:utf8-*-
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests


def spider(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    content_field = selector.xpath('//dl[@class="l-list mt10 oh"]/dd/ul/li')
    item = {}
    for each in content_field:
        name = each.xpath('a[@class="zerowzlh"]/@title')[0]
        url = each.xpath('a[@class="zerowzlh"]/@href')[0]
        episod = each.xpath('div[@class="dhp"]/span[@class="set"]/text()')[0]
        type = each.xpath('p[1]/text()')[0]
        click = each.xpath('p[2]/text()')[0]

        item['name'] = name
        item['url'] = 'http://dmxz.zerodm.com' + url
        item['episod'] = episod
        item['type'] = type[3:]
        item['click'] = click[3:-1]

        towrite(item)


def towrite(contentdict):
    f.writelines(u'名称: ' + str(contentdict['name']) + '\n')
    f.writelines(u'地址: ' + str(contentdict['url']) + '\n')
    f.writelines(u'集数: ' + str(contentdict['episod']) + '\n')
    f.writelines(u'类别: ' + str(contentdict['type']) + '\n')
    f.writelines(u'点击: ' + str(contentdict['click']) + '\n')
    f.writelines('\n')


if __name__ == '__main__':
    pool = ThreadPool(4)
    f = open('zerodm.txt', 'a', encoding='utf-8')
    page = []
    for i in range(0, 81):
        newpage = 'http://dmxz.zerodm.com/list/1/' + str(i)
        print("添加 " + newpage + " 中...")
        page.append(newpage)

    results = pool.map(spider, page)
    pool.close()
    pool.join()
    f.close()
