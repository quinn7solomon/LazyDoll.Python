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

    Definition of use case priority/level:

                            Blocker      : 中断缺陷
                            Critical     : 十分严重的缺陷
                            Major        : 较为严重的缺陷
                            Normal       : 普通缺陷
                            Minor        : 次要缺陷
                            Trivial      : 轻微缺陷
                            Enhancement  : 测试建议

"""

import allure

from core.common.log import Log
from core.const import GlobalVariate
from core.testingkit.app.driverhandle import DriverHandle

from demos.testing_app.modes.mode_system import ModeSystem


@allure.feature('模拟器系统自带程序测试')
class Test01CaseSystem(object):

    # 日志服务
    Log = Log()

    # DriverHandle 示例
    DriverHandle = DriverHandle()
    # RegisteredDriver 实例
    RegisteredDriver = DriverHandle.get_driver(GlobalVariate.DIR_PATH_CONFIG.joinpath('android_8.1.0.yaml'))

    # 元素模型
    ModeSystem = ModeSystem(RegisteredDriver)

    @classmethod
    def setup_class(cls):
        """
        类级别的初始化操作，在类开始的时候运行
        """

    @classmethod
    def teardown_class(cls):
        """
        类级别的销毁操作，在类结束的时候运行
        """
        # 全部用例执行完毕后销毁 Driver进程
        cls.RegisteredDriver.quit()

    def setup_method(self):
        """
        函数级别的初始化操作，在函数开始的时候运行
        """

    def teardown_method(self):
        """
        函数级别的销毁操作，在函数结束的时候运行
        """
        # 用例函数执行完毕后，需要保证当前页面回到'起点'
        # 所有用例函数都将从某个'起点'开始执行，从而保证用例的安全与连贯
        self.ModeSystem.app.keyboard_home(log_output=False)

    @allure.severity('Blocker')
    @allure.story('点击首页向上箭头进入应用程序视图')
    def test_001_open_app_view(self):
        """
        用例描述:
        点击首页向上箭头进入应用程序视图

        用例成功凭证: '顶部搜索框'存在于当前可视页面
        """
        try:
            self.ModeSystem.home_upward_arrows.tap()

            r = self.ModeSystem.app_view_top_search.in_page()
            assert r

        except Exception as err:
            self.Log.error(f'用例执行失败: 点击首页向上箭头进入应用程序视图: {err}')
            assert False

    @allure.severity('Blocker')
    @allure.story('通过顶部搜索框输入Calculator搜索计算器')
    def test_002_search_calculate(self):
        """
        用例描述:
        通过顶部搜索框输入Calculator搜索计算器

        用例成功凭证: '应用程序列表'首个应用程序为'Calculator'
        """
        try:
            self.ModeSystem.home_upward_arrows.tap()
            self.ModeSystem.app_view_top_search.send_key('Calculator')

            r = self.ModeSystem.app_view_app_list.get_text(1)
            assert r == 'Calculator'

        except Exception as err:
            self.Log.error(f'用例执行失败: 通过顶部搜索框输入Calculator搜索计算器: {err}')
            assert False

    @allure.severity('Blocker')
    @allure.story('打开计算机并计算1+1=2')
    def test_003_calculate_add(self):
        """
        用例描述:
        打开计算机并计算1+1=2

        用例成功凭证: 计算机的计算结果为'2'
        """
        try:
            self.ModeSystem.home_upward_arrows.tap()
            self.ModeSystem.app_view_top_search.send_key('Calculator')
            self.ModeSystem.app_view_app_list.tap(1)
            self.ModeSystem.calculator_keyboard_int(1).tap()
            self.ModeSystem.calculator_keyboard_add.tap()
            self.ModeSystem.calculator_keyboard_int(1).tap()
            self.ModeSystem.calculator_keyboard_eq.tap()
            r = self.ModeSystem.calculator_keyboard_result.get_text()
            assert r == '2'

        except Exception as err:
            self.Log.error(f'用例执行失败: 打开计算机并计算1+1=2: {err}')
            assert False


if __name__ == '__main__':
    pass

