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

from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from core.common.log import Log
from core.common.find import Find
from core.common.tools import Tools


__all__ = ['Driver', 'RegisteredDriver']


# class Driver(Find):
#     """
#     Driver 设备驱动模块
#     """
#
#     # Driver 实例
#     driverObj: WebDriver = None
#
#     # 配置文件路径
#     _configPath = None
#
#     # 配置参数容器
#     _configData = None
#
#     def __init__(self, config_path: str, interface: str = '4723'):
#         """
#         初始化，生成 Android / Ios 设备的 driver 驱动器
#
#         :param config_path        : Yaml 格式的配置文件绝对路径
#         :param interface          : Appium Server 使用的端口
#         """
#         try:
#             self._configPath = config_path
#             self._configData = Tools.load_from_yaml(self._configPath)
#             self.driverObj = webdriver.Remote(f'http://localhost:{interface}/wd/hub', self._configData)
#             self._Log.info('Driver has started .. >> running')
#
#         except Exception as err:
#             self._Log.warning(f'Driver 配置解析失败，详情信息: {err}')


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
    def get_driver(config_path: str, interface: str = '4723', driver_name: str or None = None):
        """
        获取 Android / Ios 设备的 driver 驱动器
        """
        driverObj = webdriver.Remote(f'http://localhost:{interface}/wd/hub', Tools.load_from_yaml(config_path))
        return RegisteredDriver(
            driver_obj=driverObj,
            driver_name=driver_name,
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

    def __init__(self, driver_obj, driver_name):
        self.driverObj = driver_obj
        self.driverName = self._register_driver_flow(driver_name)

        # 注册映射
        DriverObj.registeredDriverMapDict[self.driverName] = self.driverObj

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

