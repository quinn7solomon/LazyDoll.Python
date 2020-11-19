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

from core.common.log import Log


__all__ = ['ConstructorsApp']


class ConstructorsApp(object):
    """
    程序组件实现类
    """

    # 日志服务
    _Log = Log()

    # Driver 实例
    _driverObj = None

    def __init__(self, driver: WebDriver):
        """
        初始化

        :param driver        : Driver 实例
        """
        self._driverObj = driver

    def sleep(self, sleep_time: int, log_output: bool = True):
        """
        应用休眠

        :param sleep_time    : 休眠的时长，单位是秒
        :param log_output    : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        if log_output:
            self._Log.info(f'应用进入后台休眠 -> {sleep_time} 秒')
            self._driverObj.background_app(sleep_time)
            self._Log.info('应用完成后台休眠 -> 重新唤起')
        else:
            self._driverObj.background_app(sleep_time)

    def keyboard_home(self, number: int = 1, wait: int = 0, log_output: bool = True):
        """
        模拟设备物理键 - HOME键

        :param number        : 按键次数
        :param wait          : 动作执行完毕的等待时长
        :param log_output    : 执行完毕后是否打印成功日志，False 则表示不输出成功日志
        """
        self.__press_keys(3, number=number, wait=wait, key_name='HOME键', log_output=log_output)

    def keyboard_back(self, number: int = 1, wait: int = 0, log_output: bool = True):
        """
        模拟设备物理键 - 返回键
        """
        self.__press_keys(4, number=number, wait=wait, key_name='返回键', log_output=log_output)

    def keyboard_supply(self, number: int = 1, wait: int = 0, log_output: bool = True):
        """
        模拟设备物理键 - 电源键
        """
        self.__press_keys(26, number=number, wait=wait, key_name='电源键', log_output=log_output)

    def keyboard_voice_up(self, number: int = 1, wait: int = 0, log_output: bool = True):
        """
        模拟设备物理键 - 音量增加键
        """
        self.__press_keys(24, number=number, wait=wait, key_name='音量 + 键', log_output=log_output)

    def keyboard_voice_low(self, number: int = 1, wait: int = 0, log_output: bool = True):
        """
        模拟设备物理键 - 音量减少键
        """
        self.__press_keys(25, number=number, wait=wait, key_name='音量 - 键', log_output=log_output)

    def set_network_flight(self, log_output: bool = True):
        """
        切换网络 - 飞行模式
        """
        self.__set_network(1, '飞行模式', log_output=log_output)

    def set_network_wifi(self, log_output: bool = True):
        """
        切换网络 - WIFI模式
        """
        self.__set_network(2, 'WIFI模式', log_output=log_output)

    def set_network_data(self, log_output: bool = True):
        """
        切换网络 - 数据模式
        """
        self.__set_network(4, '数据模式', log_output=log_output)

    def set_network_all_on(self, log_output: bool = True):
        """
        切换网络 - 有网模式
        """
        self.__set_network(6, '有网模式', log_output=log_output)

    def set_network_all_off(self, log_output: bool = True):
        """
        切换网络 - 无网模式
        """
        self.__set_network(0, '无网模式', log_output=log_output)

    def get_package(self) -> str:
        """
        获取应用的包名

        :return package : 当前打开的应用包名
        """
        return self._driverObj.current_package

    def get_activity(self) -> str:
        """
        获取应用的启动名

        :return activity : 当前打开的应用启动名
        """
        return self._driverObj.current_activity

    def get_screen(self, pc_path: str):
        """
        截取手机当前屏幕，保存至指定位置

        :param pc_path : 截取图片所存放的 Pc 端绝对路径
        """
        self._driverObj.get_screenshot_as_file(pc_path)

    def app_is_installed(self, package: str) -> bool:
        """
        检查应用是否安装

        :param package : APP应用的包名
        """
        return self._driverObj.is_app_installed(package)

    def app_install(self, apk_path):
        """
        应用安装

        :param apk_path : APP应用的安装包路径
        """
        self._driverObj.install_app(apk_path)

    def app_uninstall(self, package: str):
        """
        应用卸载

        :param package : APP应用的包名
        """
        self._driverObj.remove_app(package)

    def closed_keyboard(self):
        """
        收起键盘
        """
        self._driverObj.hide_keyboard()

    def open_radio(self):
        """
        打开通知栏
        """
        self._driverObj.open_notifications()

    def shake(self, number=1):
        """
        摇晃手机

        :param number: 摇晃的次数
        """
        for rotate in range(number):
            self._driverObj.shake()

    def app_open(self):
        """
        启动应用
        """
        self._driverObj.launch_app()

    def app_close(self):
        """
        关闭应用
        """
        self._driverObj.close_app()

    # 重复调用的代码封装

    def __press_keys(self, key: int, number: int, wait: int, key_name: str, log_output: bool):
        """
        物理键事件，模拟物理键的一些操作

        :param key                  : 物理键的编号
        :param number               : 按键次数
        :param wait                 : 按键的间隔时长
        :param key_name             : 按键名称
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        try:
            time.sleep(1)
            for rotate in range(number):
                self._driverObj.keyevent(key)
                time.sleep(wait)
            if log_output:
                self._Log.info(f'模拟按下物理键 -> {key_name}')

        except Exception as err:
            self._Log.error(f'物理键事件异常，详情信息: {err}')
            raise

    def __set_network(self, net_key: int, net_name: str, log_output: bool):
        """
        网络切换事件

        :param net_key              : 网络状态 key
        :param net_name             : 网络状态 name
        :param log_output           : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        try:
            self._driverObj.set_network_connection(net_key)
            if log_output:
                self._Log.info(f'切换网络状态 -> {net_name}')

        except Exception as err:
            self._Log.error(f'网络切换事件异常，详情信息: {err}')
            raise


if __name__ == '__main__':
    pass

