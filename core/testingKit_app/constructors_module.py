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

from appium.webdriver.common.touch_action import TouchAction

from core.common.log import Log

from core.testingKit_app.const import *


__all__ = ['ConstructorsModule']


class ConstructorsModule(object):
    """
    元素组件实现类
    """

    # 日志服务
    _Log = Log()

    # DriverHandle 实例
    _driverHandleObj = None

    # 元素信息字典
    _elementDict = None

    # 元素列表容器
    _elementList = None

    def __init__(self, driver_handle, element_dict: dict):
        """
        初始化

        :param driver_handle       : DriverHandle 实例
        :param element_dict        : 按键组件构建参数字典
        """
        self._driverHandleObj = driver_handle
        self._elementDict = element_dict

    def _analytical_elements(self, wait: int = 20):
        """
        解析函数
        """
        self._elementList = self._driverHandleObj.find_element(self._elementDict, wait=wait)

    def get_el_len(self, log_output: bool = True):
        """
        获取元素的数量

        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._analytical_elements()
        el_len = len(self._elementList)

        if log_output:
            self._Log.info(f'获取元素数量'
                           f' -> {self._elementDict[CONST_ELEMENT_PAGE_NAME]}'
                           f' -> {self._elementDict[CONST_ELEMENT_BUTTON_NAME]}'
                           f' -> [{el_len}]')

        return el_len

    def get_text(self, element_id: int = 1, log_output: bool = True):
        """
        获取元素的 text 属性

        :param element_id           : 元素列表下标
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._analytical_elements()
        text = self._elementList[element_id - 1].text

        if log_output:
            self._Log.info(f'获取文本'
                           f' -> {self._elementDict[CONST_ELEMENT_PAGE_NAME]}'
                           f' -> {self._elementDict[CONST_ELEMENT_BUTTON_NAME]}'
                           f' -> [{text}]')

        return text

    def tap(self, element_id: int = 1, click_number: int = 1, log_output: bool = True):
        """
        模拟一次作用于 WebElement 对象上的点击操作

        :param element_id           : 元素列表下标
        :param click_number         : 点击次数
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        try:
            self._analytical_elements()
            text = self._elementList[element_id - 1].text
            TouchAction(self._driverHandleObj.driverObj).\
                tap(self._elementList[element_id - 1], count=click_number).perform()

            if log_output:
                log_output_info = f'点击事件 ' \
                                  f' -> {self._elementDict[CONST_ELEMENT_PAGE_NAME]}'\
                                  f' -> {self._elementDict[CONST_ELEMENT_BUTTON_NAME]}'
                if text != '':
                    log_output_info += f' -> [{text}]'
                self._Log.info(log_output_info)

        except Exception as err:
            self._Log.error(f'ConstructorsModule.tap 函数异常，详情信息: {err}')
            raise

    def long_tap(self, element_id: int = 1, wait: int = 1500, log_output: bool = True):
        """
        模拟一次作用于 WebElement 对象上的长按操作

        :param element_id           : 元素列表下标
        :param wait                 : 按住时长，单位是毫秒
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        try:
            self._analytical_elements()
            TouchAction(self._driverHandleObj.driverObj).\
                long_press(self._elementList[element_id - 1]).wait(wait).perform()

            if log_output:
                self._Log.info(f'长按事件'
                               f' -> {self._elementDict[CONST_ELEMENT_PAGE_NAME]}'
                               f' -> {self._elementDict[CONST_ELEMENT_BUTTON_NAME]}')

        except Exception as err:
            self._Log.error(f'ConstructorsModule.long_tap 函数异常，详情信息: {err}')
            raise

    def send(self, key: str, element_id: int = 1, log_output: bool = True):
        """
        输入框输入内容

        :param key                  : 输入内容
        :param element_id           : 元素列表下标
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._analytical_elements()
        self._elementList[element_id - 1].clear()
        self._elementList[element_id - 1].send_keys(key)
        if log_output:
            self._Log.info(f'输入内容'
                           f' -> {self._elementDict[CONST_ELEMENT_PAGE_NAME]}'
                           f' -> {self._elementDict[CONST_ELEMENT_BUTTON_NAME]}'
                           f' -> [{key}]')

    def clear(self, element_id: int = 1, log_output: bool = True):
        """
        输入框清除内容

        :param element_id           : 元素列表下标
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._analytical_elements()
        self._elementList[element_id - 1].clear()
        if log_output:
            self._Log.info(f'清空内容'
                           f' -> {self._elementDict[CONST_ELEMENT_PAGE_NAME]}'
                           f' -> {self._elementDict[CONST_ELEMENT_BUTTON_NAME]}')

    def in_page(self, element_id: int = 1, wait: int = 3, log_output: bool = True):
        """
        判断元素是否存在当前可视页面

        :param element_id           : 元素列表下标
        :param wait                 : 元素获取时长
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志

        :return                     : Bool
        """
        self._analytical_elements(wait=wait)

        if len(self._elementList) >= element_id:
            if log_output:
                self._Log.info(f'元素存在'
                               f' -> {self._elementDict[CONST_ELEMENT_PAGE_NAME]}'
                               f' -> {self._elementDict[CONST_ELEMENT_BUTTON_NAME]}'
                               f' -> [{element_id}]')
            return True

        else:
            if log_output:
                self._Log.info(f'元素不存在'
                               f' -> {self._elementDict[CONST_ELEMENT_PAGE_NAME]}'
                               f' -> {self._elementDict[CONST_ELEMENT_BUTTON_NAME]}'
                               f' -> [{element_id}]')
            return False


if __name__ == '__main__':
    pass

