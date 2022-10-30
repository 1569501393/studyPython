#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'shouke'

import gzip, re
from io import BytesIO
from urllib.request import *
import re
import chardet

# 爬虫类
class Reptile:
    """to download web pages"""

    def __init__(self, filepath_of_urls_visited="d:/filepath_of_urls_visited.txt", filepath_of_urls_in_trouble="d:/filepath_of_urls_in_trouble.txt"):
        self.url_set_visited = set()      # 用于存储已下载过的页面url
        self.filepath_of_urls_visited = filepath_of_urls_visited  # 用于存储已下载过的页面url
        self.filepath_of_urls_in_trouble  = filepath_of_urls_in_trouble  # 用于存储访问出问题的页面url
        self.data = "" # 存放访问url，返回的web页面数据
        self.file = open(self.filepath_of_urls_visited, 'w')
        self.file2 = open(self.filepath_of_urls_in_trouble, 'w')
        self.page_visited_num = 0 # 访问页面计数器

    def get_page(self, protocol, host, port, url_path, headers):
        if not url_path.startswith("http://") and not url_path.startswith("https://"):
            url = protocol + '://' + host + ':' + port + url_path
        else:
            url = url_path
        request = Request(url, headers=headers)
        request.add_header('Accept-encoding', 'gzip') #下载经过gzip方式压缩后的网页，减少网络流量

        try:
            print('正在访问第 %s 个链接:\n %s' % (self.page_visited_num, url))
            response = urlopen(request) # 发送请求报文
            self.page_visited_num = self.page_visited_num + 1

            if response.code == 200: # 请求成功
                print('访问成功。', end=' ')
                # 存储已成功访问的页面url
                self.file.write('URL：' + url)
                self.file.write('\n')
                self.file.flush()
                page = response.read() # 读取经压缩后的页面
                if response.info().get("Content-Encoding") ==  "gzip":
                    page_data = BytesIO(page)
                    gzipper = gzip.GzipFile(fileobj = page_data)
                    self.data = gzipper.read()
                else:
                    #page_data = BytesIO(page)
                    #self.data = page #page_data  # 网页未采用gzip方式压缩，使用原页面
                    page_data = BytesIO(page)
                    self.data = page_data  # 网页未采用gzip方式压缩，使用原页面

                encoding = chardet.detect(self.data)['encoding']
                # print('正在对服务器返回body进行解码')

                if encoding:
                    if  encoding.lower() in ('gb2312', 'windows-1252', 'iso-8859-2', 'iso-8859-1'):
                        self.data = self.data.decode('gbk')  # decode函数对获取的字节数据进行解码
                    elif encoding.lower() in('utf-8', 'utf-8-sig'):
                        self.data = self.data.decode('utf-8')
                    elif encoding.lower() == 'ascii':
                        self.data = self.data.decode('unicode_escape')
                    else:
                        print('解码失败，未知编码:%s，不对body做任何解码' % encoding)
                        pass
                result = re.findall("<title>(.+?)</title>", str(self.data))
                if result:
                    title = result[0]
                else:
                    title = '页面标题为空'
                print('页面标题为：%s\n' % title)
            else:
                print('访问链接 %s 失败' % url)
                # 存储未成功访问的页面url
                self.file2.write(url)
                self.file2.write('\n')
                self.file2.flush()
        except Exception as e:
            pass
            print('解析页面出错\n')
            # self.file2.write("解析出错：" + url)
            # self.file2.write('\n')
            # self.file2.flush()

        # 存储已经访问url的url_path
        self.url_set_visited.add(url_path)

        return self.data

    # 获取种子URL
    def get_target_url_seed_set(self, url_set, include, exclusion):
        url_seed_set = set() # 存放相同服务器下的url
        target_url_seed_set = set() # 存放目标的url


        # # 过滤不属于当前服务器下的url
        # while len(url_set) != 0:
        #     url = url_set.pop()
        #     if not url.startswith('http://') and not url.startswith('https://') and url.startswith('/'):
        #         url_seed_set.add(url)

        while len(url_set) != 0:
            url = url_set.pop()
            if url.startswith('http://') or url.startswith('https://') or url.startswith('/'):
                url_seed_set.add(url)

        # 进一步过滤不想要的url
        if exclusion != "":
            exclusive = re.compile(exclusion)
            while len(url_seed_set) != 0:
                url = url_seed_set.pop()
                if re.findall(exclusive, url) == []:
                    target_url_seed_set.add(url)
        else:
            target_url_seed_set = url_seed_set

        #过滤掉已经抓取过的url
        target_url_seed_set = target_url_seed_set - self.url_set_visited

        return target_url_seed_set

    # 关闭文件
    def closefile(self):
        self.file.close()