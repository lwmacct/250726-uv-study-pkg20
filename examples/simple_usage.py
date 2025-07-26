#!/usr/bin/env python3
"""
简单使用示例
直接导入已安装的包
"""

from py_uv_study_pkg20_250726 import DataProcessor


def main():
    """简单使用示例"""
    print("=== 简单使用示例 ===")

    # 创建处理器
    processor = DataProcessor("simple_processor")

    # 处理一些数据
    numbers = [100, 200, 300, 400, 500]
    result = processor.process_numbers(numbers)

    print(f"数字: {numbers}")
    print(f"总和: {result['sum']}")
    print(f"平均值: {result['average']:.2f}")
    print(f"最大值: {result['max']}")
    print(f"最小值: {result['min']}")

    # 过滤数据
    mixed_data = [1, "hello", 3.14, True, "world", 42]
    strings = processor.filter_data(mixed_data, lambda x: isinstance(x, str))
    print(f"\n混合数据: {mixed_data}")
    print(f"字符串: {strings}")

    # 查看历史
    history = processor.get_history()
    print("\n操作历史:")
    for i, record in enumerate(history, 1):
        print(f"  {i}. {record['operation']} - {record['timestamp']}")


if __name__ == "__main__":
    main()
