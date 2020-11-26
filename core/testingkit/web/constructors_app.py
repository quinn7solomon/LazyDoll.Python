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

from selenium.webdriver.remote.webdriver import WebDriver

from core.common.log import Log
from core.testingkit.web.driver import RegisteredDriver


__all__ = ['ConstructorsApp']


class ConstructorsApp(object):
    """
    程序组件实现类 \n
    """

    # 日志服务
    _logServer = Log()

    # Driver 实例
    _registeredDriver: RegisteredDriver = None
    # DriverCore 实例
    _driverCore: WebDriver = None

    def __init__(self, registered_driver: RegisteredDriver):
        """
        初始化 \n

        :param registered_driver : RegisteredDriver 对象
        """
        self._registeredDriver = registered_driver
        self._driverCore = registered_driver.get_driver_core()

    def goto_url(self, url: str):
        """
        浏览器跳转到指定URL \n

        :param url               : 跳转目标URL
        """
        self._registeredDriver.goto_url(url)


if __name__ == '__main__':
    pass

