#!/user/bin/python
# -*- coding: utf-8 -*-
# Python 中文编码
import os

# 导入csv
import csv
import time  # 引入time模块

# 导入BeautifulSoup和requests模块
from bs4 import BeautifulSoup
import requests

# import requests_random_user_agent

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from urllib.parse import urlparse

from random import randint

# 任务开始时间
taskStartTime = time.time()
# taskEndTime = time.time()
# print(taskStartTime, taskEndTime-taskStartTime)
# exit()

# # 目标站点
# urlProtocol = 'https'
# urlHost = 'www.cnipa.gov.cn'
# # TODO adjyc
# urlProtocol = 'http'
# urlHost = 'www.adjyc.com'
urlProtocol = input("目标站点协议,如 https:") or 'https'
print('目标站点协议============' + urlProtocol)
urlHost = input("目标站点url：如 www.cnipa.gov.cn:") or 'www.cnipa.gov.cn'
print('目标站点url============' + urlHost)
# 目标url
urlTarget = urlProtocol + '://' + urlHost
print('目标站点============' + urlTarget)

# 存放还没访问的url
urlSetNotVisit = set()

# 存放已访问的url
urlSetVisited = set()

# 当前页url
urlSetOnPage = set()

targetUrlSeedSetTmp = set()

# 存放已访问的url字典映射，关联父url
urlMapParent = {}

# 存放url标题字典映射
urlMapTitle = {}

# 访问页面计数器
pageVisitedNum = 0

# 非 链接后缀 url
notLinkSuffixSet = {'.jpg', '.zip', '.png', '.gif', '.doc', '.docx', '.ppt', '.pptx', '.pdf', '.rar', '.gz', }

pageContentType = ''

# 获取字符串格式的html_doc。由于content为bytes类型，故需要decode()
# html_doc = requests.get('https://xkcd.com/353/').content.decode()
# 加 headers
# headers = {'user-agent': 'my-app/0.0.1'}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'}

userAgents = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
]

# 初始目标url
# urlTarget = 'https://www.gov.cn/zhuanti/zggcddescqgdbdh/index.htm'
# pdf
# urlTarget = 'https://www.cnipa.gov.cn/module/download/down.jsp?i_ID=176955&colID=74'
# urlTarget = 'https://www.cnipa.gov.cn/attach/0/9607103da7fa4ae493f000bd0303f565.pdf'
# title IndexError: list index out of range
# urlTarget = 'https://pss-system.cponline.cnipa.gov.cn'
# urlTarget = 'http://wsgs.sbj.cnipa.gov.cn:9080/tmpu/'
# urlTarget = 'http://wsgs.sbj.cnipa.gov.cn:9080/tmpu/\\'
# urlTarget = 'http://wsgs.sbj.cnipa.gov.cn:9080/tmpu/javascript'

targetUrlSeedSet = {urlTarget}

# 默认状态 0
serverResponseStatusCode = 0

# 日志文件
csvFileName = './storage/link_' + urlHost + '_' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + '.csv'
logFileName = './storage/log_' + urlHost + '_' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + '.log'


# 获取链接后缀
def getLinkSuffix(urlFull):
    a = urlparse(urlFull)
    print(a)
    linkFileName = os.path.basename(a.path)
    _, linkSuffix = os.path.splitext(linkFileName)
    print(linkFileName)
    print(linkSuffix)
    # exit()
    return linkSuffix


# 获取随机 UA
def getRandomUa():
    global userAgents
    return userAgents[randint(0, len(userAgents) - 1)]


# 获取请求

# s = requests.Session()
# print(s.headers['User-Agent'])

# # Without a session
# resp = requests.get('https://httpbin.org/user-agent')
# print('user-agent======', resp.json()['user-agent'])
# print('resp========', resp.json())
# exit()

