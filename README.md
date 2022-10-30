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
