"""
包的主入口点
当使用 python -m pkg20 时执行
"""

from .processor import Calculator


def main() -> None:
    """主函数，演示Calculator类的使用"""
    print("=== Calculator 演示 ===")

    # 创建计算器实例
    calc = Calculator("demo_calculator")

    # 演示基本运算
    print("\n1. 基本运算:")
    print(f"   10 + 5 = {calc.add(10, 5)}")
    print(f"   10 - 5 = {calc.subtract(10, 5)}")
    print(f"   10 * 5 = {calc.multiply(10, 5)}")
    print(f"   10 / 5 = {calc.divide(10, 5)}")
    print(f"   2 ^ 8 = {calc.power(2, 8)}")

    # 演示列表计算
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("\n2. 列表计算:")
    print(f"   数字列表: {numbers}")
    print(f"   总和: {calc.calculate_sum(numbers)}")
    print(f"   平均值: {calc.calculate_average(numbers):.2f}")

    # 演示错误处理
    print("\n3. 错误处理:")
    try:
        calc.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"   10 / 0 错误: {e}")

    # 显示统计信息
    print("\n4. 统计信息:")
    stats = calc.get_statistics()
    print(f"   计算器名称: {stats['calculator_name']}")
    print(f"   总操作次数: {stats['total_operations']}")
    print(f"   历史记录数: {stats['history_count']}")

    # 显示历史记录
    print("\n5. 操作历史:")
    history = calc.get_history()
    for i, record in enumerate(history, 1):
        print(
            f"   {i}. {record['operation']}: "
            f"{record['inputs']} = {record['result']}"
        )

    print("\n=== 演示完成 ===")


if __name__ == "__main__":
    main()
