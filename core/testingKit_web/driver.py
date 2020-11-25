# /usr/bin/env python3.8
# -*- coding=utf-8 -*-
"""
     ___      _______  _______  __   __  ______   _______  ___      ___              _______  __   __
    |   |    |   _   ||       ||  | |  ||      | |       ||   |    |   |            |       ||  | |  |
    |   |    |  |_|  ||____   ||  |_|  ||  _    ||   _   ||   |    |   |            |    _  ||  |_|  |
    |   |    |       | ____|  ||       || | |   ||  | |  ||   |    |   |            |   |_| ||       |
    |   |___ |       || ______||_     _|| |_|   ||  |_|  ||   |___ |   |___         |    ___||_     _|
    |       ||   _   || |_____   |   |  |       ||       ||       ||       | _____  |   |      |   |
    |_______||__| |__||_______|  |___|  |______| |_______||_______||_______||_____| |___|      |___|

    Copyright (c) 2020, @ quinn.7@foxmail.com, All rights reserved

    GitPath      : https://github.com/quinn7solomon/LazyDoll_Python
    FrameName    : LazyDoll_Python
    CreatorName  : Quinn7k
    CreationTime : 2020.11.19
    Environment  : PyCharm

"""

import random

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from core.const import *
from core.common.log import Log
from core.common.find import Find


__all__ = ['Driver', 'RegisteredDriver']


class Driver(object):
    """
    单例模式
    """

    _driverObj = None

    def __new__(cls, *args, **kwargs):
        if not cls._driverObj:
            cls._driverObj = DriverObj()
        return cls._driverObj


class DriverObj(object):
    """
    Driver 设备驱动模块
    """

    # 日志服务
    _Log = Log()

    # 已注册的驱动器列表
    registeredDriverList = []
    # 已注册的驱动器映射字典
    registeredDriverMapDict = {}

    @staticmethod
    def get_driver_chrome(driver_name: str or None = None):
        """
        获取 谷歌浏览器 驱动
        """

        # Chrome浏览器 提供 W3C 校验的解决方案
        # if :: Cannot call non W3C standard command while in W3C mode
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)

        return RegisteredDriver(
            driver_obj=webdriver.Chrome(chrome_options=opt),
            driver_name=driver_name,
            driver_type=CONST_DRIVER_TYPE_CHROME
        )

    def quit(self, driver_name: str):
        """
        销毁名为 driver_name 的已注册浏览器驱动
        """
        if driver_name in self.registeredDriverList:
            self.registeredDriverMapDict[driver_name].quit()
            self.registeredDriverList.remove(driver_name)
            self.registeredDriverMapDict.pop(driver_name)


class RegisteredDriver(Find):
    """
    已注册的浏览器驱动
    """

    driverObj: WebDriver = None
    driverName = None
    driverType = None

    def __init__(self, driver_obj, driver_name, driver_type):
        self.driverObj = driver_obj
        self.driverName = self._register_driver_flow(driver_name)
        self.driverType = driver_type

        # 注册映射
        DriverObj.registeredDriverMapDict[self.driverName] = self.driverObj

    def goto_url(self, url: str):
        """
        访问 URL
        """
        self.driverObj.get(url)

    @staticmethod
    def _register_driver_flow(driver_name: str or None) -> str:
        """
        驱动器注册合法性验证
        """
        if not driver_name:
            driver_name = f'browser{random.randint(1000000, 9999999)}'

        if driver_name not in DriverObj.registeredDriverList:
            DriverObj.registeredDriverList.append(driver_name)
            return driver_name

        raise Exception(f'The {driver_name} driver name is registered')


if __name__ == '__main__':
    pass

