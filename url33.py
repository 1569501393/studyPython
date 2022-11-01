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


# 获取字符串格式的html_doc。由于content为bytes类型，故需要decode()
# html_doc = requests.get('https://xkcd.com/353/').content.decode()
# 加 headers
# headers = {'user-agent': 'my-app/0.0.1'}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'}


# 初始目标url
# urlTarget = 'https://www.gov.cn/zhuanti/zggcddescqgdbdh/index.htm'
# pdf
# urlTarget = 'https://www.cnipa.gov.cn/module/download/down.jsp?i_ID=176955&colID=74'
# urlTarget = 'https://www.cnipa.gov.cn/attach/0/9607103da7fa4ae493f000bd0303f565.pdf'
# title IndexError: list index out of range
# urlTarget = 'https://pss-system.cponline.cnipa.gov.cn'
# urlTarget = 'http://wsgs.sbj.cnipa.gov.cn:9080/tmpu/'

targetUrlSeedSet = {urlTarget}


# 默认状态 0
serverResponseStatusCode = 0

# 日志文件
csvFileName = './storage/link_' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + '.csv'
logFileName = './storage/log_' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + '.log'


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
    global headers

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


with open(logFileName, 'w') as logFile:
    # 写csv
    with open(csvFileName, 'w', newline='') as csvFile:
        fieldnames = ['link', 'text', 'pageWhereFound', 'serverResponse']
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writeheader()

        while (targetUrlSeedSet):
            for urlPath in targetUrlSeedSet:
                logContent = ('\n %s: 正在访问第 %s 个链接, urlPath:\n %s' %
                              (
                                  time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                  pageVisitedNum,
                                  urlPath
                              ))

                print(logContent)

                # 写日志
                logFile.write(logContent)
                logFile.flush()

                # urlPath 转 完整url
                urlFull = returnUrl(urlPath)
                # print(urlPath, urlFull)
                # exit()

                # 下载页面
                print('%s: 正在访问第 %s 个链接, urlFull:\n %s' %
                      (time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()), pageVisitedNum, urlFull))
                pageVisitedNum += 1

                try:
                    page = getHttpRequest(urlFull)
                except requests.exceptions.HTTPError as e:
                    # 写日志
                    logFile.write(('\n异常request urlFull: %s, code: %s, message: %s' %
                                  (urlFull, str(e.code), e.message)))
                    logFile.flush()
                    continue
                    pass
                # page = getHttpRequest(urlFull)
                # print(page.get("Content-Type"))
                # exit()

                    # TODO 只解析 utf8
                try:
                    htmlDoc = page.content.decode()
                except Exception as e:
                    # 写日志
                    logFile.write(('\n异常解码 urlFull: %s, code: %s, message: %s' % (urlFull, '', '')))
                    logFile.flush()

                    continue
                    pass

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
                # print(titles, titles[0].contents)
                # exit()

                if titles and titles[0] and titles[0].contents:
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
                csvFile.flush()

                # 获取页面url
                # url_set_on_page = html_parser.get_url_set_on_page()
                links = soup.find_all('a')

                # 返回url默认值
                returnUrlFull = ''

                for item in links:
                    print('item in links ==href:,  %s:\n ' %
                          (item.get('href')))

                    if item.get('href'):
                        returnUrlFull = returnUrl(item.get('href'))

                    # 本站点
                    if returnUrlFull.startswith(urlTarget):
                        urlSetOnPage.add(returnUrlFull)

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

            # print(targetUrlSeedSet, '\n====== \n', urlSetNotVisit,  '\n======\n', urlSetVisited)
            # exit()
