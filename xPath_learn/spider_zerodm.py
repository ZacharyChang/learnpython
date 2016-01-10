# -*-coding:utf8-*-
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import json


def spider(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    content_field = selector.xpath('//dl[@class="l-list mt10 oh"]/dd/ul/li')
    item = {}
    for each in content_field:
        name = each.xpath('a[@class="zerowzlh"]/text()')
        print(name)
        # author = reply_info['author']['user_name']
        # content = \
        #     each.xpath(
        #             'div[@class="d_post_content_main"]/div/cc/div[@class="d_post_content j_d_post_content  clearfix"]/text()')[
        #         0]
        # reply_time = reply_info['content']['date']
        # print(content)
        # print(reply_time)
        # print(author)
        item['name'] = name
        # item['topic_reply_content'] = content
        # item['topic_reply_time'] = reply_time
        towrite(item)


def towrite(contentdict):
    f.writelines(u'名称:' + str(contentdict['name']) + '\n')


#     f.writelines(u'类别:' + str(contentdict['topic_reply_content']) + '\n')
#     f.writelines(u'点击:' + contentdict['user_name'] + '\n\n')

if __name__ == '__main__':
    pool = ThreadPool(4)
    f = open('zerodm.txt', 'a', encoding='utf-8')
    page = []
    for i in range(0, 20):
        newpage = 'http://dmxz.zerodm.com/list/wanjie/' + str(i)
        print("处理 " + newpage + " 中...")
        page.append(newpage)

    results = pool.map(spider, page)
    pool.close()
    pool.join()
    f.close()
