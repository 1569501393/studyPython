[TOC]

## 项目概述

* 产品名称：坏链检测
* 项目代号：url
* 官方地址：<git@github.com:1569501393/studyPython.git>

## 运行环境要求

* python3

## 开发环境部署/安装

### 基础安装

#### 1. 克隆源代码

克隆源代码到本地：

	> git clone git@github.com:1569501393/studyPython.git

#### 2. 创建 storage 目录

```
mkdir storage
```

替换 目标站点
url = 'https://www.cnipa.gov.cn/'

#### 3. 启动服务

```bash
python3 ./url3.py 
```

### 逻辑
站点坏链检测：
1. 本站点所有去重链接，从首页开始递归
2. 对于外链只需一次curl，不需要递归
3. 坏链检测 curl, 非200 状态
4. 导出 csv

### 参考效果
<https://www.brokenlinkcheck.com/broken-links.php#status>
在linux上部署成任务方式，比如每天扫描一次，自动输出格式结果csv文件。

### 参考项目
WDScanner平台目前实现了如下功能：分布式web漏洞扫描、客户管理、漏洞定期扫描、子域名枚举、端口扫描、网站爬虫、暗链检测、坏链检测、网站指纹搜集、专项漏洞检测、代理搜集及部署等功能。
<https://github.com/TideSec/WDScanner>


### 修改点

#### break

#### 对于非html的链接就不用去获取页面内容，只需要判断http链接状态即可
这个try前面增加常见的zip,images,js,pptx,doc,docx,ppt,pdf等判断，如果符合，就只判断http状态，写入csv，其它则继续htmldoc解析非外链页面内容中的链接
```
# 判断文件名后缀
urlFull2 = urlFull[len(urlFull) - 5:].lower();
# print(urlFull2);
s2 = ".";
# print(urlFull2.index(s2));
u1 = urlFull[len(urlFull) - 5 + urlFull2.index(s2):].lower()
# print(u1);

# print(urlFull2[:urlFull2.index(s2)]);

a1 = '.jpg'
a2 = '.zip'
a3 = '.png'
a4 = '.gif'
a5 = '.doc'
a6 = '.docx'
a7 = '.ppt'
a8 = 'pptx'
a9 = '.pdf'
a10 = '.rar'
a11 = '.gz'

if not (u1 == a1 or u1 == a2 or u1 == a3 or u1 == a4 or u1 == a5 or u1 == a6 or u1 == a7 or u1 == a8 or u1 == a9 or u1 == a10 or u1 == a11):
```
