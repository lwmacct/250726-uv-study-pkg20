from typing import List, Dict, Any
import json
from datetime import datetime


class DataProcessor:
    """数据处理类，提供各种数据处理和转换功能"""

    def __init__(self, name: str = "default"):
        self.name = name
        self.processed_count = 0
        self.data_history: List[Dict[str, Any]] = []

    def process_numbers(self, numbers: List[int]) -> Dict[str, Any]:
        """处理数字列表，返回统计信息"""
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

        self.processed_count += 1
        self.data_history.append({
            "timestamp": datetime.now().isoformat(),
            "operation": "process_numbers",
            "input": numbers,
            "output": result
        })

        return result

    def filter_data(self, data: List[Any], condition: callable) -> List[Any]:
        """根据条件过滤数据"""
        filtered = [item for item in data if condition(item)]

        self.processed_count += 1
        self.data_history.append({
            "timestamp": datetime.now().isoformat(),
            "operation": "filter_data",
            "input": data,
            "output": filtered
        })

        return filtered

    def convert_to_json(self, data: Any) -> str:
        """将数据转换为JSON字符串"""
        try:
            json_str = json.dumps(data, ensure_ascii=False, indent=2)

            self.processed_count += 1
            self.data_history.append({
                "timestamp": datetime.now().isoformat(),
                "operation": "convert_to_json",
                "input": data,
                "output": json_str
            })

            return json_str
        except Exception as e:
            return f"转换失败: {str(e)}"

    def get_statistics(self) -> Dict[str, Any]:
        """获取处理统计信息"""
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
        """获取处理历史"""
        return self.data_history.copy()


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
