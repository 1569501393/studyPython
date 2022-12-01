#!/user/bin/python
# -*- coding: utf-8 -*-
# Python 中文编码

# 导入BeautifulSoup和requests模块
from bs4 import BeautifulSoup
import requests

# str = '<p>Back to the <a rel="index">homepage hello world < br > 办事指南</a></p>'
str = '<a class="dys_addLink" href="http://www.gov.cn/zhuanti/zggcddescqgdbdh/index.htm" target="_blank"> <img class="shouji10" src="http://www.gov.cn/govweb/xhtml/2019zhuanti/20thCPCNationalCongress/images/20221027xxgcdesdjsclickin.png"/><img class="shouji11" src="http://ysp.www.gov.cn/013582404bd78ad3c016b8fffefe6a9a/top20meeting.jpg"/></a>'
rel_soup = BeautifulSoup(str)
# rel_soup = BeautifulSoup('< a target="_blank" title="集成电路布图设计登记审批办事指南" href="/attach/0/d4b9c91154c041a49e7ad653bbfa0cc2.pdf" > <img src="/picture/0/2006101457034528487.png" alt="" > 集成电路布图设计登记审批 < br > 办事指南 < /a >')


# rel_soup.a['rel']
# ['index']
# rel_soup.a['rel'] = ['index', 'contents']
print("rel_soup.p==")
print(rel_soup.p)
print("内容==")
print(rel_soup.a.contents)
# print(type(rel_soup.a.contents),  ''.join(rel_soup.a.contents))




a =1
print(type(a))

exit()
# <p>Back to the <a rel="index contents">homepage</a></p>


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
link = soup.find('a').contents
print(link)
