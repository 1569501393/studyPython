#!/user/bin/python
# -*- coding: utf-8 -*-
# Python 中文编码
# 导入csv
import csv
import time  # 引入time模块

# 导入BeautifulSoup和requests模块
from bs4 import BeautifulSoup
import requests

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# 目标站点
urlHost = 'www.cnipa.gov.cn'
# urlTarget = 'https://www.cnipa.gov.cn/'

# 目标url
# urlTarget = 'https://' + urlHost + '/'
urlTarget = 'https://' + urlHost


# 存放还没访问的url
urlSetNotVisit = set()

# 存放已访问的url
urlSetVisited = set()

# 当前页url
urlSetOnPage = set()

# 存放已访问的url字典映射，关联父url
urlMapParent = {}

# 访问页面计数器
pageVisitedNum = 0

# 获取状态码


def getHttpStatusCode(url):
    try:
        request = getHttpRequest(url)
        httpStatusCode = request.status_code
        return httpStatusCode
    except requests.exceptions.HTTPError as e:
        return e

# 获取请求


def getHttpRequest(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'}
    try:
        return requests.get(url, headers=headers, verify=False)
    except requests.exceptions.HTTPError as e:
        return e


# 检测字符串是否url
def checkIsUrl(strx):
    return strx.startswith("http")

# 返回 url


def returnUrl(strx):
    if strx.startswith("http"):
        return strx
    else:
        return 'https://www.cnipa.gov.cn/' + strx


# 获取字符串格式的html_doc。由于content为bytes类型，故需要decode()
# html_doc = requests.get('https://xkcd.com/353/').content.decode()
# 加 headers
# headers = {'user-agent': 'my-app/0.0.1'}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'}

# html_doc = requests.get(url, headers=headers).content.decode()
# urlRequest = requests.get(urlTarget, headers=headers, verify=False)

''' htmlDoc = getHttpRequest(urlTarget).content.decode()
# 使用BeautifulSoup模块对页面文件进行解析
soup = BeautifulSoup(htmlDoc, 'html.parser')
# print("soup==")
# print(soup)

# 查找所有tag为'a'的html元素，并生成列表
# links = soup.find_all('a')
links = soup.find_all('a')

# links = soup.find_all('a target')
print("links==")
print(links)

# time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
fileName = './storage/link_' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + '.csv'
with open(fileName, 'w', newline='') as csvfile:
    fieldnames = ['link', 'text', 'pageWhereFound', 'serverResponse']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in links:
        print("content==")
        print(item.contents)
        # print(''.join(item.contents))
        # 列表转字符串
        contentList = map(lambda x: str(x), item.contents)
        contentStr = ''.join(contentList)
        print(contentStr)

        urlHref = item.get('href')
        print("url==")
        print(urlHref)
        # 写入 csv
        pageWhereFound = ''
        serverResponseStatusCode = getHttpStatusCode(returnUrl(urlHref))
        writer.writerow(
            {
                'link': urlHref,
                'text': contentStr,
                'pageWhereFound': pageWhereFound,
                'serverResponse': serverResponseStatusCode
            }
        ) '''

# todo 去重
# todo 递归
# urlTarget = 'https://www.gov.cn/zhuanti/zggcddescqgdbdh/index.htm'
targetUrlSeedSet = {urlTarget}
serverResponseStatusCode = 0

# 日志文件
fileName = './storage/link_' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + '.csv'

# 写csv
with open(fileName, 'w', newline='') as csvfile:
    fieldnames = ['link', 'text', 'pageWhereFound', 'serverResponse']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    while (targetUrlSeedSet):
        for urlPath in targetUrlSeedSet:
            print('%s: 正在访问第 %s 个链接, urlPath:\n %s' %
                  (time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()), pageVisitedNum, urlPath))

            # print(urlPath)
            # exit()

            # urlPath 转 完整url
            # urlFull = returnUrl('https://www.cnipa.gov.cn')
            urlFull = returnUrl(urlPath)
            # print(urlPath, urlFull)
            # exit()

            # 下载页面
            print('%s: 正在访问第 %s 个链接, urlFull:\n %s' %
                  (time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()), pageVisitedNum, urlFull))
            pageVisitedNum += 1

            try:
                page = getHttpRequest(urlFull)
            except print(0):
                pass
            # page = getHttpRequest(urlFull)
            # print(page.get("Content-Type"))
            # exit()

            htmlDoc = page.content.decode()
            # 解析网页
            soup = BeautifulSoup(htmlDoc, 'html.parser')
            # print(htmlDoc)
            # exit()

            # 获取标题
            # titles = soup.findall("<title>(.+?)</title>", str(htmlDoc))
            # titles = soup.find_all('a')
            titles = soup.find_all("title")
            # links = soup.find_all('a')

            # print(titles[0], titles[0].contents, titles[0].contents[0])
            # exit()

            if titles:
                title = titles[0].contents[0]
            else:
                title = '页面标题为空'

            # 写入 csv
            pageWhereFound = ''
            writer.writerow(
                {
                    'link': urlFull,
                    'text': title,
                    'pageWhereFound': str(urlMapParent.get(urlFull)),
                    'serverResponse': page.status_code
                }
            )

            # 获取页面url
            # url_set_on_page = html_parser.get_url_set_on_page()
            links = soup.find_all('a')

            for item in links:
                print('item in links ==href:,  %s:\n ' %
                      (item.get('href')))
                if item.get('href'):
                    urlSetOnPage.add(returnUrl(item.get('href')))

            # 获取种子url
            targetUrlSeedSetTmp = urlSetOnPage
            # print(targetUrlSeedSetTmp)
            # exit()

            # 构建映射
            for urlTmp in targetUrlSeedSetTmp:
                urlMapParent[urlTmp] = urlFull

            # print(urlMapParent)
            # exit()

            # url_set_not_visit = url_set_not_visit | target_url_seed_set_tmp
            urlSetNotVisit = urlSetNotVisit | targetUrlSeedSetTmp

        # url_set_visited = url_set_visited | target_url_seed_set
        urlSetVisited = urlSetVisited | targetUrlSeedSet
        targetUrlSeedSet = urlSetNotVisit - urlSetVisited

        print(targetUrlSeedSet, '\n====== \n', urlSetNotVisit,  '\n======\n', urlSetVisited)
        # exit()
