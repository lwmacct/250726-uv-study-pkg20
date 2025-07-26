"""
包的主入口点
当使用 python -m py_uv_study_pkg20_250726 时执行
"""

from .processor import DataProcessor


def main() -> None:
    """主函数，演示DataProcessor类的使用"""
    print("=== DataProcessor 演示 ===")

    # 创建处理器实例
    processor = DataProcessor("demo_processor")

    # 演示数字处理
    numbers = [10, 25, 8, 42, 15, 30]
    print(f"\n1. 处理数字列表: {numbers}")
    result = processor.process_numbers(numbers)
    print(f"结果: {result}")

    # 演示数据过滤
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"\n2. 过滤偶数: {data}")
    even_numbers = processor.filter_data(data, lambda x: x % 2 == 0)
    print(f"偶数: {even_numbers}")

    # 演示JSON转换
    sample_data = {"name": "测试", "numbers": [1, 2, 3], "active": True}
    print(f"\n3. 转换为JSON: {sample_data}")
    json_result = processor.convert_to_json(sample_data)
    print(f"JSON: {json_result}")

    # 显示统计信息
    print("\n4. 统计信息:")
    stats = processor.get_statistics()
    print(f"处理器名称: {stats['processor_name']}")
    print(f"总处理次数: {stats['total_processed']}")
    print(f"历史记录数: {stats['history_count']}")

    print("\n=== 演示完成 ===")


if __name__ == "__main__":
    main()
