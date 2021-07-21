#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:loyo
# datetime:2021/7/22 12:01 上午

def pytest_collection_modifyitems(items):
    """
        解决参数化 ids 用例描述为中文时控制台输出Unicode编码问题
    :param items:
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")