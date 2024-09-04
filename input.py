#!/user/bin/python
# -*- coding: utf-8 -*-
# Python 中文编码
# from datetime import datetime
import time
import datetime

# q = input("按任意键退出：")
# print(q)

current_time = time.time()
print("current_time==", current_time)
dt = datetime.datetime.fromtimestamp(current_time)
formatted_time = dt.strftime("%Y-%m-%d %H:%M:%S")
print("formatted_time==", formatted_time)
# current_time = datetime.now()
# print(current_time)

name = input("请输入名字：")
print("hello, " + name)
