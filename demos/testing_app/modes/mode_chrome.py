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

from core.testingkit.app.puppeteer import PuppeteerLiving


__all__ = ['ModeChrome']


class ModeChrome(object):
    """
    元素模型 - 谷歌浏览器模型
    """

    pageName = '谷歌浏览器模型'

    # 日志服务
    _Log = Log()

    # Puppeteer 实例
    _puppeteerObj: PuppeteerLiving = None

    def __init__(self, puppeteer_obj: PuppeteerLiving):
        """
        初始化

        :param puppeteer_obj    : Puppeteer 实例
        """
        self._puppeteerObj = puppeteer_obj

    def open_app(self):
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
        return self._puppeteerObj.app()

    @property
    def view(self):
        """
        屏幕组件
        """
        return self._puppeteerObj.view()

    @property
    def search(self):
        """
        搜索框
        """
        return self._puppeteerObj.module(
            {
                CONST_ELEMENT_BY: 'id',
                CONST_ELEMENT_EL: 'com.android.chrome:id/search_box_text',

                CONST_ELEMENT_PAGE_NAME: self.pageName,
                CONST_ELEMENT_BUTTON_NAME: '搜索框',
            })

    @property
    def url_bar(self):
        """
        URL输入框
        """
        return self._puppeteerObj.module(
            {
                CONST_ELEMENT_BY: 'id',
                CONST_ELEMENT_EL: 'com.android.chrome:id/url_bar',

                CONST_ELEMENT_PAGE_NAME: self.pageName,
                CONST_ELEMENT_BUTTON_NAME: 'URL输入框',
            })

    @property
    def search_result(self):
        """
        搜索结果
        """
        return self._puppeteerObj.module(
            {
                CONST_ELEMENT_BY: 'xpath',
                CONST_ELEMENT_EL: "//*[@class='android.widget.TextView']",

                CONST_ELEMENT_PAGE_NAME: self.pageName,
                CONST_ELEMENT_BUTTON_NAME: '搜索结果',
            })


if __name__ == '__main__':
    pass

