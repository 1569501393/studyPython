#!/user/bin/python
# -*- coding: utf-8 -*-
# Python 中文编码

# # 目标站点 固定
urlProtocol = 'https'
urlHost = 'www.cnipa.gov.cn'
# # TODO adjyc
# urlProtocol = 'http'
# urlHost = 'www.adjyc.com'
# urlProtocol = input("目标站点协议,如 https:") or 'https'
# print('目标站点协议============' + urlProtocol)
# urlHost = input("目标站点url：如 www.cnipa.gov.cn:") or 'www.cnipa.gov.cn'
# print('目标站点url============' + urlHost)

# 目标url
urlTarget = urlProtocol + '://' + urlHost
print('目标站点============' + urlTarget)


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


strx = '//www.baidu.com/duty'
print(returnUrl(strx))
