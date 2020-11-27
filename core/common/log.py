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

"""

import logging

from core.const import GlobalVariate


__all__ = ['Log']


class Log(object):
    """
    日志类 \n
    """

    # 日志对象实例
    loggingObject = None

    # 日志配置字典
    configureDict = {
        'logging_level': 'INFO',
        'streamHandler_level': 'INFO',

        'fileHandler_list': {

            'debug_file': {
                'name': f'{GlobalVariate.ROOT_NAME}_DeBug.log',
                'level': 'DEBUG',
            },

            'info_file': {
                'name': f'{GlobalVariate.ROOT_NAME}_Info.log',
                'level': 'INFO',
            },

            'error_file': {
                'name': f'{GlobalVariate.ROOT_NAME}_Error.log',
                'level': 'ERROR',
            },

            'warning_file': {
                'name': f'{GlobalVariate.ROOT_NAME}_Warning.log',
                'level': 'WARNING',
            },
        }
    }

    # 日志的输出格式定义
    logOutputStructure = '[%(asctime)s] [%(process)d] [%(levelname)8s] --->> %(message)s'

    def __new__(cls, *args, **kwargs):
        """
        单例创建 \n

        实例化该类的时候会调用 __new__ 函数，判断 loggingObj 是否为 None，若存在则引用，否则才会创建一个实例

        :return loggingObj         : 日志处理器实例对象
        """

        if not cls.loggingObject:
            cls.loggingObject = logging.getLogger()

            log_formatter = logging.Formatter(cls.logOutputStructure)

            cls.loggingObject.setLevel(cls.configureDict['logging_level'])
            cls.loggingObject.handlers.clear()

            streamHandler = logging.StreamHandler()
            streamHandler.setFormatter(log_formatter)
            streamHandler.setLevel(cls.configureDict['streamHandler_level'])

            cls.loggingObject.addHandler(streamHandler)

            for key, value in cls.configureDict['fileHandler_list'].items():
                log_file_handle = logging.FileHandler(f'{GlobalVariate.DIR_PATH_LOG.joinpath(value["name"])}')
                log_file_handle.setLevel(value['level'])
                log_file_handle.setFormatter(log_formatter)
                cls.loggingObject.addHandler(log_file_handle)

        return cls.loggingObject


if __name__ == '__main__':
    pass

