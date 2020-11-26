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

from core.common.log import Log


class _CustomizeException(Exception):
    """
    自定义异常 \n
    """
    _logServer = Log()


class FindElementException(_CustomizeException):
    """
    Find 获取函数异常 \n
    """
    def __init__(self, err='The element retrieved by Find is empty'):
        self._logServer.error(err)
        Exception.__init__(self, err)


class LoadYamlException(_CustomizeException):
    """
    Yaml文件加载异常 \n
    """
    def __init__(self, err='Yaml file loading error'):
        self._logServer.error(err)
        Exception.__init__(self, err)


class DriverNameRegisterException(_CustomizeException):
    """
    Driver 名称注册异常 \n
    """
    def __init__(self, driver_name: str):
        self._logServer.error(f'The {driver_name} driver name is registered')
        Exception.__init__(self, f'The {driver_name} driver name is registered')


class PuppeteerConstructorsAppException(_CustomizeException):
    """
    构架程序组件异常 \n
    """
    def __init__(self, err='Puppeteer builds app component exceptions'):
        self._logServer.error(err)
        Exception.__init__(self, err)


class PuppeteerConstructorsViewException(_CustomizeException):
    """
    构架屏幕组件异常 \n
    """
    def __init__(self, err='Puppeteer builds view component exceptions'):
        self._logServer.error(err)
        Exception.__init__(self, err)


class PuppeteerConstructorsModuleException(_CustomizeException):
    """
    构架按键组件异常 \n
    """
    def __init__(self, err='Puppeteer builds module component exceptions'):
        self._logServer.error(err)
        Exception.__init__(self, err)


class DevicePhysicalKeyException(_CustomizeException):
    """
    移动设备物理键异常 \n
    """
    def __init__(self, err='Device physical key exception'):
        self._logServer.error(err)
        Exception.__init__(self, err)


class NetworkSwitchEventException(_CustomizeException):
    """
    移动设备切换网络异常 \n
    """
    def __init__(self, err='Network switch event exception'):
        self._logServer.error(err)
        Exception.__init__(self, err)


class ModuleTapEventException(_CustomizeException):
    """
    点击事件异常 \n
    """
    def __init__(self, err='Module tap event exception'):
        self._logServer.error(err)
        Exception.__init__(self, err)


class ModuleLongTapEventException(_CustomizeException):
    """
    点击事件异常 \n
    """
    def __init__(self, err='Module long tap event exception'):
        self._logServer.error(err)
        Exception.__init__(self, err)


class ModuleSendKeyEventException(_CustomizeException):
    """
    点击事件异常 \n
    """
    def __init__(self, err='Module send key event exception'):
        self._logServer.error(err)
        Exception.__init__(self, err)


if __name__ == '__main__':
    pass

