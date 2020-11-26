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


    # 实例化 Puppeteer 类
    puppeteer = Puppeteer(android_configPath)

    # 组件构建模板
    button = puppeteer.module(
    {
        'anchor_ele': {                # 非必须，当存在锚元素参数时，将在锚元素下查找元素
            'by': 'element_by',
            'el': 'element_el'
        }

        'by': 'element_by',            # 元素定位方式，如id、class
        'el': 'element_el',            # 元素定位方式相应的属性
        'id': 1                        # 非必须

        'pg_name': 'page_name',        # 组件所属页面
        'bn_name': 'button_name',      # 组件名称
    })

    # 组件调用
    button.tap()
    button.on_in_page()

"""

from core.common.log import Log
from core.testingkit.web.driver import RegisteredDriver
from core.common.element_structure import ElementStructure
from core.common.customize_exception import PuppeteerConstructorsAppException
from core.common.customize_exception import PuppeteerConstructorsViewException
from core.common.customize_exception import PuppeteerConstructorsModuleException

from core.testingkit.web.constructors_app import ConstructorsApp
from core.testingkit.web.constructors_view import ConstructorsView
from core.testingkit.web.constructors_module import ConstructorsModule


__all__ = ['_PuppeteerCore']


class Puppeteer(object):
    """
    单例模式 \n
    """

    _unique_puppeteer_core = None

    def __new__(cls, registered_driver, *args, **kwargs):
        if not cls._unique_puppeteer_core:
            cls._unique_puppeteer_core = _PuppeteerCore(registered_driver)
        return cls._unique_puppeteer_core


class _PuppeteerCore(object):
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

