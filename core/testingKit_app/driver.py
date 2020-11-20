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

from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from core.common.log import Log
from core.common.tools import Tools

from core.testingKit_app.const import *


__all__ = ['Driver']


class Driver(object):
    """
    Driver 设备驱动模块
    """

    # 日志服务
    _Log = Log()

    # Driver 实例
    driverObj = None

    # 配置文件路径
    _configPath = None

    # 配置参数容器
    _configData = None

    def __init__(self, config_path: str, interface: str = '4723'):
        """
        初始化，生成 Android / Ios 设备的 driver 驱动器

        :param config_path        : Yaml 格式的配置文件绝对路径
        :param interface          : Appium Server 使用的端口
        """
        try:
            self._configPath = config_path
            self._configData = Tools.load_from_yaml(self._configPath)

            self.driverObj = webdriver.Remote(f'http://localhost:{interface}/wd/hub', self._configData)

            self._Log.info('Driver has started .. >> running')

        except Exception as err:
            self._Log.warning(f'Driver 配置解析失败，详情信息: {err}')

    def quit(self):
        """
        安全退出
        """
        self.driverObj.quit()

        self._Log.info('Driver be destroyed .. >> end')

    def find_element(self, element_dict: dict, wait: int = 20):
        """
        获取元素列表

        该函数返回一个元素列表，通过下标进行切片提取 WebElement 对象

        定位满足条件的某个元素，获取不到则根据容错值 tolerance 决定是否抛出错误或者返回 None 值

        容错机制的设定使得该函数可以当作判定元素是否存在当前页面的条件来使用

        而参数 log_output 能够决定是否输出容错日志，因为有些时候，我们并不需要这些日志
        """
        dore = self.driverObj

        if CONST_ANCHOR_ELEMENT in element_dict.keys():
            anchor_ele = self.__finds_all_packaging_logical_thinking(
                element_dict[CONST_ANCHOR_ELEMENT][CONST_ELEMENT_BY],
                element_dict[CONST_ANCHOR_ELEMENT][CONST_ELEMENT_EL],
                self.driverObj, wait, tolerance=False, log_output=False)

            dore = anchor_ele
            if CONST_ELEMENT_ID in element_dict[CONST_ANCHOR_ELEMENT]:
                print()
                dore = dore[element_dict[CONST_ANCHOR_ELEMENT][CONST_ELEMENT_ID] - 1]

        r_module = self.__finds_all_packaging_logical_thinking(
            element_dict[CONST_ELEMENT_BY],
            element_dict[CONST_ELEMENT_EL],
            dore, wait, tolerance=False, log_output=False)

        # 携带 CONST_ELEMENT_ID 参数时，会返回一个只包含该下标元素的列表
        if CONST_ELEMENT_ID in element_dict.keys():
            return [r_module[element_dict[CONST_ELEMENT_ID] - 1]]

        return r_module

    # 重复调用的代码封装

    def __finds_all_packaging_logical_thinking(self, by: str, el: str, dore: WebDriver,
                                               wait: int, tolerance: bool, log_output: bool):
        """
        find 系列函数的运行逻辑封装

        返回一个包含 ElementOperation 对象的列表

        :param by                   : 通过什么方法定位元素，如 id, class, xpath
        :param el                   : 相应方法所对应的元素的属性值
        :param dore                 : Driver对象或者锚元素对象
        :param wait                 : 查找元素所等待的等待时长，若开启容错机制应该尽量减少等待时长提高执行效率
        :param tolerance            : 容错模式，为 True 则表示定位不到元素也不报错，返回 None 值
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志

        :return                     : WebElement 对象列表 / None 值
        """
        try:
            obtain = WebDriverWait(dore, wait, ignored_exceptions=None).\
                until(ec.presence_of_all_elements_located((by, el)))

            return obtain

        except Exception as err:
            if tolerance:
                if log_output:
                    self._Log.info(f'Driver 获取不到元素，但容错机制返回None，详情信息: {err}')
                return None

            else:
                if log_output:
                    self._Log.info(f'Driver 获取不到元素，抛出错误，详情信息: {err}')
                raise


if __name__ == '__main__':
    pass

