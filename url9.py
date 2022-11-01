#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'jieqiang'

import gzip
import re
from io import BytesIO
import time  # 引入time模块
# from urllib.request import *
# from urllib import *
import urllib.request
import urllib.error

import chardet
# import requests


# 爬虫类


class Reptile:
    """to download web pages"""

    def __init__(self, filepath_of_urls_visited="./storage/" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + "_filepath_of_urls_visited.csv", filepath_of_urls_in_trouble="./storage/" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + "_filepath_of_urls_in_trouble.csv", filepath_of_urls_result="./storage/" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + "_filepath_of_urls_result.csv"):
        self.url_set_visited = set()      # 用于存储已下载过的页面url
        self.filepath_of_urls_visited = filepath_of_urls_visited  # 用于存储已下载过的页面url
        self.filepath_of_urls_in_trouble = filepath_of_urls_in_trouble  # 用于存储访问出问题的页面url
        self.filepath_of_urls_result = filepath_of_urls_result  # 用于存储访问结果
        self.data = ""  # 存放访问url，返回的web页面数据
        self.file = open(self.filepath_of_urls_visited, 'w')
        self.file2 = open(self.filepath_of_urls_in_trouble, 'w')
        self.file3 = open(self.filepath_of_urls_result, 'w')
        # 写入头
        # self.file3.write("'link', 'text', 'page_where_found', 'server_response'")
        self.file3.write("link, text, page_where_found, server_response \n")
        self.file3.flush()

        self.page_visited_num = 0  # 访问页面计数器

    def get_page(self, protocol, host, port, url_path, headers, url_map_parent={}):
        if not url_path.startswith("http://") and not url_path.startswith("https://"):
            url = protocol + '://' + host + ':' + port + url_path
        else:
            url = url_path
        request = urllib.request.Request(url, headers=headers)
        request.add_header('Accept-encoding', 'gzip')  # 下载经过gzip方式压缩后的网页，减少网络流量

        # 定义 title
        title = ''
        status_code = 0
        
        try:
            print('%s, 正在访问第 %s 个链接:\n %s' % (time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()), self.page_visited_num, url))

            # response = urlopen(request)  # 发送请求报文
            response = urllib.request.urlopen(request)  # 发送请求报文
            # status_code = response.code
            status_code = response.getcode()
            
            # 存储已成功访问的页面url
            self.file.write('%s, 正在访问第 %s 个链接: code: %s \n %s' % (time.strftime(
                "%Y-%m-%d-%H-%M-%S", time.localtime()), self.page_visited_num, status_code, url))
            self.file.flush()
            
            self.page_visited_num = self.page_visited_num + 1

            if status_code == 200:  # 请求成功
                print('访问成功。', end=' ')
                page = response.read()  # 读取经压缩后的页面
                if response.info().get("Content-Encoding") == "gzip":
                    page_data = BytesIO(page)
                    gzipper = gzip.GzipFile(fileobj=page_data)
                    self.data = gzipper.read()
                else:
                    #page_data = BytesIO(page)
                    # self.data = page #page_data  # 网页未采用gzip方式压缩，使用原页面
                    page_data = BytesIO(page)
                    self.data = page_data  # 网页未采用gzip方式压缩，使用原页面

                # encoding = chardet.detect(self.data)['encoding']
                encoding = chardet.detect(self.data)['encoding']
                # print('正在对服务器返回body进行解码')

                if encoding:
                    if encoding.lower() in ('gb2312', 'windows-1252', 'iso-8859-2', 'iso-8859-1'):
                        self.data = self.data.decode('gbk')  # decode函数对获取的字节数据进行解码
                    elif encoding.lower() in ('utf-8', 'utf-8-sig'):
                        self.data = self.data.decode('utf-8')
                    elif encoding.lower() == 'ascii':
                        self.data = self.data.decode('unicode_escape')
                    else:
                        print('解码失败，未知编码:%s，不对body做任何解码' % encoding)
                        # 存储已成功访问的页面url
                        self.file.write('URL：' + url + ' 解码失败，未知编码:%s，不对body做任何解码' % encoding)
                        self.file.write('\n')
                        self.file.flush()
                        pass
                result = re.findall("<title>(.+?)</title>", str(self.data))
                if result:
                    title = result[0]
                else:
                    title = '页面标题为空'
                    # 存储已成功访问的页面url
                    self.file.write('URL：' + url + ' 页面标题为空')
                    self.file.write('\n')
                    self.file.flush()

                print('页面标题为：%s\n' % title)
            else:
                print('访问链接 %s 失败' % url)
                # 存储已成功访问的页面url
                self.file.write('URL：' + url + ' 访问链接 %s 失败' % url)
                self.file.write('\n')
                self.file.flush()
        # except Exception as e:
        except urllib.error.HTTPError as e:
        # except request as e:
            pass

            self.page_visited_num = self.page_visited_num + 1
            status_code = e.code
            # print("111")
            # print(str(e))
            # exit()
            print('解析页面出错\n')
            # 存储已成功访问的页面url
            self.file.write('URL：' + url + ' 解析页面出错')
            self.file.write('\n')
            self.file.flush()

        # 存储已经访问url的url_path
        self.url_set_visited.add(url_path)

        # 写入内容
        self.file3.write(
            url +
            ", " +
            title +
            ", " +
            str(url_map_parent.get(url_path)) +
            ", " +
            str(status_code) + " \n"
        )
        self.file3.flush()

        return self.data

    # 获取种子URL
    def get_target_url_seed_set(self, url_set, include, exclusion):
        url_seed_set = set()  # 存放相同服务器下的url
        target_url_seed_set = set()  # 存放目标的url

        # 过滤不属于当前服务器下的url
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

        # 过滤掉已经抓取过的url
        target_url_seed_set = target_url_seed_set - self.url_set_visited

        return target_url_seed_set

    # 关闭文件
    def closefile(self):
        self.file.close()
