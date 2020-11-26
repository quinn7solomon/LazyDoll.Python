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

import random

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from core.common.log import Log
from core.common.element_structure import ElementStructure
from core.common.customize_exception import FindElementException
from core.common.customize_exception import DriverNameRegisterException


class BaseDriverHandle(object):
    """
    Driver 设备驱动处理器 \n
    """

    # 日志服务
    _Log = Log()

    # 已注册的驱动器名称
    registeredDriverName = None
    # 已注册的驱动器列表
    _registeredDriverList = []
    # 已注册的驱动器映射字典
    _registeredDriverMapDict = {}

    def quit(self, driver_name: str):
        """
        销毁名为 driver_name 的已注册浏览器驱动 \n
        """
        if driver_name in self._registeredDriverList:
            self._registeredDriverMapDict[driver_name].quit()
            self._registeredDriverList.remove(driver_name)
            self._registeredDriverMapDict.pop(driver_name)

    def _register_driver_flow(self, driver_name: str or None, driver_core) -> str:
        """
        驱动器注册合法性验证 \n
        """
        if not driver_name:
            driver_name = f'{self.registeredDriverName}{random.randint(1000000, 9999999)}'

        if driver_name not in self._registeredDriverList:
            self._registeredDriverList.append(driver_name)
            self._registeredDriverMapDict[driver_name] = driver_core
            return driver_name

        raise DriverNameRegisterException(driver_name)

    def get_registered_driver_list(self):
        return self._registeredDriverList

    def get_registered_driver_map_dict(self):
        return self._registeredDriverMapDict


class BaseRegisteredDriver(object):
    """
    已注册的设备驱动类 \n
    """

    # 日志服务
    _logServer = Log()

    # Driver Core WebDriver Object
    _driverCore: WebDriver = None
    _driverName = None
    _driverType = None

    def __init__(self, driver_core, driver_name, driver_type):
        self._driverCore = driver_core
        self._driverName = driver_name
        self._driverType = driver_type

    def get_driver_core(self):
        return self._driverCore

    def get_driver_name(self):
        return self._driverName

    def get_driver_type(self):
        return self._driverType

    def quit(self):
        """
        安全退出驱动进程
        """
        self._driverCore.quit()

    def find_element(self, element_structure: ElementStructure,
                     wait: int = 20, tolerance: bool = False, log_output: bool = True) -> list:
        """
        元素定位函数 \n

        :param element_structure    : 元素结构体 ElementStructure 对象
        :param wait                 : 查找元素所等待的等待时长
        :param tolerance            : 容错模式，为 True 则表示定位不到元素也不报错，返回 None 值
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志

        :return                     : WebElement 对象列表 / None 值
        """
        try:
            restricted = self._get_search_range(element_structure, wait=wait)

            element_list = self._native_web_driver_wait_packaging(
                element_structure.by,
                element_structure.el,
                restricted, wait, tolerance, log_output)

            # 携带 CONST_ELEMENT_ID 参数时，会返回一个只包含该下标元素的列表
            if element_structure.id and tolerance is False:
                element_list = [element_list[element_structure.id - 1]]

            return element_list

        except Exception as err:
            self._logServer.info(f'common_find.find_element error: {err}')
            raise

    def find_element_exist(self, element_structure: ElementStructure, wait: int = 3, log_output: bool = True) -> bool:
        """
        定位元素是否存在于当前可视化页面 \n

        :param element_structure    : 元素结构体 ElementStructure 对象
        :param wait                 : 查找元素所等待的等待时长
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志

        :return                     : 表示元素是否存在于当前可视化页面中的布尔值
        """
        element_list = self.find_element(element_structure, wait, tolerance=True, log_output=log_output)
        if element_list is None:
            return False
        return True

    def _get_search_range(self, element_structure: ElementStructure, wait: int) -> WebElement or WebDriver:
        """
        获取元素搜索范围 \n

        如果 element_structure 不携带 ANCHOR_ELEMENT 锚元素对象则返回 WebDriver 对象， 否则 返回 WebElement 对象

        :return                     : WebElement 对象 / WebDriver 对象
        """
        try:
            search_range = self._driverCore

            if element_structure.anchor_by:
                search_range = self._native_web_driver_wait_packaging(
                    element_structure.anchor_by,
                    element_structure.anchor_el,
                    search_range, wait, tolerance=False, log_output=False)[element_structure.anchor_id - 1]

            return search_range

        except Exception as err:
            self._logServer.info(f'common_find._get_search_range error: {err}')
            raise

    def _native_web_driver_wait_packaging(self, by: str, el: str, driver, wait: int, tolerance: bool, log_output: bool):
        """
        原生 WebDriverWait 封装 \n

        :param by                   : 通过什么方法定位元素，如 id, class, xpath
        :param el                   : 相应方法所对应的元素的属性值
        :param driver               : Driver对象或者锚元素对象
        :param wait                 : 查找元素所等待的等待时长，若开启容错机制应该尽量减少等待时长提高执行效率
        :param tolerance            : 容错模式，为 True 则表示定位不到元素也不报错，返回 None 值
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志

        :return                     : WebElement 对象列表 / None 值
        """
        try:
            obtain = WebDriverWait(driver, wait, poll_frequency=0.5, ignored_exceptions=None).\
                until(ec.presence_of_all_elements_located((by, el)))

            return obtain

        except Exception as err:
            if tolerance:
                if log_output:
                    self._logServer.info(
                        'The element cannot be retrieved， '
                        f'but the Find fault-tolerant switch is true， returning []: {err}')
                return []

            else:
                raise FindElementException


if __name__ == '__main__':
    pass

