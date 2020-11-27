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

    Last Modified Time : 2020.11.27

    RegisteredDriver   :

        DriverHandle 模块由基类 BaseDriverHandle 实现注册机制， 其本身只负责驱动注册过程

        RegisteredDriver 模块由基类 BaseRegisteredDriver 实现封装的 Find 函数

"""

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from core.const import Const
from core.common.base_driver import BaseDriverHandle
from core.common.base_driver import BaseRegisteredDriver


__all__ = ['DriverHandle', 'RegisteredDriver']


class DriverHandle(object):
    """
    单例模式 \n
    """

    _unique_driver_handle = None

    def __new__(cls, *args, **kwargs):
        if not cls._unique_driver_handle:
            cls._unique_driver_handle = _DriverHandle()
        return cls._unique_driver_handle


class _DriverHandle(BaseDriverHandle):
    """
    Driver 设备驱动处理器 \n
    """

    # 已注册的驱动器名称
    registeredDriverName = 'WebDriver'

    def get_driver_chrome(self, driver_name: str or None = None):
        """
        获取 谷歌浏览器 驱动 \n
        """

        # Chrome浏览器 提供 W3C 校验的解决方案
        # if :: Cannot call non W3C standard command while in W3C mode
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        driverCore = webdriver.Chrome(chrome_options=opt),

        return RegisteredDriver(
            driver_core=driverCore[0],
            driver_name=self._register_driver_flow(driver_name, driverCore),
            driver_type=Const.DRIVER_TYPE_BROWSER_CHROME
        )


class RegisteredDriver(BaseRegisteredDriver):
    """
    已注册的设备驱动类 \n
    """

    _driverCore: WebDriver = None


if __name__ == '__main__':
    pass

