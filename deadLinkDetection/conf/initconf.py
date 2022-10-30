#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'shouke'

import  configparser

class InitConfig:
    def __init__(self, init_conf):
        config = configparser.ConfigParser()

        # 从配置文件中读取运行模式
        config.read(init_conf, encoding='utf-8-sig')
        try:
            self.protocol = config['CONFIG']['protocol']
            self.host = config['CONFIG']['host']
            self.port = config['CONFIG']['port']
            self.username = config['CONFIG']['username']
            self.password = config['CONFIG']['password']
        except Exception as e:
            print('读取运行模式配置失败：%s' % e)
            exit()

    def get_protcol(self):
        return self.protocol

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password