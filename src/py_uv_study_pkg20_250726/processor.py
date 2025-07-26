"""
数据处理模块
提供DataProcessor类用于各种数据处理和转换功能
"""

from typing import List, Dict, Any
import json
from datetime import datetime


class DataProcessor:
    """数据处理类，提供各种数据处理和转换功能"""

    def __init__(self, name: str = "default"):
        """
        初始化数据处理器

        Args:
            name: 处理器名称
        """
        self.name = name
        self.processed_count = 0
        self.data_history: List[Dict[str, Any]] = []

    def process_numbers(self, numbers: List[int]) -> Dict[str, Any]:
        """
        处理数字列表，返回统计信息

        Args:
            numbers: 要处理的数字列表

        Returns:
            包含统计信息的字典
        """
        if not numbers:
            return {"error": "输入列表为空"}

        result = {
            "count": len(numbers),
            "sum": sum(numbers),
            "average": sum(numbers) / len(numbers),
            "min": min(numbers),
            "max": max(numbers),
            "sorted": sorted(numbers)
        }

        self._record_operation("process_numbers", numbers, result)
        return result

    def filter_data(self, data: List[Any], condition: callable) -> List[Any]:
        """
        根据条件过滤数据

        Args:
            data: 要过滤的数据列表
            condition: 过滤条件函数

        Returns:
            过滤后的数据列表
        """
        filtered = [item for item in data if condition(item)]

        self._record_operation("filter_data", data, filtered)
        return filtered

    def convert_to_json(self, data: Any) -> str:
        """
        将数据转换为JSON字符串

        Args:
            data: 要转换的数据

        Returns:
            JSON字符串
        """
        try:
            json_str = json.dumps(data, ensure_ascii=False, indent=2)
            self._record_operation("convert_to_json", data, json_str)
            return json_str
        except Exception as e:
            error_msg = f"转换失败: {str(e)}"
            self._record_operation("convert_to_json", data, error_msg)
            return error_msg

    def get_statistics(self) -> Dict[str, Any]:
        """
        获取处理统计信息

        Returns:
            统计信息字典
        """
        return {
            "processor_name": self.name,
            "total_processed": self.processed_count,
            "history_count": len(self.data_history),
            "created_at": datetime.now().isoformat()
        }

    def clear_history(self) -> None:
        """清空处理历史"""
        self.data_history.clear()
        self.processed_count = 0

    def get_history(self) -> List[Dict[str, Any]]:
        """
        获取处理历史

        Returns:
            历史记录列表的副本
        """
        return self.data_history.copy()

    def _record_operation(
        self, operation: str, input_data: Any, output_data: Any
    ) -> None:
        """
        记录操作历史（私有方法）

        Args:
            operation: 操作名称
            input_data: 输入数据
            output_data: 输出数据
        """
        self.processed_count += 1
        self.data_history.append({
            "timestamp": datetime.now().isoformat(),
            "operation": operation,
            "input": input_data,
            "output": output_data
        })
