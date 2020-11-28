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

        ElementStructure 职责于解析元素信息字典并封装成了结构体

"""

from core.const import Const


class ElementStructure(object):
    """
    元素结构体 \n

    ElementStructure 构建协议:

        字典必须传递的常量:
            Const.ELEMENT_BY
            Const.ELEMENT_El
            Const.ELEMENT_PAGE_NAME
            Const.ELEMENT_ELEMENT_NAME

        若传递 ANCHOR_ELEMENT_BY 则必须同时传递以下常量:
            Const.ANCHOR_ELEMENT_BY
            Const.ANCHOR_ELEMENT_EL
            Const.ANCHOR_ELEMENT_ID

    """

    by = None
    el = None
    id = None
    page_name = None
    element_name = None
    anchor_by = None
    anchor_el = None
    anchor_id = None

    _source_dict = None

    def __init__(self, element_dictionary: dict):
        """
        解析源字典 \n
        """
        self._source_dict = element_dictionary

        self.by = element_dictionary[Const.ELEMENT_BY]
        self.el = element_dictionary[Const.ELEMENT_EL]
        self.page_name = element_dictionary[Const.ELEMENT_PAGE_NAME]
        self.element_name = element_dictionary[Const.ELEMENT_ELEMENT_NAME]

        if Const.ELEMENT_ID in element_dictionary:
            self.id = element_dictionary[Const.ELEMENT_ID]

        if Const.ANCHOR_ELEMENT_BY in element_dictionary:
            self.anchor_by = element_dictionary[Const.ANCHOR_ELEMENT_BY]
            self.anchor_el = element_dictionary[Const.ANCHOR_ELEMENT_EL]
            self.anchor_id = element_dictionary[Const.ANCHOR_ELEMENT_ID]

    def get_source(self):
        """
        获取源字典 \n
        """
        return self._source_dict


if __name__ == '__main__':
    pass

