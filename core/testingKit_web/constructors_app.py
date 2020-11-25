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
from core.testingKit_web.driver import RegisteredDriver


__all__ = ['ConstructorsApp']


class ConstructorsApp(object):
    """
    程序组件实现类
    """

    # 日志服务
    _Log = Log()

    # Driver 实例
    _driver: RegisteredDriver = None
    # DriverCore 实例
    _driverCore: WebDriver = None

    def __init__(self, driver):
        """
        初始化

        :param driver        : Driver 实例
        """
        self._driver = driver
        self._driverCore = driver.driverObj

    def goto_url(self, url: str):
        self._driver.goto_url(url)


if __name__ == '__main__':
    pass

