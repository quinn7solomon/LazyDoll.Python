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

        该模块的职责在于构建程序组件

"""

import time

from appium.webdriver.webdriver import WebDriver

from core.common.log import Log
from core.testingkit.app.driverhandle import RegisteredDriver
from core.common.customize_exception import DevicePhysicalKeyException
from core.common.customize_exception import NetworkSwitchEventException


__all__ = ['ConstructorsApp']


class ConstructorsApp(object):
    """
    程序组件实现类 \n
    """

    # 日志服务
    _logServer = Log()

    # RegisteredDriver 实例
    _registeredDriver: RegisteredDriver = None
    # DriverCore 实例
    _driverCore: WebDriver = None

    def __init__(self, registered_driver: RegisteredDriver):
        """
        初始化 \n

        :param registered_driver : RegisteredDriver 对象
        """
        self._registeredDriver = registered_driver
        self._driverCore = registered_driver.get_driver_core()

    def sleep(self, sleep_time: int, log_output: bool = True):
        """
        应用休眠 \n

        :param sleep_time    : 休眠的时长，单位是秒
        :param log_output    : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        if log_output:
            self._logServer.info(f'Application goes to sleep in the background -> {sleep_time} s')
            self._driverCore.background_app(sleep_time)
            self._logServer.info('Application completes background sleep -> To revive')
        else:
            self._driverCore.background_app(sleep_time)

    def keyboard_home(self, number: int = 1, wait: int = 0, log_output: bool = True):
        """
        模拟设备物理键 - HOME键 \n

        :param number        : 按键次数
        :param wait          : 动作执行完毕的等待时长
        :param log_output    : 执行完毕后是否打印成功日志，False 则表示不输出成功日志
        """
        self._press_keys(3, number=number, wait=wait, key_name='Key-Home', log_output=log_output)

    def keyboard_back(self, number: int = 1, wait: int = 0, log_output: bool = True):
        """
        模拟设备物理键 - 返回键 \n
        """
        self._press_keys(4, number=number, wait=wait, key_name='Key-Back', log_output=log_output)

    def keyboard_supply(self, number: int = 1, wait: int = 0, log_output: bool = True):
        """
        模拟设备物理键 - 电源键 \n
        """
        self._press_keys(26, number=number, wait=wait, key_name='Key-Supply', log_output=log_output)

    def keyboard_volume_up(self, number: int = 1, wait: int = 0, log_output: bool = True):
        """
        模拟设备物理键 - 音量增加键 \n
        """
        self._press_keys(24, number=number, wait=wait, key_name='Key-VolumeUp', log_output=log_output)

    def keyboard_volume_down(self, number: int = 1, wait: int = 0, log_output: bool = True):
        """
        模拟设备物理键 - 音量减少键 \n
        """
        self._press_keys(25, number=number, wait=wait, key_name='Key-VolumeDown', log_output=log_output)

    def set_network_airplane_mode(self, log_output: bool = True):
        """
        切换网络 - 飞行模式 \n
        """
        self._set_network(1, 'Network-Airplane-Mode', log_output=log_output)

    def set_network_wifi(self, log_output: bool = True):
        """
        切换网络 - WIFI模式 \n
        """
        self._set_network(2, 'Network-Wifi', log_output=log_output)

    def set_network_data(self, log_output: bool = True):
        """
        切换网络 - 数据模式 \n
        """
        self._set_network(4, 'Network-Data', log_output=log_output)

    def set_network_all_on(self, log_output: bool = True):
        """
        切换网络 - 有网模式 \n
        """
        self._set_network(6, 'Network-All-On', log_output=log_output)

    def set_network_all_off(self, log_output: bool = True):
        """
        切换网络 - 无网模式 \n
        """
        self._set_network(0, 'Network-All-Off', log_output=log_output)

    def get_package(self) -> str:
        """
        获取应用的包名 \n

        :return package : 当前打开的应用包名
        """
        return self._driverCore.current_package

    def get_activity(self) -> str:
        """
        获取应用的启动名 \n

        :return activity : 当前打开的应用启动名
        """
        return self._driverCore.current_activity

    def get_screen(self, pc_path: str):
        """
        截取手机当前屏幕，保存至指定位置 \n

        :param pc_path : 截取图片所存放的 Pc 端绝对路径
        """
        self._driverCore.get_screenshot_as_file(pc_path)

    def app_is_installed(self, package: str) -> bool:
        """
        检查应用是否安装 \n

        :param package : APP应用的包名
        """
        return self._driverCore.is_app_installed(package)

    def app_install(self, apk_path):
        """
        应用安装 \n

        :param apk_path : APP应用的安装包路径
        """
        self._driverCore.install_app(apk_path)

    def app_uninstall(self, package: str):
        """
        应用卸载 \n

        :param package : APP应用的包名
        """
        self._driverCore.remove_app(package)

    def closed_keyboard(self):
        """
        收起键盘 \n
        """
        self._driverCore.hide_keyboard()

    def open_radio(self):
        """
        打开通知栏 \n
        """
        self._driverCore.open_notifications()

    def shake(self, number=1):
        """
        摇晃手机 \n

        :param number: 摇晃的次数
        """
        for rotate in range(number):
            self._driverCore.shake()

    def app_open(self):
        """
        启动配置中指定的应用 \n
        """
        self._driverCore.launch_app()

    def app_close(self):
        """
        关闭应用 \n
        """
        self._driverCore.close_app()

    def app_open_activity(self, app_name: str, package: str, activity: str, log_output: bool = True):
        """
        启动给定包名与启动名的应用 \n

        :param app_name             : 应用程序名称
        :param package              : 应用程序包名
        :param activity             : 应用程序启动名
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._driverCore.start_activity(package, activity)
        if log_output:
            self._logServer.info(f'Starts the application with the given package name and startup name -> {app_name}')

    # 重复调用的代码封装

    def _press_keys(self, key: int, number: int, wait: int, key_name: str, log_output: bool):
        """
        物理键事件，模拟物理键的一些操作 \n

        :param key                  : 物理键的编号
        :param number               : 按键次数
        :param wait                 : 按键的间隔时长
        :param key_name             : 按键名称
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        try:
            time.sleep(1)
            for rotate in range(number):
                self._driverCore.keyevent(key)
                time.sleep(wait)
            if log_output:
                self._logServer.info(f'Simulate pressing the physical key -> {key_name}')

        except Exception:
            raise DevicePhysicalKeyException

    def _set_network(self, net_key: int, net_name: str, log_output: bool):
        """
        网络切换事件 \n

        :param net_key              : 网络状态 key
        :param net_name             : 网络状态 name
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        try:
            self._driverCore.set_network_connection(net_key)
            if log_output:
                self._logServer.info(f'Switching network state -> {net_name}')

        except Exception:
            raise NetworkSwitchEventException


if __name__ == '__main__':
    pass

