#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:loyo
# datetime:2021/7/21 11:13 下午
# software: PyCharm
# 作业没啥思路看着花小田的一步步走下去的，编程思维很重要
# 此为测试计算器函数的代码

import yaml
import pytest
from decimal import Decimal
from calculator import Calculator

def get_calc_date(name):
    """
    打开data并将数据格式化为Python可识别
    :param name:
    :return:
    """
    with open('./calc_data.yml',encoding='utf-8') as f:
        return yaml.safe_load(f)[name]

# (验证是否正确获取到数据)
def test_getdatas():
    print(get_calc_date('add')['fail'])

class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    @pytest.mark.parametrize(**get_calc_date('add')['success'])
    def test_add_success(self,a,b,expect_result):
        if not float('inf') in [eval(str(a)),eval(str(b))]:
            # 非无穷数在字符串a,b中循环后取值
            a = Decimal(str(a))
            # 转化为10进制
            b = Decimal(str(b))
            expect_result = Decimal(str(expect_result))
        else:
            a = eval(str(a))
            b = eval(str(b))
            expect_result = eval(str(expect_result))
        assert expect_result == self.calc.add(a,b)
        
    @pytest.mark.parametrize(**get_calc_date('add')['fail'])
    def test_add_fail(self,a,b,errorType):
        try:
            self.calc.add(a,b)
        except Exception as e:
            assert errorType == type(e).__name__
            raise AttributeError(f"预期发生{errorType}错误")
        
    @pytest.mark.parametrize(**get_calc_date('div')['success'])
    def test_div_success(self,a,b,expect_result):
        a = Decimal(str(a))
        b = Decimal(str(b))
        expect_result = Decimal(str(expect_result))
        assert expect_result == self.calc.div(a,b)
    
    @pytest.mark.parametrize(**get_calc_date('div')['fail'])
    def test_div_fail(self,a,b,errorType):
        try:
            self.calc.div(a,b)
        except Exception as e:
            assert errorType == type(e).__name__
            raise AssertionError(f"预期发生{errorType}错误")
        