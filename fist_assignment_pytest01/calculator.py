#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:loyo
# datetime:2021/7/21 10:50 下午
# software: PyCharm
# 1、补全计算器（加法 除法）的测试用例
# 2、使用参数化完成测试用例的自动生成
# 3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
# 注意：
# 使用等价类，边界值，因果图等设计测试用例
# 测试用例中添加断言，验证结果
# 灵活使用 setup(), teardown() , setup_class(), teardown_class()
class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b