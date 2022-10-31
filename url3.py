#!/user/bin/python
# -*- coding: utf-8 -*-
# Python 中文编码
# 导入csv
import csv
import time  # 引入time模块

# 导入BeautifulSoup和requests模块
from bs4 import BeautifulSoup
import requests
from reptile import Reptile
from myHtmlParser import MyHtmlParser


# ➜  studyPython git: (master) ✗ python3 ./url3.py(1s)[21:08:48]
# [ < a href = "/archive" > Archive < /a > , < a href = "https://what-if.xkcd.com" > What If?< /a > , < a href = "https://blag.xkcd.com" > Blag < /a > , < a href = "/about" rel = "author" > About < /a > , < a href = "/atom.xml" > Feed < /a >
# url = 'https://xkcd.com/353/'

# ➜  studyPython git: (master) ✗ python3 ./url3.py(0s)[21:08:40]
# [ < a href = "http://www.sina.com.cn/" > 新浪首页 < /a > , < a href = "http://news.sina.com.cn/" > 新闻 < /a > , < a href = "http://sports.sina.com.cn/" > 体育 < /a > , < a href = "http://finance.sina.com.cn/" > 财经 < /a >
# url = 'http://news.sina.com.cn/china/'

# 目标站点
urlTarget = 'https://www.cnipa.gov.cn/'

# 存放还没访问的url
url_set_not_visit = set()

# 存放已访问的url
url_set_visited = set()

# 存放已访问的url字典映射，关联父url
url_map_parent = {}


def check_dead_links(reptile, html_parser, target_url_seed_set, protocol, host, port, headers):
    global url_set_not_visit
    global url_set_visited

    # print(reptile, html_parser, target_url_seed_set, protocol, host, port, headers)
    # exit()
    
    # 原页面, 默认首页
    origin_page = ''
    
    while (target_url_seed_set):
        for url_path in target_url_seed_set:
            # 下载页面
            page = reptile.get_page(protocol, host, port, url_path, headers, url_map_parent)

            # 解析网页
            html_parser.feed(str(page))

            # 获取页面url
            url_set_on_page = html_parser.get_url_set_on_page()
            # print(url_path, url_set_on_page)
            # # exit()

            #exclusion = "mod=login|card.php|archiver|mod=viewthread|[.]css|[.]js|[.]gif|.jpg|about[.]php|panel[.]php|[.]swf|search[.]php"
            exclusion = '[.]xlsx'
            include = ''

            # 获取种子url
            target_url_seed_set_tmp = reptile.get_target_url_seed_set(url_set_on_page, include, exclusion)
            # print(url_path, target_url_seed_set_tmp)
            # exit()
            
            # 构建映射
            for urlTarget in target_url_seed_set_tmp:
                url_map_parent[urlTarget] = url_path
            
            # print(url_path, url_map_parent)
            # exit()
            
            url_set_not_visit = url_set_not_visit | target_url_seed_set_tmp

        url_set_visited = url_set_visited | target_url_seed_set
        target_url_seed_set = url_set_not_visit - url_set_visited
        

# 获取字符串格式的html_doc。由于content为bytes类型，故需要decode()
# html_doc = requests.get('https://xkcd.com/353/').content.decode()
# 加 headers
# headers = {'user-agent': 'my-app/0.0.1'}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'}

# url = 'http://www.adjyc.com'

# 获取状态码
def getHttpStatusCode(url):
    global headers
    try:
        request = requests.get(url, headers=headers, verify=False)
        httpStatusCode = request.status_code
        return httpStatusCode
    except requests.exceptions.HTTPError as e:
        # pass
        return e
        # return '443'

print('正则构造html解析器')
html_parser = MyHtmlParser()

print('正则检测死链')
reptile = Reptile()
# check_dead_links(reptile, html_parser, set(urlTarget), 'http', 'www.cnipa.gov.cn', '80', headers)
check_dead_links(reptile, html_parser, {urlTarget}, 'http', 'www.cnipa.gov.cn', '80', headers)

# 释放资源
reptile.closefile()
