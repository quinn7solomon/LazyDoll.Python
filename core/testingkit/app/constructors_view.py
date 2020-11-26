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

import time

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.touch_action import TouchAction

from core.common.log import Log
from core.testingkit.app.driver import Driver


__all__ = ['ConstructorsView']


class ConstructorsView(object):
    """
    屏幕组件实现类
    """
    # 日志服务
    _Log = Log()

    # Driver 实例
    _driver: Driver = None
    # DriverCore 实例
    _driverCore: WebDriver = None

    # TouchAction 类
    _touchAction = TouchAction

    def __init__(self, driver):
        """
        初始化

        :param driver        : Driver 实例
        """
        self._driver = driver
        self._driverCore = driver.driverObj

    def adaption_swipe_up(self, speed: int = 1000, number: int = 1, wait: int = 1, log_output: bool = True):
        """
        自适应滑动屏幕 Up ↑
        """
        self._adaption_swipe(x1=0.5, y1=0.25, x2=0.5, y2=0.75,
                             direction='向上滑屏', speed=speed, number=number, wait=wait, log_output=log_output)

    def adaption_swipe_down(self, speed: int = 1000, number: int = 1, wait: int = 1, log_output: bool = True):
        """
        自适应滑动屏幕 down ↓
        """
        self._adaption_swipe(x1=0.5, y1=0.75, x2=0.5, y2=0.25,
                             direction='向下滑屏', speed=speed, number=number, wait=wait, log_output=log_output)

    def adaption_swipe_left(self, speed: int = 1000, number: int = 1, wait: int = 1, log_output: bool = True):
        """
        自适应滑动屏幕 left ←
        """
        self._adaption_swipe(x1=0.25, y1=0.5, x2=0.75, y2=0.5,
                             direction='向左滑屏', speed=speed, number=number, wait=wait, log_output=log_output)

    def adaption_swipe_right(self, speed: int = 1000, number: int = 1, wait: int = 1, log_output: bool = True):
        """
        自适应滑动屏幕 right →
        """
        self._adaption_swipe(x1=0.75, y1=0.5, x2=0.25, y2=0.5,
                             direction='向右滑屏', speed=speed, number=number, wait=wait, log_output=log_output)

    def tap_xy(self, x: int, y: int, log_output: bool = True):
        """
        模拟一次指向 x, y 坐标上的点击操作

        值得注意的是，不同的设备分辨率会导致固定像素的坐标落点存在差异，推荐使用自适应点击函数 tap_xy_adaption

        :param x                    : 明确的 x 坐标
        :param y                    : 明确的 y 坐标
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        try:
            self._touchAction(self._driverCore).tap(x=x, y=y).perform()

            if log_output:
                self._Log.info(f'指向坐标的点击事件 -> x: {x}, y: {y}')

        except Exception as err:
            self._Log.error(f'指向坐标的点击事件，详情信息: {err}')
            raise

    def tap_xy_adaption(self, x: int, y: int):
        """
        模拟一次作用于坐标百分比上的点击操作
        """
        size = self._driverCore.get_window_size()
        self.tap_xy(x=size['width'] * x, y=size['height'] * y)

    # 重复调用的代码封装

    def _adaption_swipe(self, x1: float, y1: float, x2: float, y2: float,
                        direction: str, speed: int = 1000, number: int = 1, wait: int = 1, log_output: bool = True):
        """
        自适应滑动

        :param x1                   : float 类型，表示当前设备屏幕百分比
        :param y1                   : float 类型，表示当前设备屏幕百分比
        :param x2                   : float 类型，表示当前设备屏幕百分比
        :param y2                   : float 类型，表示当前设备屏幕百分比
        :param direction            : 滑动方向
        :param speed                : 滑动速度
        :param number               : 滑动次数
        :param wait                 : 滑动前的等待时长
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        try:
            size = self._driverCore.get_window_size()

            for rotate in range(number):
                time.sleep(wait)
                self._driverCore.swipe(size['width'] * x1, size['height'] * y1,
                                       size['width'] * x2, size['height'] * y2, speed)
            if log_output:
                self._Log.info(f'自适应滑动屏幕 -> {direction}')

        except Exception as err:
            self._Log.error(f'自适应滑动事件，详情信息: {err}')
            raise


if __name__ == '__main__':
    pass

