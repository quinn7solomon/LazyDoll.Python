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

        GuiQuickStart 模块实现了项目快速启动 测试Case 的 WindowsGui 可视化操作界面

"""

import os
import time
import shutil

from dearpygui import core
from dearpygui import simple

from core.common.log import Log
from core.const import GlobalVariate


__all__ = ['GuiQuickStart']


class GuiQuickStart(object):
    """
    测试方案快速启动窗口
    """

    # 日志服务
    _Log = Log()

    guiWindowTitle = 'LazyDoll_Python :: Quick Start Testing'
    guiWindowWidth = 500
    guiWindowHeight = 300

    # 测试方案的 Cases 列表
    caseNameList = ['running all case']

    def __init__(self):
        core.set_main_window_title(self.guiWindowTitle)
        core.set_main_window_size(self.guiWindowWidth, self.guiWindowHeight)
        core.set_main_window_resizable(False)

        for case_name in GlobalVariate.DIR_PATH_CASES.glob('test_*.py'):
            self.caseNameList.append(case_name.name)

        # 注册Value : 默认测试报告名称
        core.add_value('reports_name', f'{GlobalVariate.ROOT_NAME}_report')

    def _running_callback(self, sender, data):
        """
        Running 回调函数
        """
        try:
            if core.get_value('##CasesNameListCombo') != '':

                # 生成测试用例运行路径
                running_case = self.get_running_case_name()
                # 生成测试报告的输出路径
                reports_output_path = self.get_output_reports_path()
                # 测试报告 xml 中间文件路径拼接
                reports_output_path_xml = str(reports_output_path) + 'xml'
                # 运行测试
                os.system(f'pytest -v {running_case} --alluredir={reports_output_path_xml}')
                # 测试报告 xml 转 http
                os.system(f'allure generate {reports_output_path_xml} -o {reports_output_path} --clean')
                # 递归删除测试报告 xml 中间文件
                shutil.rmtree(f'{reports_output_path_xml}', ignore_errors=True)
            else:
                print('Selection Case Is Empty')

        except Exception as err:
            self._Log.error(f'GUI可视化页面Running回调函数异常: {err}')
            raise

    def running_windows(self):
        """
        渲染窗口组件
        """
        with simple.window(name='main_windows'):
            core.add_text('FrameName    : LazyDoll_Python')
            core.add_text('CreatorName  : Quinn7k')
            core.add_text('CreationTime : 2020.11.19')

            core.add_spacing(count=2)
            core.add_separator()
            core.add_spacing(count=2)

            # 测试方案的名称与路径
            core.add_text(f'Testing Scheme Name    : {GlobalVariate.ROOT_NAME}')
            core.add_text(f'Testing Scheme Path    : {str(GlobalVariate.ROOT_PATH)}')

            core.add_spacing(count=2)
            core.add_separator()
            core.add_spacing(count=2)

            # 选择需要运行的Case
            core.add_text('Selected Run Case : ')
            core.add_same_line()
            core.add_combo('##CasesNameListCombo', items=self.caseNameList)

            # 输出测试报告的名称
            core.add_text('     Reports Name : ')
            core.add_same_line()
            core.add_input_text('##ReportsName', default_value=core.get_value('reports_name'))

            core.add_spacing(count=2)
            core.add_separator()
            core.add_spacing(count=2)

            core.add_button('Running Testing ...', width=self.guiWindowWidth, height=50,
                            tip='Run the selected test case, and output the test report document',
                            callback=self._running_callback)

        core.start_dearpygui(primary_window='main_windows')

    @staticmethod
    def get_running_case_name():
        """
        生成测试用例运行路径
        """
        selected_case_name = core.get_value('##CasesNameListCombo')
        if selected_case_name == 'running all case':
            return GlobalVariate.DIR_PATH_CASES
        else:
            return GlobalVariate.DIR_PATH_CASES.joinpath(selected_case_name)

    @staticmethod
    def get_output_reports_path():
        """
        生成测试报告的输出路径
        """
        current_timestamp = time.strftime('%Y%m%d', time.localtime())
        reports_name = core.get_value('##ReportsName') + '-' + current_timestamp

        reports_output_path = GlobalVariate.DIR_PATH_REPORTS.joinpath(reports_name)
        if reports_output_path.exists():
            i = 1
            while True:
                reports_output_path = GlobalVariate.DIR_PATH_REPORTS.joinpath(reports_name + '-' + str(i))
                if reports_output_path.exists():
                    i += 1
                    continue
                break
        return reports_output_path


if __name__ == '__main__':
    pass

