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

"""

from core.const import Const
from core.common.log import Log
from core.common.element_structure import ElementStructure

from core.testingkit.web.driverhandle import RegisteredDriver
from core.testingkit.web.puppeteer import Puppeteer
from core.testingkit.web.puppeteer import PuppeteerCore


__all__ = ['ModeBdHome']


class ModeBdHome(object):
    """
    元素模型 - 百度首页
    """

    modeName = '百度首页模型'

    # 日志服务
    _logServer = Log()

    # PuppeteerCore 实例
    _puppeteerCore: PuppeteerCore = None

    def __init__(self, registered_driver: RegisteredDriver):
        """
        初始化

        :param registered_driver : RegisteredDriver 实例
        """
        self._puppeteerCore = Puppeteer(registered_driver)

    @property
    def app(self):
        """
        程序组件
        """
        return self._puppeteerCore.app()

    @property
    def view(self):
        """
        屏幕组件
        """
        return self._puppeteerCore.view()

    @property
    def home_search(self):
        """
        搜索框
        """
        return self._puppeteerCore.module(ElementStructure(
            {
                Const.ELEMENT_BY: 'xpath',
                Const.ELEMENT_EL: '//input[@id="kw"]',
                Const.ELEMENT_PAGE_NAME: self.modeName,
                Const.ELEMENT_ELEMENT_NAME: '搜索框',
            }))

    @property
    def home_search_confirm(self):
        """
        搜索框 - 百度一下
        """
        return self._puppeteerCore.module(ElementStructure(
            {
                Const.ELEMENT_BY: 'xpath',
                Const.ELEMENT_EL: '//input[@id="su"]',
                Const.ELEMENT_PAGE_NAME: self.modeName,
                Const.ELEMENT_ELEMENT_NAME: '搜索框.百度一下',
            }))


if __name__ == '__main__':
    pass

