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

        ConstructorsApp 由 Puppeteer 进行集成

        该模块的职责在于构建元素组件

"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webdriver import WebDriver

from core.common.log import Log
from core.common.element_structure import ElementStructure
from core.common.customize_exception import ModuleTapEventException
from core.common.customize_exception import ModuleLongTapEventException
from core.common.customize_exception import ModuleSendKeyEventException

from core.testingkit.web.driverhandle import RegisteredDriver


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

    def _analytical_elements(self, wait: int = 3):
        """
        解析函数 \n
        """
        self._elementContainer = self._registeredDriver.find_element(self._elementStructure, wait)

    def get_element_len(self, log_output: bool = True):
        """
        获取元素的数量 \n

        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._analytical_elements()
        element_len = len(self._elementContainer)

        if log_output:
            self._logServer.info(f'Element Len'
                                 f' -> {self._elementStructure.page_name}'
                                 f' -> {self._elementStructure.element_name}'
                                 f' -> [{element_len}]')

        return element_len

    def get_text(self, element_id: int = 1, log_output: bool = True):
        """
        获取元素的 text 属性 \n

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

    def tap(self, element_id: int = 1, log_output: bool = True):
        """
        模拟一次作用于 WebElement 对象上的单击操作 \n

        :param element_id           : 元素列表下标
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        try:
            self._analytical_elements()
            element_text = self._elementContainer[element_id - 1].text

            ActionChains(self._driverCore).click(self._elementContainer[element_id - 1]).perform()

            if log_output:
                log_output_info = f'Tap Event' \
                                  f' -> {self._elementStructure.page_name} ' \
                                  f'-> {self._elementStructure.element_name}'

                if element_text != '':
                    log_output_info += f' -> [{element_text}]'

                self._logServer.info(log_output_info)

        except Exception:
            raise ModuleTapEventException

    def double_tap(self, element_id: int = 1, log_output: bool = True):
        """
        模拟一次作用于 WebElement 对象上的双击操作 \n

        :param element_id           : 元素列表下标
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        try:
            self._analytical_elements()
            element_text = self._elementContainer[element_id - 1].text

            ActionChains(self._driverCore).double_click(self._elementContainer[element_id - 1]).perform()

            if log_output:
                log_output_info = f'Double Tap Event' \
                                  f' -> {self._elementStructure.page_name} ' \
                                  f'-> {self._elementStructure.element_name}'

                if element_text != '':
                    log_output_info += f' -> [{element_text}]'

                self._logServer.info(log_output_info)

        except Exception:
            raise ModuleTapEventException

    def long_tap(self, element_id: int = 1, log_output: bool = True):
        """
        模拟一次作用于 WebElement 对象上的长按操作 \n

        :param element_id           : 元素列表下标
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        try:
            self._analytical_elements()
            element_text = self._elementContainer[element_id - 1].text

            ActionChains(self._driverCore).click_and_hold(self._elementContainer[element_id - 1]).perform()

            if log_output:
                log_output_info = f'Long Tap Event' \
                                  f' -> {self._elementStructure.page_name} ' \
                                  f'-> {self._elementStructure.element_name}'

                if element_text != '':
                    log_output_info += f' -> [{element_text}]'

                self._logServer.info(log_output_info)

        except Exception:
            raise ModuleLongTapEventException

    def mouse_move_to(self, element_id: int = 1, wait: int = 3, log_output: bool = True):
        """
        模拟一次作用于 WebElement 对象上的点击操作 \n

        :param element_id           : 元素列表下标
        :param wait                 : 鼠标悬停时间
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        try:
            self._analytical_elements()

            ActionChains(self._driverCore).move_to_element(self._elementContainer[element_id - 1]).perform()
            time.sleep(wait)

            if log_output:
                self._logServer.info(f'Mouse Move To Element'
                                     f' -> {self._elementStructure.page_name}'
                                     f' -> {self._elementStructure.element_name}'
                                     f' -> [{wait}s]')

        except Exception:
            raise ModuleTapEventException

    def send_key(self, key: str, element_id: int = 1, log_output: bool = True):
        """
        输入框输入内容 \n

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
        输入框清除内容 \n

        :param element_id           : 元素列表下标
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._analytical_elements()
        self._elementContainer[element_id - 1].clear()

        if log_output:
            self._logServer.info(f'Clear Event'
                                 f' -> {self._elementStructure.page_name}'
                                 f' -> {self._elementStructure.element_name}')

    def drop_down_box_select_index(self, index: int, element_id: int = 1, log_output: bool = True):
        """
        下拉框选择:: 通过索引 \n

        :param index                : 下拉框选项集索引
        :param element_id           : 元素列表下标
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._analytical_elements()
        select_object = Select(self._elementContainer[element_id - 1])
        select_object.select_by_index(index - 1)

        select_item_name = select_object.all_selected_options[0].text

        if log_output:
            self._logServer.info(f'DropDownBor Select Event'
                                 f' -> {self._elementStructure.page_name}'
                                 f' -> {self._elementStructure.element_name}'
                                 f' -> [{select_item_name}]')

    def drop_down_box_select_text(self, text: int, element_id: int = 1, log_output: bool = True):
        """
        下拉框选择:: 通过 text 值 \n

        :param text                 : 下拉框选项集的 text 值
        :param element_id           : 元素列表下标
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._analytical_elements()
        select_object = Select(self._elementContainer[element_id - 1])
        select_object.select_by_visible_text(text)

        select_item_name = select_object.all_selected_options[0].text

        if log_output:
            self._logServer.info(f'DropDownBor Select Event'
                                 f' -> {self._elementStructure.page_name}'
                                 f' -> {self._elementStructure.element_name}'
                                 f' -> [{select_item_name}]')

    def in_page(self, element_id: int = 1, wait: int = 3, log_output: bool = True):
        """
        判断元素是否存在当前可视页面 \n

        :param element_id           : 元素列表下标
        :param wait                 : 元素获取时长
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志

        :return                     : Bool
        """
        self._analytical_elements(wait=wait)

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

    def goto_element_location(self, element_id: int = 1, log_output: bool = True):
        """
        跳转至 元素 所在位置 \n

        :param element_id           : 元素列表下标
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._analytical_elements()
        self._driverCore.execute_script("arguments[0].scrollIntoView();", self._elementContainer[element_id - 1])
        if log_output:
            self._logServer.info(f'Goto Element Location'
                                 f' -> {self._elementStructure.page_name}'
                                 f' -> {self._elementStructure.element_name}')


if __name__ == '__main__':
    pass

