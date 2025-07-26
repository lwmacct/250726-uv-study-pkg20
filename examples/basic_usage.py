#!/usr/bin/env python3
"""
基本使用示例
展示如何导入和使用DataProcessor类
"""

from pkg20 import DataProcessor
import sys
import os

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


def main():
    """基本使用示例"""
    print("=== 基本使用示例 ===")

    # 创建处理器
    processor = DataProcessor("example_processor")

    # 示例1: 处理数字
    numbers = [1, 5, 3, 8, 2, 9, 4]
    print(f"\n处理数字: {numbers}")
    stats = processor.process_numbers(numbers)
    print(f"统计结果: {stats}")

    # 示例2: 过滤字符串
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    print(f"\n过滤单词: {words}")
    long_words = processor.filter_data(words, lambda x: len(x) > 5)
    print(f"长单词: {long_words}")

    # 示例3: JSON转换
    user_data = {
        "name": "张三",
        "age": 25,
        "hobbies": ["编程", "阅读", "运动"],
        "active": True
    }
    print(f"\n用户数据: {user_data}")
    json_str = processor.convert_to_json(user_data)
    print(f"JSON格式:\n{json_str}")

    # 显示统计
    print(f"\n处理统计: {processor.get_statistics()}")


if __name__ == "__main__":
    main()