def getHttpRequest(url):
    # global headers

    # 使用 requests_random_user_agent 包
    # s = requests.Session()
    # headers = {'user-agent': s.headers['User-Agent'], 'Connection': 'close'}

    headers = {'user-agent': getRandomUa(), 'Connection': 'close'}
    print('===================================headers==========')
    print(headers)

    try:
        resGet = requests.get(url, headers=headers, verify=False)
        return resGet
    except requests.exceptions.HTTPError as e:
        # TODO debug
        print(111)
        print(e)
        return e
    except requests.exceptions.ConnectionError as e:
        # TODO debug
        print(222)
        print(e)
        return e
    except:
        # return e
        print(333)
        print(e)
        return e


# 检测字符串是否url


def checkIsUrl(strx):
    return strx.startswith("http")


# 返回 url
def returnUrl(strx):
    if strx.startswith("http"):
        return strx.strip()
    # //www.baidu.com/duty
    elif strx.startswith("//"):
        return (urlProtocol + ':' + strx).strip()
    elif strx.startswith("/"):
        return (urlProtocol + '://' + urlHost + strx).strip()
    elif strx.startswith("./"):
        return (urlProtocol + '://' + urlHost + strx[1:]).strip()
    else:
        return (urlProtocol + '://' + urlHost + '/' + strx).strip()


