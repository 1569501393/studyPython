#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'shouke'

import urllib.parse

from conf.initconf import InitConfig
from myHtmlParser import MyHtmlParser
from reptile import Reptile
from httpProtocol import MyHttp


url_set_not_visit = set() # 存放还没访问的url
url_set_visited = set() # 存放已访问的url
def check_dead_links(reptile, html_parser, target_url_seed_set, protocol, host, port, headers):
    global url_set_not_visit
    global url_set_visited

    while(target_url_seed_set):
        for url_path in target_url_seed_set:
             # 下载页面
            page = reptile.get_page(protocol, host, port, url_path, headers)

            # 解析网页
            html_parser.feed(str(page))

            # 获取页面url
            url_set_on_page = html_parser.get_url_set_on_page()

            #exclusion = "mod=login|card.php|archiver|mod=viewthread|[.]css|[.]js|[.]gif|.jpg|about[.]php|panel[.]php|[.]swf|search[.]php"
            exclusion = '[.]xlsx'
            include = ''

            # 获取种子url
            target_url_seed_set_tmp = reptile.get_target_url_seed_set(url_set_on_page, include, exclusion)

            url_set_not_visit = url_set_not_visit | target_url_seed_set_tmp

        url_set_visited = url_set_visited | target_url_seed_set
        target_url_seed_set = url_set_not_visit - url_set_visited

def login_system(username, password):
    myhttp.get('/res/rpatchca.png?','0.7627999931392293')
    data = {"userName":username,"userPwd":password,
         "captcha":"5555","channelType":"dt"}
    data = urllib.parse.urlencode(data)
    data= data.encode('utf-8')
    login_result = myhttp.post('/auth/login', data)
    if not login_result[0]:
        print('登录失败')
        exit()

if __name__ == '__main__':
    print('正在读取初始化配置')
    init_conf = InitConfig('./conf/init.conf')

    protocol = init_conf.get_protcol()
    host = init_conf.get_host()
    port = init_conf.get_port()
    init_url_paths_nologin = set() # 不用登陆即可访问的初始url集合
    init_url_paths_login = set() # 需要登陆才可访问的初始url集合

    with open('./conf/urlNoLogin.txt', 'r') as f:
        line = f.readline()
        while line:
            line = line.strip(' ')
            line = line.rstrip('\n')
            init_url_paths_nologin.add(line)
            line = f.readline()

    with open('./conf/urlNeedLogin.txt', 'r') as f:
        line = f.readline()
        while line:
            line = line.strip(' ')
            line = line.rstrip('\n')
            init_url_paths_login.add(line)
            line = f.readline()

    # 添加头域，伪装浏览器访问网站,防止一些网站拒绝爬虫访问
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0"}

    print('正则构造html解析器')
    html_parser = MyHtmlParser(strict = False)

    reptile = Reptile()
    print('正则检测死链')
    check_dead_links(reptile, html_parser, init_url_paths_nologin, protocol, host, port, headers)

    myhttp = MyHttp(protocol, host, port)

    print('正在登录系统')
    username = init_conf.get_username()
    password = init_conf.get_password()
    login_system(username, password)

    print('正则检测死链')
    check_dead_links(reptile, html_parser, init_url_paths_login, protocol, host, port, headers)


    # 释放资源
    reptile.closefile()