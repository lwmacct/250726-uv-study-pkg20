#!/usr/bin/env python3
"""
Calculator类的测试
"""

# import pytest  # 如果需要运行pytest测试，取消注释
from pkg20 import Calculator


class TestCalculator:
    """Calculator类的测试用例"""

    def setup_method(self):
        """每个测试方法前的设置"""
        self.calc = Calculator("test_calculator")

    def test_add(self):
        """测试加法功能"""
        result = self.calc.add(5, 3)
        assert result == 8

    def test_subtract(self):
        """测试减法功能"""
        result = self.calc.subtract(10, 4)
        assert result == 6

    def test_multiply(self):
        """测试乘法功能"""
        result = self.calc.multiply(6, 7)
        assert result == 42

    def test_divide(self):
        """测试除法功能"""
        result = self.calc.divide(15, 3)
        assert result == 5.0

    def test_divide_by_zero(self):
        """测试除零错误"""
        try:
            self.calc.divide(10, 0)
            assert False, "应该抛出ZeroDivisionError"
        except ZeroDivisionError:
            pass

    def test_power(self):
        """测试幂运算功能"""
        result = self.calc.power(2, 8)
        assert result == 256

    def test_calculate_sum(self):
        """测试列表求和功能"""
        numbers = [1, 2, 3, 4, 5]
        result = self.calc.calculate_sum(numbers)
        assert result == 15

    def test_calculate_average(self):
        """测试列表平均值功能"""
        numbers = [1, 2, 3, 4, 5]
        result = self.calc.calculate_average(numbers)
        assert result == 3.0

    def test_empty_list_sum(self):
        """测试空列表求和"""
        result = self.calc.calculate_sum([])
        assert result == 0

    def test_empty_list_average(self):
        """测试空列表平均值"""
        result = self.calc.calculate_average([])
        assert result == 0.0

    def test_get_statistics(self):
        """测试统计信息功能"""
        # 先执行一些操作
        self.calc.add(1, 2)
        self.calc.multiply(3, 4)

        stats = self.calc.get_statistics()
        assert stats["calculator_name"] == "test_calculator"
        assert stats["total_operations"] == 2
        assert stats["history_count"] == 2

    def test_clear_history(self):
        """测试清空历史功能"""
        self.calc.add(1, 2)
        assert self.calc.operation_count == 1

        self.calc.clear_history()
        assert self.calc.operation_count == 0
        assert len(self.calc.history) == 0


if __name__ == "__main__":
    # 简单运行测试
    calc = Calculator("test")

    # 测试基本运算
    print("测试基本运算:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")

    # 测试列表计算
    numbers = [1, 2, 3, 4, 5]
    print(f"\n测试列表计算: {numbers}")
    print(f"总和: {calc.calculate_sum(numbers)}")
    print(f"平均值: {calc.calculate_average(numbers)}")

    # 测试错误处理
    print("\n测试错误处理:")
    try:
        calc.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"除零错误: {e}")

    print("\n所有测试通过！")
