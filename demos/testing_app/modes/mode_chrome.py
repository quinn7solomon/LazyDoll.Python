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

from core.testingkit.app.driverhandle import RegisteredDriver
from core.testingkit.app.puppeteer import PuppeteerCore


__all__ = ['ModeChrome']


class ModeChrome(object):
    """
    元素模型 - 谷歌浏览器模型
    """

    modeName = '谷歌浏览器模型'

    # 日志服务
    _logServer = Log()

    # PuppeteerCore 实例
    _puppeteerCore: PuppeteerCore = None

    def __init__(self, registered_driver: RegisteredDriver):
        """
        初始化

        :param registered_driver : RegisteredDriver 实例
        """
        self._puppeteerCore = PuppeteerCore(registered_driver)

    def open_app_chrome(self):
        """
        启动谷歌浏览器
        """
        self.app.app_open_activity(
            app_name='谷歌浏览器',
            package=' com.android.chrome',
            activity='com.google.android.apps.chrome.Main'
        )

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
    def search(self):
        """
        搜索框
        """
        return self._puppeteerCore.module(ElementStructure(
            {
                Const.ELEMENT_BY: 'id',
                Const.ELEMENT_EL: 'com.android.chrome:id/search_box_text',
                Const.ELEMENT_PAGE_NAME: self.modeName,
                Const.ELEMENT_ELEMENT_NAME: '搜索框',
            }))

    @property
    def url_bar(self):
        """
        URL输入框
        """
        return self._puppeteerCore.module(ElementStructure(
            {
                Const.ELEMENT_BY: 'id',
                Const.ELEMENT_EL: 'com.android.chrome:id/url_bar',
                Const.ELEMENT_PAGE_NAME: self.modeName,
                Const.ELEMENT_ELEMENT_NAME: 'URL输入框',
            }))

    @property
    def search_result(self):
        """
        搜索结果
        """
        return self._puppeteerCore.module(ElementStructure(
            {
                Const.ELEMENT_BY: 'xpath',
                Const.ELEMENT_EL: '//*[@class="android.widget.TextView"]',
                Const.ELEMENT_PAGE_NAME: self.modeName,
                Const.ELEMENT_ELEMENT_NAME: '搜索结果',
            }))


if __name__ == '__main__':
    pass

