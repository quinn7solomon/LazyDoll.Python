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

from core.testingKit_app.driver import Driver

from core.testingKit_app.constructors_app import ConstructorsApp
from core.testingKit_app.constructors_view import ConstructorsView
from core.testingKit_app.constructors_module import ConstructorsModule


__all__ = ['Puppeteer']


class Puppeteer(object):
    """
    组件对象 OOP 构建函数类
    """

    # 日志服务
    _Log = Log()

    # DriverHandle 实例
    _DriverObj = None

    # ConstructorsApp 实例
    _constructorsAppObj = None

    # ConstructorsView 实例
    _constructorsViewObj = None

    def __init__(self, config_path: str, interface: str = '4723'):
        """
        初始化，通过 Driver 类创建驱动器对象

        :param config_path        : Yaml 格式的配置文件路径
        :param interface          : Appium Server 使用的端口
        """
        self._DriverObj = Driver(config_path, interface=interface)

    def quit(self):
        """
        退出驱动器
        """
        self._DriverObj.quit()

    def app(self):
        """
        构架组件对象: 程序组件
        """
        try:
            if not self._constructorsAppObj:
                self._constructorsAppObj = ConstructorsApp(self._DriverObj.driverObj)

        except Exception as err:
            self._Log.error(f'构建 ConstructorsApp 异常，详情信息: {err}')
            raise

        return self._constructorsAppObj

    def view(self):
        """
        构架组件对象: 屏幕组件
        """
        try:
            if not self._constructorsViewObj:
                self._constructorsViewObj = ConstructorsView(self._DriverObj.driverObj)

        except Exception as err:
            self._Log.error(f'构建 ConstructorsView 异常，详情信息: {err}')
            raise

        return self._constructorsViewObj

    def module(self, element_dict: dict):
        """
        构架组件对象: 按键组件

        :param element_dict  : 按键组件构建参数字典
        """
        try:
            constructorsModuleObj = ConstructorsModule(self._DriverObj, element_dict)

        except Exception as err:
            self._Log.error(f'构建 ConstructorsModule 异常，详情信息: {err}')
            raise

        return constructorsModuleObj


if __name__ == '__main__':
    pass

