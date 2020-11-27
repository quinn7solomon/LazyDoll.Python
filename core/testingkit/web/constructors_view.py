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

    Last Modified Time : 2020.11.27

    RegisteredDriver   :

        ConstructorsApp 由 Puppeteer 进行集成

        该模块的职责在于构建屏幕组件

"""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.touch_actions import TouchActions

from core.common.log import Log
from core.testingkit.web.driverhandle import RegisteredDriver


__all__ = ['ConstructorsView']


class ConstructorsView(object):
    """
    屏幕组件实现类 \n
    """

    # 日志服务
    _logServer = Log()

    # Driver 实例
    _registeredDriver: RegisteredDriver = None
    # DriverCore 实例
    _driverCore: WebDriver = None

    # TouchAction 类
    _touchAction = TouchActions

    def __init__(self, registered_driver: RegisteredDriver):
        """
        初始化 \n

        :param registered_driver : RegisteredDriver 对象
        """
        self._registeredDriver = registered_driver
        self._driverCore = registered_driver.get_driver_core()

    def max_windows(self, log_output: bool = True):
        """
        最大化浏览器窗口 \n

        :param log_output    : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._driverCore.maximize_window()
        if log_output:
            self._logServer.info(f'Browser Window Maximization')

    def min_windows(self, log_output: bool = True):
        """
        最小化浏览器窗口 \n

        :param log_output    : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._driverCore.minimize_window()
        if log_output:
            self._logServer.info(f'Browser Window Maximization')

    def get_window_size(self):
        """
        获取浏览器尺寸 \n
        """
        return self._driverCore.get_window_size()

    def set_window_size(self, width, height):
        """
        设置浏览器尺寸 \n

        :param width             : 宽度
        :param height            : 高度
        """
        self._driverCore.set_window_size(width, height)

    def get_window_position(self):
        """
        获取浏览器位置 \n
        """
        return self._driverCore.get_window_position()

    def set_window_position(self, x, y):
        """
        获取浏览器位置 \n

        :param x                 : x 坐标
        :param y                 : y 坐标
        """
        self._driverCore.set_window_position(x, y)

    def back(self):
        """
        回退到之前的页面 \n
        """
        self._driverCore.back()

    def forward(self):
        """
        前进到之后的页面 \n
        """
        self._driverCore.forward()

    def alert_get_text(self):
        """
        弹窗操作:: 获取弹窗文本 \n
        """
        return self._driverCore.switch_to.alert.text

    def alert_tap_accept(self, log_output: bool = True):
        """
        弹窗操作:: 点击确定 \n

        :param log_output    : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._driverCore.switch_to.alert.accept()
        if log_output:
            self._logServer.info('Alert Popups:: Tap Accept')

    def alert_tap_dismiss(self, log_output: bool = True):
        """
        弹窗操作:: 点击取消 \n

        :param log_output    : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._driverCore.switch_to.alert.dismiss()
        if log_output:
            self._logServer.info('Alert Popups:: Tap Dismiss')

    def alert_send_key(self, key: str, log_output: bool = True):
        """
        弹窗操作:: 输入文本 \n

        :param key           : 输入的内容
        :param log_output    : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._driverCore.switch_to.alert.send_keys(key)
        if log_output:
            self._logServer.info(f'Alert Popups:: Send Key -> [{key}]')

    def switch_to_frame(self, frame_property: str, log_output: bool = True):
        """
        切换框架:: frame \n

        规则:
            1. 如果存在多级框架时，框架必须一级一级往下切换，不可越级
            2. 切换新的框架时，必须先切换回主框架 -> switch_to_default_content()

        :param frame_property : frame 的 id 或者 name 属性
        :param log_output     : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._driverCore.switch_to.frame(frame_property)
        if log_output:
            self._logServer.info(f'Browser Switch Frame -> {frame_property}')

    def switch_to_default_content(self):
        """
        切换框架至主框架 \n
        :return:
        """
        self._driverCore.switch_to.default_content()

    def swipe_location(self, altitude, log_output: bool = True):
        """
        页面滑动:: 滑动到指定的高度 \n

        :param altitude       : 指定的高度
        :param log_output     : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        js = f'var q=document.documentElement.scrollTop={altitude}'
        self._driverCore.execute_script(js)
        if log_output:
            self._logServer.info(f'The Page Swipe To -> {altitude}')

    def swipe_top(self):
        self.swipe_location(7777)

    def swipe_down(self):
        self.swipe_location(0)


if __name__ == '__main__':
    pass

