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

import yaml


__all__ = ['Tools']


class Tools(object):
    """
    工具类
    """

    @staticmethod
    def load_from_yaml(file_path: str, mode: str = 'r', coding: str = 'utf-8') -> dict:
        """
        读取 Yaml 格式文件数据

        :param file_path             : 文件路径
        :param mode                  : 打开模式
        :param coding                : 编码格式

        :return                      : 解析后的文件数据字典
        """
        try:
            with open(file_path, mode, encoding=coding) as fp:
                return yaml.load(fp, Loader=yaml.FullLoader)

        except BaseException:
            raise FileNotFoundError


if __name__ == '__main__':
    pass


