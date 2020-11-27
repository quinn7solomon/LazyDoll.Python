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

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from core.testingkit.web.driverhandle import RegisteredDriver

from core.common.log import Log
from core.common.customize_exception import DevicePhysicalKeyException
from core.common.customize_exception import NewWindowsNameExistException


__all__ = ['ConstructorsApp']


class ConstructorsApp(object):
    """
    程序组件实现类 \n
    """

    # 日志服务
    _logServer = Log()

    # Driver 实例
    _registeredDriver: RegisteredDriver = None
    # DriverCore 实例
    _driverCore: WebDriver = None

    # 页面句柄字典
    _window_handles_dict = {}
    # 当前浏览器所在标签页
    _present_windows = 'main_windows'

    def __init__(self, registered_driver: RegisteredDriver):
        """
        初始化 \n

        :param registered_driver : RegisteredDriver 对象
        """
        self._registeredDriver = registered_driver
        self._driverCore = registered_driver.get_driver_core()

        self._window_handles_dict['main_windows'] = self._driverCore.current_window_handle

    def open_new_windows(self, windows_name: str, url: str = '', log_output: bool = True):
        """
        打开一个新的标签页 \n

        :param windows_name  : 标签页的名称，用以切换窗口句柄时识别
        :param url           : 如果不为空，则在新的标签页中跳转指定URL
        :param log_output    : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        if windows_name not in self._window_handles_dict.keys():
            self._driverCore.execute_script(f'window.open("{url}");')

            self._window_handles_dict[windows_name] = self._driverCore.window_handles[-1]
            self.switch_to_windows(windows_name)

            if log_output:
                self._logServer.info(f'Browser Open New Windows， Url -> {url}')

        else:
            raise NewWindowsNameExistException

    def switch_to_windows(self, windows_name, log_output: bool = True):
        """
        切换标签句柄 \n

        :param windows_name  : 需要切换至的标签名称
        :param log_output    : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        if windows_name in self._window_handles_dict.keys():
            self._driverCore.switch_to.window(self._window_handles_dict[windows_name])
            self._present_windows = windows_name

            if log_output:
                self._logServer.info(f'Browser Switch Handle -> {windows_name}')

        else:
            raise NewWindowsNameExistException

    def close_windows(self, windows_name, log_output: bool = True):
        """
        关闭标签页 \n

        :param windows_name  : 需要关闭的标签名称
        :param log_output    : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        if windows_name in self._window_handles_dict.keys():
            self.switch_to_windows(windows_name, log_output=False)
            self._driverCore.close()

            self._window_handles_dict.pop(self._present_windows)
            self.switch_to_windows(list(self._window_handles_dict.keys())[-1], log_output=False)

            if log_output:
                self._logServer.info(f'Browser Close Windows -> {windows_name}')

        else:
            raise NewWindowsNameExistException

    def close_all_windows(self, log_output: bool = True):
        """
        关闭所有窗口 \n

        :param log_output    : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._driverCore.quit()
        self._driverCore.switch_to.frame()
        if log_output:
            self._logServer.info('Browser Close All Windows')

    def goto_url(self, url: str, log_output: bool = True):
        """
        浏览器跳转到指定URL \n

        :param url           : 跳转指定URL
        :param log_output    : 执行完毕后是否打印容错日志，False 则表示不输出容错日志
        """
        self._driverCore.get(url)
        if log_output:
            self._logServer.info(f'Browser Goto Url -> {url}')

    def get_url(self):
        """
        获取当前页面的URL \n
        """
        return self._driverCore.current_url

    def get_title(self):
        """
        获取当前浏览器标题 \n
        """
        return self._driverCore.title

    def refresh(self):
        """
        刷新页面 \n
        """
        self._driverCore.refresh()

    def get_cookies(self):
        """
        获取所有 cookies \n
        """
        return self._driverCore.get_cookies()

    def get_cookie(self, cookie_name):
        """
        获取指定 cookies \n

        :param cookie_name   : cookies名称
        """
        return self._driverCore.get_cookie(cookie_name)

    def add_cookie(self, cookie_dict):
        """
        设置 cookies \n

        :param cookie_dict   : cookies
        """
        self._driverCore.add_cookie(cookie_dict)

    def delete_cookie(self, cookie_name):
        """
        删除指定 cookies \n

        :param cookie_name   : cookies名称
        """
        self._driverCore.delete_cookie(cookie_name)

    def delete_all_cookie(self):
        """
        删除所有 cookies \n
        """
        self._driverCore.delete_all_cookies()

    def save_snapshot_to_png(self, save_png_path):
        """
        保存快照 \n

        :param save_png_path     : 保存 快照Png 的路径
        """
        return self._driverCore.get_screenshot_as_file(save_png_path)

    def keyboard_space(self, number: int = 1, wait: int = 0, log_output: bool = True):
        """
        模拟设备物理键 - 空格键 \n

        :param number        : 按键次数
        :param wait          : 动作执行完毕的等待时长
        :param log_output    : 执行完毕后是否打印成功日志，False 则表示不输出成功日志
        """
        self._press_keys(Keys.SPACE, number=number, wait=wait, key_name='Space', log_output=log_output)

    def keyboard_backspace(self, number: int = 1, wait: int = 0, log_output: bool = True):
        """
        模拟设备物理键 - 删除键 \n
        """
        self._press_keys(Keys.BACK_SPACE, number=number, wait=wait, key_name='Backspace', log_output=log_output)

    def keyboard_tab(self, number: int = 1, wait: int = 0, log_output: bool = True):
        """
        模拟设备物理键 - 制表键 \n
        """
        self._press_keys(Keys.TAB, number=number, wait=wait, key_name='Tab', log_output=log_output)

    def keyboard_esc(self, number: int = 1, wait: int = 0, log_output: bool = True):
        """
        模拟设备物理键 - 回退键 \n
        """
        self._press_keys(Keys.ESCAPE, number=number, wait=wait, key_name='Esc', log_output=log_output)

    def keyboard_enter(self, number: int = 1, wait: int = 0, log_output: bool = True):
        """
        模拟设备物理键 - 回车键 \n
        """
        self._press_keys(Keys.ENTER, number=number, wait=wait, key_name='Enter', log_output=log_output)

    def keyboard_ctrl_add_key(self, key, number: int = 1, wait: int = 0, log_output: bool = True):
        """
        模拟设备物理键 - Ctrl + key \n
        """
        self._press_keys(Keys.CONTROL + key, number=number, wait=wait, key_name=f'Ctrl + {key}', log_output=log_output)

    # 重复调用的代码封装

    def _press_keys(self, key: str, number: int, wait: int, key_name: str, log_output: bool):
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
                ActionChains(self._driverCore).send_keys(key).perform()
                time.sleep(wait)
            if log_output:
                self._logServer.info(f'Simulate pressing the physical key -> {key_name}')

        except Exception:
            raise DevicePhysicalKeyException


if __name__ == '__main__':
    pass

