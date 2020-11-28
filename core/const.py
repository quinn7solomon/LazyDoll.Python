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

"""
import pathlib


__all__ = ['Const', 'GlobalVariate']


class Const(object):
    """
    常量代理 \n
    """

    # 常量:: 元素Key
    ELEMENT_BY = 'ELEMENTS_BY'
    ELEMENT_EL = 'ELEMENTS_EL'
    ELEMENT_ID = 'ELEMENTS_ID'
    ELEMENT_PAGE_NAME = 'ELEMENTS_PAGE_NAME'
    ELEMENT_ELEMENT_NAME = 'ELEMENT_ELEMENT_NAME'
    ANCHOR_ELEMENT_BY = 'ANCHOR_ELEMENT_BY'
    ANCHOR_ELEMENT_EL = 'ANCHOR_ELEMENT_EL'
    ANCHOR_ELEMENT_ID = 'ANCHOR_ELEMENT_ID'

    # 常量:: 驱动器类型
    DRIVER_TYPE_APPIUM = 'DRIVER_TYPE_APPIUM'
    DRIVER_TYPE_BROWSER_CHROME = 'DRIVER_TYPE_BROWSER_CHROME'
    DRIVER_TYPE_BROWSER_FIREFOX = 'DRIVER_TYPE_BROWSER_FIREFOX'
    DRIVER_TYPE_BROWSER_EDGE = 'DRIVER_TYPE_BROWSER_EDGE'


class GlobalVariate(object):
    """
    全局变量代理 \n
    """

    # 测试方案目录名称映射字典
    GLOBAL_MAPPING_DIR = {
        'DIR_NAME_CASES': 'cases',
        'DIR_NAME_CONFIG': 'configure',
        'DIR_NAME_LOG': 'logs',
        'DIR_NAME_MODES': 'modes',
        'DIR_NAME_PACKAGES': 'packages',
        'DIR_NAME_REPORTS': 'reports',
    }

    # 项目根目录路径
    ROOT_PATH = pathlib.Path().cwd()
    # 项目名称
    ROOT_NAME = ROOT_PATH.name
    # 测试用例存放目录 Path
    DIR_PATH_CASES = ROOT_PATH.joinpath(GLOBAL_MAPPING_DIR['DIR_NAME_CASES'])
    # 配置文件存放目录 Path
    DIR_PATH_CONFIG = ROOT_PATH.joinpath(GLOBAL_MAPPING_DIR['DIR_NAME_CONFIG'])
    # 日志文件存放目录 Path
    DIR_PATH_LOG = ROOT_PATH.joinpath(GLOBAL_MAPPING_DIR['DIR_NAME_LOG'])
    # 元素模型存放目录 Path
    DIR_PATH_MODES = ROOT_PATH.joinpath(GLOBAL_MAPPING_DIR['DIR_NAME_MODES'])
    # 应用包存放目录 Path
    DIR_PATH_APK = ROOT_PATH.joinpath(GLOBAL_MAPPING_DIR['DIR_NAME_PACKAGES'])
    # 测试报告存放目录 Path
    DIR_PATH_REPORTS = ROOT_PATH.joinpath(GLOBAL_MAPPING_DIR['DIR_NAME_REPORTS'])


if __name__ == '__main__':
    pass

