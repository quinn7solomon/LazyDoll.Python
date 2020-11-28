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

    GitPath      : https://github.com/quinn7solomon/LazyDoll.Python
    FrameName    : LazyDoll_Python
    CreatorName  : Quinn7k
    CreationTime : 2020.11.19

    Last Modified Time : 2020.11.27

    RegisteredDriver   :

        Puppeteer 模块职责于优雅的构建页面功能组件与构建页面元素组件

        示例: (构建一个百度首页搜索框的元素组件并调用方法)

            baiDu_button = puppeteerObj.module(ElementStructure(
                           {
                               Const.ELEMENT_BY: 'xpath',
                               Const.ELEMENT_EL: '//input[@id="kw"]',
                               Const.ELEMENT_PAGE_NAME: '百度模型',
                               Const.ELEMENT_ELEMENT_NAME: '首页搜索框'
                           }))

        示例: (调用方法)

            baiDu_button.get_element_len()  # 获取元素数量
            baiDu_button.get_text()         # 获取元素 text 属性
            baiDu_button.tap()              # 点击元素
            baiDu_button.in_page()          # 判断元素是否存在当前页面

"""

from core.common.log import Log
from core.testingkit.app.driverhandle import RegisteredDriver
from core.common.element_structure import ElementStructure
from core.common.customize_exception import PuppeteerConstructorsAppException
from core.common.customize_exception import PuppeteerConstructorsViewException
from core.common.customize_exception import PuppeteerConstructorsModuleException

from core.testingkit.app.constructors_app import ConstructorsApp
from core.testingkit.app.constructors_view import ConstructorsView
from core.testingkit.app.constructors_module import ConstructorsModule


__all__ = ['Puppeteer', 'PuppeteerCore']


class Puppeteer(object):
    """
    单例模式 \n
    """

    _unique_puppeteer_core = None

    def __new__(cls, registered_driver, *args, **kwargs):
        if not cls._unique_puppeteer_core:
            cls._unique_puppeteer_core = PuppeteerCore(registered_driver)
        return cls._unique_puppeteer_core


class PuppeteerCore(object):
    """
    组件对象 OOP 构建函数类 \n
    """

    # 日志服务
    _logServer = Log()

    # RegisteredDriver 实例
    _registeredDriver: RegisteredDriver = None

    # ConstructorsApp 实例
    _uniqueConstructorsApp = None

    # ConstructorsView 实例
    _uniqueConstructorsView = None

    def __init__(self, registered_driver: RegisteredDriver):
        """
        初始化 \n

        :param registered_driver : RegisteredDriver 对象
        """
        self._registeredDriver = registered_driver

    def app(self):
        """
        构架组件对象:: 程序组件 \n
        """
        try:
            if not self._uniqueConstructorsApp:
                self._uniqueConstructorsApp = ConstructorsApp(self._registeredDriver)

            return self._uniqueConstructorsApp

        except Exception:
            raise PuppeteerConstructorsAppException

    def view(self):
        """
        构架组件对象:: 屏幕组件 \n
        """
        try:
            if not self._uniqueConstructorsView:
                self._uniqueConstructorsView = ConstructorsView(self._registeredDriver)

            return self._uniqueConstructorsView

        except Exception:
            raise PuppeteerConstructorsViewException

    def module(self, element_structure: ElementStructure):
        """
        构架组件对象:: 按键组件 \n

        :param element_structure    : 元素结构体 ElementStructure 对象
        """
        try:
            return ConstructorsModule(self._registeredDriver, element_structure)

        except Exception:
            raise PuppeteerConstructorsModuleException


if __name__ == '__main__':
    pass

