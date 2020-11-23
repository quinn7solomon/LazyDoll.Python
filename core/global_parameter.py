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

import pathlib


# 全局配置映射字典.目录列表名称
GLOBAL_MAPPING_DIR = {
    'DIR_NAME_CASES': 'cases',
    'DIR_NAME_CONFIG': 'configure',
    'DIR_NAME_LOG': 'logs',
    'DIR_NAME_MODES': 'modes',
    'DIR_NAME_PACKAGES': 'packages',
    'DIR_NAME_REPORTS': 'reports',
}

# 项目根目录路径
GLOBAL_ROOT_PATH = pathlib.Path().cwd()

# 项目名称
GLOBAL_ROOT_NAME = GLOBAL_ROOT_PATH.name

# 测试用例存放目录 Path
GLOBAL_DIR_PATH_CASES = GLOBAL_ROOT_PATH.joinpath(GLOBAL_MAPPING_DIR['DIR_NAME_CASES'])

# 配置文件存放目录 Path
GLOBAL_DIR_PATH_CONFIG = GLOBAL_ROOT_PATH.joinpath(GLOBAL_MAPPING_DIR['DIR_NAME_CONFIG'])

# 日志文件存放目录 Path
GLOBAL_DIR_PATH_LOG = GLOBAL_ROOT_PATH.joinpath(GLOBAL_MAPPING_DIR['DIR_NAME_LOG'])

# 元素模型存放目录 Path
GLOBAL_DIR_PATH_MODES = GLOBAL_ROOT_PATH.joinpath(GLOBAL_MAPPING_DIR['DIR_NAME_MODES'])

# 应用包存放目录 Path
GLOBAL_DIR_PATH_APK = GLOBAL_ROOT_PATH.joinpath(GLOBAL_MAPPING_DIR['DIR_NAME_PACKAGES'])

# 测试报告存放目录 Path
GLOBAL_DIR_PATH_REPORTS = GLOBAL_ROOT_PATH.joinpath(GLOBAL_MAPPING_DIR['DIR_NAME_REPORTS'])

# GUI 选择的 Driver 配置文件 Path
GLOBAL_GUI_SELECTED_DRIVER_CONFIG = None


if __name__ == '__main__':
    pass