with open(logFileName, 'w', encoding='utf-8-sig', newline='') as logFile:
    # 写csv
    with open(csvFileName, 'w', encoding='utf-8-sig', newline='') as csvFile:
        fieldnames = ['link', 'text', 'pageWhereFound', 'serverResponse']
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writeheader()

        while targetUrlSeedSet:
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

                # 过滤 javascript 和 mailto
                # if urlPath.find('javascript') != -1:
                #     continue
                # if urlPath.find('mailto') != -1:
                #     continue
                # if urlPath.find('/\\') != -1:
                #     continue
                if 'javascript' in urlPath:
                    print('=============urlPath带有javascript')
                    continue
                if 'mailto' in urlPath:
                    print('=============urlPath带有mailto')
                    continue
                if '/\\' in urlPath:
                    print('=============urlPath带有/\\')
                    continue

                # urlPath 转 完整url
                urlFull = returnUrl(urlPath)
                # TODO test
                # urlFull = 'https://www.cnipa.gov.cn/module/download/down.jsp?i_ID=179049&colID=74'
                # urlFull = 'https://www.cnipa.gov.cn/art/2020/5/26/art_701_14.html'
                # urlFull = 'http://www.customs.gov.cn/'
                # urlFull = 'http://36.112.95.124/reexam_out2020New/searchIndexKS.jsp'

                # print(urlPath, urlFull)
                # exit() 

                # 下载页面
                print('%s: 正在访问第 %s 个链接, urlFull:\n %s' %
                      (time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()), pageVisitedNum, urlFull))
                pageVisitedNum += 1

                # TODO 过滤 zip,jpg 等大文件, 加快检查效率
                # 跳过非 链接后缀 url
                linkSuffix = getLinkSuffix(urlFull)

                if linkSuffix in notLinkSuffixSet:
                    continue

                # 休息 0.5 秒
                # time.sleep(0.5)

                try:
                    page = getHttpRequest(urlFull)
                    # https://www.runoob.com/http/http-content-type.html
                    # print(type(page.headers), type(linkSuffix), type(notLinkSuffixSet), 'Content-Type2' in page.headers)
                    # exit()
                    if 'Content-Type' in page.headers:
                        pageContentType = page.headers['Content-Type']

                    # print('page======', page, page.headers['Content-Type'])
                    # print('page======', page, page.headers)
                    # exit()

                    # 跳过非 链接后缀 url
                    # linkSuffix = getLinkSuffix(urlFull)

                    # if (linkSuffix in notLinkSuffixSet):
                    #     continue
                    # print('page======', page, page.headers)
                    # exit()
                    if not pageContentType.startswith("text/html"):
                        continue
                except requests.exceptions.HTTPError as e:
                    print(('\n异常request urlFull: %s, code: %s, message: %s' %
                           (urlFull, str(e.code), e.message)))
                    # 写日志
                    logFile.write(('\n异常request urlFull: %s, code: %s, message: %s' %
                                   (urlFull, str(e.code), e.message)))
                    logFile.flush()
                    continue
                    # pass
                    # TODO 只解析 utf8
                except requests.exceptions.ConnectionError as e:
                    print(('\n异常request urlFull: %s, code: %s, message: %s' %
                           (urlFull, str(e.code), e.message)))
                    # 写日志
                    logFile.write(('\n异常request urlFull: %s, code: %s, message: %s' %
                                   (urlFull, str(e.code), e.message)))
                    logFile.flush()
                    continue
                    # pass
                    # TODO 只解析 utf8
                except:
                    print(('\n异常request urlFull: %s, code: %s, message: %s' %
                           (urlFull, str(500), 'error')))
                    # 写日志
                    logFile.write(('\n异常request urlFull: %s, code: %s, message: %s' %
                                   (urlFull, str(500), 'error')))
                    logFile.flush()

                    pageWhereFound = ''
                    writer.writerow(
                        {
                            'link': urlFull,
                            'text': 'error',
                            'pageWhereFound': str(urlMapParent.get(urlFull)),
                            'serverResponse': 500
                        }
                    )
                    csvFile.flush()

                    continue
                try:
                    htmlDoc = page.content.decode()
                except Exception as e:
                    print(('\n异常解码 urlFull: %s, code: %s, message: %s' % (urlFull, '', '')))
                    # 写日志
                    logFile.write(('\n异常解码 urlFull: %s, code: %s, message: %s' % (urlFull, '', '')))
                    logFile.flush()

                    continue
                    # pass

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
                    # TODO 先通过集合获取标题，没有在默认
                    title = str(urlMapTitle.get(urlFull));
                    if len(title) == 0:
                        title = '页面标题为空'

                # 写入 csv
                if page.status_code != 200:
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

                # 判断是否本站点, 非本站点，无需检测子链接
                if not urlFull.startswith(urlTarget):
                    continue

                # 获取页面url
                # url_set_on_page = html_parser.get_url_set_on_page()
                links = soup.find_all('a')

                # 返回url默认值
                returnUrlFull = ''

                for item in links:
                    print('item in links ==href:,  %s:\n ' % (item.get('href')))
                    print('item==', item)

                    if item.get('href'):
                        returnUrlFull = returnUrl(item.get('href'))

                        # 获取链接title
                        # relSoup = BeautifulSoup(item, 'html.parser')
                        # # print(relSoup.a.contents)
                        # print('relSoup==', relSoup)
                        # exit;

                        urlTitle = ''
                        # 构建映射
                        urlMapTitle[returnUrlFull] = urlTitle

                    # 本站点
                    # if returnUrlFull.startswith(urlTarget):
                    #     urlSetOnPage.add(returnUrlFull)

                    # 非本这点也要验证自身url是否死链
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

            print('\n targetUrlSeedSet====== \n', targetUrlSeedSet,
                  '\n urlSetNotVisit====== \n', urlSetNotVisit,
                  '\n urlSetVisited======\n', urlSetVisited,
                  '\n targetUrlSeedSetTmp======\n', targetUrlSeedSetTmp,
                  )

        # 任务结束时间
        taskEndTime = time.time()
        taskRunTime = taskEndTime - taskStartTime

        # 写日志
        logFile.write('\n ============检查完成============')
        logFile.write('\n ============共耗时============ \n  %s s' % (str(taskRunTime)))

        # logFile.write(('\n异常request urlFull: %s, code: %s, message: %s' %(urlFull, str(e.code), e.message)))
        logFile.flush()
        # exit()

print('检查完成')
print('\n ============共耗时============ \n  %s s' % (str(taskRunTime)))

q = input("按任意键退出：")
