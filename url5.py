# coding:utf-8
from time import time
from bs4 import BeautifulSoup
import requests
import sys

# 设置http请求头伪装成浏览器
send_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"}

# requests获取博客页面html文本
num = [1, 2, 3, 4]
artlist = ""
for i in num:
    # url = article/list /"+str(i)
    url = "article/list/1"
    r = requests.get(url, headers=send_headers)
    r.encoding = "utf-8"
    html=r.text

    # 将获取到的html送入bs4进行解析
    soup = BeautifulSoup(html, "html.parser")   # 获得解析后对象
    mainBox = soup.find("div", id="mainBox")    # 找到id是mainBox的div
    # 找到这个div中所有 class 是 article-item-box csdn-tracking-statistics 的div
    artlist =mainBox.find_all("div", attrs={"class":"article-item-box csdn-tracking-statistics"})

# 遍历每个div 输出内容 以html形式输出
    for div in artlist:
        a = div.h4.a
        print("<a href='" + a["href"] + "'>" + a.text[14:-9] + "</a><br><br>")