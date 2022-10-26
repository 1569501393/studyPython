#!/user/bin/python
# -*- coding: utf-8 -*-
# Python 中文编码
def getAllUrl(self, url):
    import urllib.request
    from bs4 import BeautifulSoup
    html = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(html, features='html.parser')
    tags = soup.find_all('a')
    for tag in tags:
        print(str(tag.get('href')).strip())

getAllUrl("self", "http://baidu.com")
