#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'shouke'

from html.parser import HTMLParser

class MyHtmlParser(HTMLParser):
    '''HTML解析器'''

    def reset(self):
        HTMLParser.reset(self)
        self.url_set_on_page = set() # 存储访问url时，返回页面上的携带的url_path

    def handle_starttag(self, tag, attrs):
        url_list = [value for key, value in attrs if "href" == key or "include-path"==key or "src"==key]
        if url_list:
            for url in url_list:
                self.url_set_on_page.add(url)

    def get_url_set_on_page(self):
        return self.url_set_on_page

