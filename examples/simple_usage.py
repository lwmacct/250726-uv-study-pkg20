#!/usr/bin/env python3
"""
简单使用示例
直接导入已安装的包
"""

from pkgs import Calculator


def main():
  """简单使用示例"""
  print("=== 简单使用示例 ===")

  # 创建计算器
  calc = Calculator("simple_calculator")

  # 基本运算
  print("\n基本运算:")
  print(f"5 + 3 = {calc.add(5, 3)}")
  print(f"10 - 4 = {calc.subtract(10, 4)}")
  print(f"6 * 7 = {calc.multiply(6, 7)}")
  print(f"15 / 3 = {calc.divide(15, 3)}")
  print(f"2 ^ 10 = {calc.power(2, 10)}")

  # 列表计算
  numbers = [1, 2, 3, 4, 5]
  print(f"\n列表计算: {numbers}")
  print(f"总和: {calc.calculate_sum(numbers)}")
  print(f"平均值: {calc.calculate_average(numbers)}")

  # 查看历史
  history = calc.get_history()
  print("\n操作历史:")
  for i, record in enumerate(history, 1):
    print(
        f"  {i}. {record['operation']}: "
        f"{record['inputs']} = {record['result']}"
    )


if __name__ == "__main__":
  main()
