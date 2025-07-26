#!/usr/bin/env python3
"""
DataProcessor类的测试
"""

# import pytest  # 如果需要运行pytest测试，取消注释
from py_uv_study_pkg20_250726 import DataProcessor


class TestDataProcessor:
    """DataProcessor类的测试用例"""

    def setup_method(self):
        """每个测试方法前的设置"""
        self.processor = DataProcessor("test_processor")

    def test_process_numbers(self):
        """测试数字处理功能"""
        numbers = [1, 2, 3, 4, 5]
        result = self.processor.process_numbers(numbers)

        assert result["count"] == 5
        assert result["sum"] == 15
        assert result["average"] == 3.0
        assert result["min"] == 1
        assert result["max"] == 5
        assert result["sorted"] == [1, 2, 3, 4, 5]

    def test_process_empty_numbers(self):
        """测试空数字列表"""
        result = self.processor.process_numbers([])
        assert result["error"] == "输入列表为空"

    def test_filter_data(self):
        """测试数据过滤功能"""
        data = [1, 2, 3, 4, 5, 6]
        even_numbers = self.processor.filter_data(data, lambda x: x % 2 == 0)
        assert even_numbers == [2, 4, 6]

    def test_convert_to_json(self):
        """测试JSON转换功能"""
        data = {"name": "测试", "value": 123}
        json_str = self.processor.convert_to_json(data)
        assert '"name": "测试"' in json_str
        assert '"value": 123' in json_str

    def test_get_statistics(self):
        """测试统计信息功能"""
        # 先执行一些操作
        self.processor.process_numbers([1, 2, 3])
        self.processor.filter_data([1, 2, 3], lambda x: x > 1)

        stats = self.processor.get_statistics()
        assert stats["processor_name"] == "test_processor"
        assert stats["total_processed"] == 2
        assert stats["history_count"] == 2

    def test_clear_history(self):
        """测试清空历史功能"""
        self.processor.process_numbers([1, 2, 3])
        assert self.processor.processed_count == 1

        self.processor.clear_history()
        assert self.processor.processed_count == 0
        assert len(self.processor.data_history) == 0


if __name__ == "__main__":
    # 简单运行测试
    processor = DataProcessor("test")

    # 测试数字处理
    result = processor.process_numbers([1, 2, 3, 4, 5])
    print(f"数字处理测试: {result}")

    # 测试过滤
    filtered = processor.filter_data([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
    print(f"过滤测试: {filtered}")

    # 测试JSON转换
    json_str = processor.convert_to_json({"test": "数据"})
    print(f"JSON转换测试: {json_str}")

    print("所有测试通过！")
