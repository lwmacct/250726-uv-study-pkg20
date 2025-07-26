"""
简单计算机器模块
提供基本的数学运算功能，主要用于测试包
"""

from typing import List, Union, Dict, Any


class Calculator:
    """简单计算机器类，提供基本的数学运算功能"""

    def __init__(self, name: str = "default"):
        """
        初始化计算机器

        Args:
            name: 计算器名称
        """
        self.name = name
        self.operation_count = 0
        self.history: List[Dict[str, Any]] = []

    def add(
        self, a: Union[int, float], b: Union[int, float]
    ) -> Union[int, float]:
        """
        加法运算

        Args:
            a: 第一个数
            b: 第二个数

        Returns:
            两数之和
        """
        result = a + b
        self._record_operation("add", [a, b], result)
        return result

    def subtract(
        self, a: Union[int, float], b: Union[int, float]
    ) -> Union[int, float]:
        """
        减法运算

        Args:
            a: 被减数
            b: 减数

        Returns:
            两数之差
        """
        result = a - b
        self._record_operation("subtract", [a, b], result)
        return result

    def multiply(
        self, a: Union[int, float], b: Union[int, float]
    ) -> Union[int, float]:
        """
        乘法运算

        Args:
            a: 第一个数
            b: 第二个数

        Returns:
            两数之积
        """
        result = a * b
        self._record_operation("multiply", [a, b], result)
        return result

    def divide(
        self, a: Union[int, float], b: Union[int, float]
    ) -> Union[int, float]:
        """
        除法运算

        Args:
            a: 被除数
            b: 除数

        Returns:
            两数之商

        Raises:
            ZeroDivisionError: 当除数为0时
        """
        if b == 0:
            raise ZeroDivisionError("除数不能为0")

        result = a / b
        self._record_operation("divide", [a, b], result)
        return result

    def power(
        self, base: Union[int, float], exponent: Union[int, float]
    ) -> Union[int, float]:
        """
        幂运算

        Args:
            base: 底数
            exponent: 指数

        Returns:
            base的exponent次方
        """
        result = base ** exponent
        self._record_operation("power", [base, exponent], result)
        return result

    def calculate_sum(
        self, numbers: List[Union[int, float]]
    ) -> Union[int, float]:
        """
        计算列表中所有数字的和

        Args:
            numbers: 数字列表

        Returns:
            所有数字的和
        """
        if not numbers:
            return 0

        result = sum(numbers)
        self._record_operation("calculate_sum", numbers, result)
        return result

    def calculate_average(
        self, numbers: List[Union[int, float]]
    ) -> float:
        """
        计算列表中所有数字的平均值

        Args:
            numbers: 数字列表

        Returns:
            所有数字的平均值
        """
        if not numbers:
            return 0.0

        result = sum(numbers) / len(numbers)
        self._record_operation("calculate_average", numbers, result)
        return result

    def get_statistics(self) -> Dict[str, Any]:
        """
        获取计算器统计信息

        Returns:
            统计信息字典
        """
        return {
            "calculator_name": self.name,
            "total_operations": self.operation_count,
            "history_count": len(self.history)
        }

    def get_history(self) -> List[Dict[str, Any]]:
        """
        获取计算历史

        Returns:
            历史记录列表的副本
        """
        return self.history.copy()

    def clear_history(self) -> None:
        """清空计算历史"""
        self.history.clear()
        self.operation_count = 0

    def _record_operation(
        self, operation: str, inputs: List[Any], result: Any
    ) -> None:
        """
        记录操作历史（私有方法）

        Args:
            operation: 操作名称
            inputs: 输入参数
            result: 计算结果
        """
        self.operation_count += 1
        self.history.append({
            "operation": operation,
            "inputs": inputs,
            "result": result,
            "operation_number": self.operation_count
        })
