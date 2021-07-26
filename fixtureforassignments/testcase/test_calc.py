#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:loyo
# datetime:2021/7/25 5:43 下午
# software: PyCharm
import yaml
import logging
import allure
from decimal import Decimal
import pytest

def get_calc_data(name):
    with open('/Users/loyo/Desktop/Python/myassignment/fixtureforassignments/data/data_calc.yml',encoding='utf-8') as f:
        return yaml.safe_load(f)[name]
    
# 测试获取数据方法
def test_getdatas():
    print({**get_calc_data('add')['success'],**{'indirect':True}})
    print(get_calc_data('add')['fail'])

@allure.feature("计算器")
class TestCalcuLator():
    
    @allure.story('相加功能')
    @allure.title('成功用例 {a}+{b}={expect_result}')
    @pytest.mark.parametrize(**get_calc_data('add')['success'])
    def test_add_success(self,a,b,expect_result,calc_precedence):
        with allure.step(f'计算{a}+{b}'):
            if not float('inf') in [eval(str(a)),eval(str(b))]:
                a = Decimal(str(a))
                b = Decimal(str(b))
                expect_result = Decimal(str(expect_result))
            else:
                a = eval(str(a))
                b = eval(str(b))
                expect_result = eval(str(expect_result))
            logging.info(f"计算{a}+{b},预期结果为{expect_result}")
            assert  expect_result == calc_precedence.add(a,b)


    @allure.story('相加功能')
    @allure.title('失败用例 {a} + {b} 会触发{errorType}')
    @pytest.mark.parametrize(**get_calc_data('add')['fail'])
    def test_add_fail(self,a,b,errorType,calc_precedence):
        with allure.step(f'计算{a}+{b}'):
            logging.info(f"计算{a}+{b},预期结果为{errorType}异常")
        
        with pytest.raises(ValueError) as e:    
            assert  errorType == calc_precedence.add(a,b)

    @allure.story('相减功能')
    @allure.title('成功用例 {a} - {b}  = {expect_result}')
    @pytest.mark.parametrize(**get_calc_data('sub')['success'])
    def test_sub_success(self, a, b, expect_result, calc_precedence):
        with allure.step(f'计算{a}-{b}'):
            a = Decimal(str(a))
            b = Decimal(str(b))
            expect_result = Decimal(str(expect_result))
            logging.info(f"计算{a}-{b},预期结果为{expect_result}")
            assert expect_result == calc_precedence.sub(a, b)

    @allure.story('相减功能')
    @allure.title('失败用例 {a} - {b} 会触发{errorType}')
    @pytest.mark.parametrize(**get_calc_data('sub')['fail'])
    def test_sub_fail(self, a, b, errorType, calc_precedence):
        with allure.step(f'计算{a}-{b}'):
            logging.info(f"计算{a}-{b},预期结果为{errorType}异常")

        with pytest.raises(ValueError) as e:
            assert errorType == calc_precedence.sub(a, b)

    @allure.story('除法功能')
    @allure.title('成功用例{a}/{b} = {expect_result}')
    @pytest.mark.parametrize(**get_calc_data('div')['success'])
    def test_div_success(self,a,b,expect_result,calc_precedence):
        with allure.step(f'计算{a}与{b}相除'):
            a = Decimal(str(a))
            b = Decimal(str(b))
            expect_result = Decimal(str(expect_result))
            logging.info(f'计算{a}/{b},预期结果为{expect_result}')
        assert expect_result == calc_precedence.div(a,b)
        
    @allure.story('除法功能')
    @allure.title('失败用例{a}/{b} 会触发{errorType}')
    @pytest.mark.parametrize(**get_calc_data('div')['fail'])
    def test_div_fail(self,a,b,errorType,calc_precedence):
        with allure.step(f'计算{a}/{b}相除'):
            logging.info(f'计算{a}/{b},预期结果为{errorType}异常')
        with pytest.raises(ZeroDivisionError,ValueError) as e:
            assert errorType == calc_precedence.div(a,b)

    @allure.story('乘法功能')
    @allure.title('成功用例{a}*{b} = {expect_result}')
    @pytest.mark.parametrize(**get_calc_data('mul')['success'])
    def test_mul_success(self, a, b, expect_result, calc_precedence):
        with allure.step(f'计算{a}与{b}相乘'):
            a = Decimal(str(a))
            b = Decimal(str(b))
            expect_result = Decimal(str(expect_result))
            logging.info(f'计算{a}*{b},预期结果为{expect_result}')
        assert expect_result == calc_precedence.mul(a,b)

    @allure.story('乘法功能')
    @allure.title('失败用例{a}*{b} 会触发{errorType}')
    @pytest.mark.parametrize(**get_calc_data('mul')['fail'])
    def test_mul_fail(self, a, b, errorType, calc_precedence):
        with allure.step(f'计算{a}*{b}相乘'):
            logging.info(f'计算{a}*{b},预期结果为{errorType}异常')
        with pytest.raises(TypeError) as e:
            assert errorType == calc_precedence.mul(a,b)
    

