#!/user/bin/python
# -*- coding: utf-8 -*-
# Python 中文编码
# 导入csv
import csv
import time  # 引入time模块

# 导入BeautifulSoup和requests模块
from bs4 import BeautifulSoup
import requests

# ➜  studyPython git: (master) ✗ python3 ./url3.py(1s)[21:09:44]
# []
# []
# url = 'http://baidu.com'

# ➜  studyPython git: (master) ✗ python3 ./url3.py(1s)[21:08:48]
# [ < a href = "/archive" > Archive < /a > , < a href = "https://what-if.xkcd.com" > What If?< /a > , < a href = "https://blag.xkcd.com" > Blag < /a > , < a href = "/about" rel = "author" > About < /a > , < a href = "/atom.xml" > Feed < /a >
# url = 'https://xkcd.com/353/'

# ➜  studyPython git: (master) ✗ python3 ./url3.py(0s)[21:08:40]
# [ < a href = "http://www.sina.com.cn/" > 新浪首页 < /a > , < a href = "http://news.sina.com.cn/" > 新闻 < /a > , < a href = "http://sports.sina.com.cn/" > 体育 < /a > , < a href = "http://finance.sina.com.cn/" > 财经 < /a >
# url = 'http://news.sina.com.cn/china/'

# 目标站点
url = 'https://www.cnipa.gov.cn/'

# url = 'http://www.adjyc.com'


# 获取字符串格式的html_doc。由于content为bytes类型，故需要decode()
# html_doc = requests.get('https://xkcd.com/353/').content.decode()
# 加 headers
# headers = {'user-agent': 'my-app/0.0.1'}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'}

html_doc = requests.get(url, headers=headers).content.decode()
# 使用BeautifulSoup模块对页面文件进行解析
soup = BeautifulSoup(html_doc, 'html.parser')
# print("soup==")
# print(soup)

# 查找所有tag为'a'的html元素，并生成列表
# links = soup.find_all('a')
links = soup.find_all('a')

# links = soup.find_all('a target')
print("links==")
print(links)

# 获取每个元素中'href'键对应的键值--即URL，并放入url_lst
url_lst = []

# todo 去重
# todo 递归

# time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
file_name = 'link_' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + '.csv'
with open(file_name, 'w', newline='') as csvfile:
    fieldnames = ['link', 'text', 'page_where_found', 'server_response']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in links:
        print("content==")
        print(item.contents)
        # print(''.join(item.contents))
        # 列表转字符串
        content_list = map(lambda x: str(x), item.contents)
        content_str = ''.join(content_list)
        print(content_str)

        url = item.get('href')
        print("url==")
        print(url)
        url_lst.append(url)
        # 写入 csv
        page_where_found = ''
        # todo curl
        server_response = 404
        writer.writerow({'link': url, 'text': content_str, 'page_where_found': page_where_found,
                        'server_response': server_response})

# 含有 None
# print(url_lst, filter(lambda url_str: 'http' in url_str, url_lst), list(filter(None, url_lst)))
# 过滤url_lst--仅保留包含http的URL

# 使用filter()函数，删除列表中的None值
# url_lst = list(filter(None, url_lst))

# # print(url_lst)
# # url_lst = list(filter(lambda url_str: 'http' in url_str, url_lst))
# url_lst = list(filter(lambda url_str: 'title' in url_str, url_lst))
# print("url_lst==")
# print(url_lst)
