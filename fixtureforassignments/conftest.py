#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:loyo
# datetime:2021/7/24 8:24 下午
# software: PyCharm
import pytest
import logging
from fixtureforassignments.calculator import Calculator


@pytest.fixture()
def calc_precedence():
    logging.info("开始计算")
    cal = Calculator()
    yield cal
    logging.info("结束运算")
    
# def pytest_collection_modifyitems(items):
#     """
#     测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
#     :return:
#     """
#     for item in items:
#         item.name = item.name.encode("utf-8").decode("unicode_escape")
#         item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")



