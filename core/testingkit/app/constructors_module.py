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

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.touch_action import TouchAction

from core.common.log import Log
from core.common.element_structure import ElementStructure
from core.common.customize_exception import ModuleTapEventException
from core.common.customize_exception import ModuleLongTapEventException
from core.common.customize_exception import ModuleSendKeyEventException

from core.testingkit.app.driver import RegisteredDriver


__all__ = ['ConstructorsModule']


class ConstructorsModule(object):
    """
    元素组件实现类 \n
    """

    # 日志服务
    _logServer = Log()

    # RegisteredDriver 实例
    _registeredDriver: RegisteredDriver = None
    # DriverCore 实例
    _driverCore: WebDriver = None

    # TouchAction 类
    _touchAction = TouchAction

    # 元素结构体 ElementStructure 对象
    _elementStructure = None

    # 元素容器
    _elementContainer = None

    def __init__(self, registered_driver: RegisteredDriver, element_structure: ElementStructure):
        """
        初始化 \n

        :param registered_driver    : RegisteredDriver 实例
        :param element_structure    : 元素结构体 ElementStructure 对象
        """
        self._registeredDriver = registered_driver
        self._driverCore = registered_driver.get_driver_core()
        self._elementStructure = element_structure

    def _analytical_elements(self, wait: int = 3, tolerance=False, log_output=True):
        """
        解析函数 \n
        """
        self._elementContainer \
            = self._registeredDriver.find_element(self._elementStructure, wait, tolerance, log_output)

    def get_element_len(self, log_output: bool = True):
        """
        获取元素的数量 \n

        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._analytical_elements()
        element_len = len(self._elementContainer)

        if log_output:
            self._logServer.info(f'Get Element Len'
                                 f' -> {self._elementStructure.page_name}'
                                 f' -> {self._elementStructure.element_name}'
                                 f' -> [{element_len}]')

        return element_len

    def get_text(self, element_id: int = 1, log_output: bool = True):
        """
        获取元素的 text 属性

        :param element_id           : 元素列表下标
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._analytical_elements()
        element_text = self._elementContainer[element_id - 1].text

        if log_output:
            self._logServer.info(f'Get Element Text'
                                 f' -> {self._elementStructure.page_name}'
                                 f' -> {self._elementStructure.element_name}'
                                 f' -> [{element_text}]')

        return element_text

    def tap(self, element_id: int = 1, click_number: int = 1, log_output: bool = True):
        """
        模拟一次作用于 WebElement 对象上的点击操作

        :param element_id           : 元素列表下标
        :param click_number         : 点击次数
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        try:
            self._analytical_elements()
            element_text = self._elementContainer[element_id - 1].text

            self._touchAction(self._driverCore).tap(
                self._elementContainer[element_id - 1], count=click_number).perform()

            if log_output:
                log_output_info = f'Tap Event' \
                                  f' -> {self._elementStructure.page_name} ' \
                                  f'-> {self._elementStructure.element_name}'

                if element_text != '':
                    log_output_info += f' -> [{element_text}]'

                self._logServer.info(log_output_info)

        except Exception:
            raise ModuleTapEventException

    def long_tap(self, element_id: int = 1, wait: int = 1500, log_output: bool = True):
        """
        模拟一次作用于 WebElement 对象上的长按操作

        :param element_id           : 元素列表下标
        :param wait                 : 按住时长，单位是毫秒
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        try:
            self._analytical_elements()
            element_text = self._elementContainer[element_id - 1].text

            self._touchAction(self._driverCore).long_press(
                self._elementContainer[element_id - 1]).wait(wait).perform()

            if log_output:
                log_output_info = f'Long Tap Event' \
                                  f' -> {self._elementStructure.page_name} ' \
                                  f'-> {self._elementStructure.element_name}'

                if element_text != '':
                    log_output_info += f' -> [{element_text}]'

                self._logServer.info(log_output_info)

        except Exception:
            raise ModuleLongTapEventException

    def send_key(self, key: str, element_id: int = 1, log_output: bool = True):
        """
        输入框输入内容

        :param key                  : 输入内容
        :param element_id           : 元素列表下标
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        try:
            self._analytical_elements()
            self._elementContainer[element_id - 1].clear()
            self._elementContainer[element_id - 1].send_keys(key)

            if log_output:
                self._logServer.info(f'Send Key Event'
                                     f' -> {self._elementStructure.page_name}'
                                     f' -> {self._elementStructure.element_name}'
                                     f' -> [{key}]')

        except Exception:
            raise ModuleSendKeyEventException

    def clear(self, element_id: int = 1, log_output: bool = True):
        """
        输入框清除内容

        :param element_id           : 元素列表下标
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._analytical_elements()
        self._elementContainer[element_id - 1].clear()

        if log_output:
            self._logServer.info(f'Clear Event'
                                 f' -> {self._elementStructure.page_name}'
                                 f' -> {self._elementStructure.element_name}')

    def in_page(self, element_id: int = 1, wait: int = 3, log_output: bool = True):
        """
        判断元素是否存在当前可视页面

        :param element_id           : 元素列表下标
        :param wait                 : 元素获取时长
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志

        :return                     : Bool
        """
        self._analytical_elements(wait=wait, tolerance=True, log_output=False)

        if len(self._elementContainer) >= element_id:
            if log_output:
                self._logServer.info(f'Element Exists'
                                     f' -> {self._elementStructure.page_name}'
                                     f' -> {self._elementStructure.element_name}')
            return True

        else:
            if log_output:
                self._logServer.info(f'Element Not Exist'
                                     f' -> {self._elementStructure.page_name}'
                                     f' -> {self._elementStructure.element_name}')
            return False


if __name__ == '__main__':
    pass

