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

from core.testingKit_app.const import *

from core.testingKit_app.puppeteer import Puppeteer


__all__ = ['ModeSystem']


class ModeSystem(object):
    """
    元素模型 - 系统元素模型
    """

    pageName = '系统元素模型'

    # 日志服务
    _Log = Log()

    # Puppeteer 实例
    _puppeteerObj: Puppeteer = None

    def __init__(self, puppeteer_obj: Puppeteer):
        """
        初始化

        :param puppeteer_obj    : Puppeteer 实例
        """
        self._puppeteerObj = puppeteer_obj

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
    def home_upward_arrows(self):
        """
        首页 - 向上的箭头
            * 该元素点击后会进入应用程序视窗
        """
        return self._puppeteerObj.module(
            {
                CONST_ELEMENT_BY: 'id',
                CONST_ELEMENT_EL: 'com.google.android.apps.nexuslauncher:id/all_apps_handle',

                CONST_ELEMENT_PAGE_NAME: self.pageName,
                CONST_ELEMENT_BUTTON_NAME: '向上的箭头',
            })

    @property
    def app_view_top_search(self):
        """
        应用程序视窗 - 顶部搜索框
        """
        return self._puppeteerObj.module(
            {
                CONST_ELEMENT_BY: 'id',
                CONST_ELEMENT_EL: 'com.google.android.apps.nexuslauncher:id/search_box_input',

                CONST_ELEMENT_PAGE_NAME: self.pageName,
                CONST_ELEMENT_BUTTON_NAME: '应用程序视窗.顶部搜索框',
            })

    @property
    def app_view_app_list(self):
        """
        应用程序视窗 - 应用程序列表
            * 该元素拥有 text 属性，为该应用程序名称
        """
        return self._puppeteerObj.module(
            {
                CONST_ELEMENT_BY: 'id',
                CONST_ELEMENT_EL: 'com.google.android.apps.nexuslauncher:id/icon',

                CONST_ELEMENT_PAGE_NAME: self.pageName,
                CONST_ELEMENT_BUTTON_NAME: '应用程序视窗.应用程序列表',
            })

    # 可以看到系统计算机的数字1-9中，id定位方式的属性由 com.android.calculator2:id/digit_ + 数字1-9 组成
    # 这在实际场景中也是一种常见的常见，应对这种情况，可以通过以下方法设计模型
    # 将模型函数的 @property 装饰器 去掉
    # 通过传入一个数字参数，并拼接到元素的 id 属性中实现
    def calculator_keyboard_int(self, key: int):
        """
        系统计算机 - 软键盘 - 数字
        """
        return self._puppeteerObj.module(
            {
                CONST_ELEMENT_BY: 'id',
                CONST_ELEMENT_EL: f'com.android.calculator2:id/digit_{key}',

                CONST_ELEMENT_PAGE_NAME: self.pageName,
                CONST_ELEMENT_BUTTON_NAME: f'系统计算机.软键盘.数字{key}',
            })

    @property
    def calculator_keyboard_add(self):
        """
        系统计算机 - 数字键盘 - 加号
        """
        return self._puppeteerObj.module(
            {
                CONST_ELEMENT_BY: 'id',
                CONST_ELEMENT_EL: 'com.android.calculator2:id/op_add',

                CONST_ELEMENT_PAGE_NAME: self.pageName,
                CONST_ELEMENT_BUTTON_NAME: '系统计算机.软键盘.加号',
            })

    @property
    def calculator_keyboard_eq(self):
        """
        系统计算机 - 数字键盘 - 等于号
        """
        return self._puppeteerObj.module(
            {
                CONST_ELEMENT_BY: 'id',
                CONST_ELEMENT_EL: 'com.android.calculator2:id/eq',

                CONST_ELEMENT_PAGE_NAME: self.pageName,
                CONST_ELEMENT_BUTTON_NAME: '系统计算机.软键盘.等于号',
            })

    @property
    def calculator_keyboard_result(self):
        """
        系统计算机 - 数字键盘 - 计算结果
        """
        return self._puppeteerObj.module(
            {
                CONST_ELEMENT_BY: 'id',
                CONST_ELEMENT_EL: 'com.android.calculator2:id/result',

                CONST_ELEMENT_PAGE_NAME: self.pageName,
                CONST_ELEMENT_BUTTON_NAME: '系统计算机.软键盘.计算结果',
            })


if __name__ == '__main__':
    pass

