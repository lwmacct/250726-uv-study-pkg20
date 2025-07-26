# pkg20

一个使用 `uv` 构建的Python数据处理工具包。

## 功能特性

- 📊 **数字处理**: 计算统计信息（总和、平均值、最大值、最小值等）
- 🔍 **数据过滤**: 支持自定义条件的数据过滤
- 🔄 **JSON转换**: 将Python对象转换为JSON格式
- 📈 **操作历史**: 记录所有处理操作的历史
- 📋 **统计信息**: 提供处理统计和历史记录

## 安装

### 使用 uv（推荐）

```bash
# 克隆仓库
git clone <repository-url>
cd py_uv_study-pkg20-250726

# 使用uv安装
uv sync
uv pip install -e .
```

### 传统方式

```bash
pip install -e .
```

## 快速开始

### 基本使用

```python
from pkg20 import DataProcessor

# 创建处理器
processor = DataProcessor("my_processor")

# 处理数字
numbers = [1, 2, 3, 4, 5]
result = processor.process_numbers(numbers)
print(f"总和: {result['sum']}")
print(f"平均值: {result['average']}")

# 过滤数据
data = [1, 2, 3, 4, 5, 6]
even_numbers = processor.filter_data(data, lambda x: x % 2 == 0)
print(f"偶数: {even_numbers}")

# 转换为JSON
user_data = {"name": "张三", "age": 25}
json_str = processor.convert_to_json(user_data)
print(json_str)
```

### 运行演示

```bash
# 使用uv运行包演示
uv run python -m pkg20

# 运行示例
uv run python examples/simple_usage.py
uv run python examples/basic_usage.py
```

## API 文档

### DataProcessor 类

#### 构造函数

```python
DataProcessor(name: str = "default")
```

- `name`: 处理器名称

#### 方法

##### process_numbers(numbers: List[int]) -> Dict[str, Any]

处理数字列表，返回统计信息。

```python
result = processor.process_numbers([1, 2, 3, 4, 5])
# 返回: {
#   "count": 5,
#   "sum": 15,
#   "average": 3.0,
#   "min": 1,
#   "max": 5,
#   "sorted": [1, 2, 3, 4, 5]
# }
```

##### filter_data(data: List[Any], condition: callable) -> List[Any]

根据条件过滤数据。

```python
even_numbers = processor.filter_data([1, 2, 3, 4], lambda x: x % 2 == 0)
# 返回: [2, 4]
```

##### convert_to_json(data: Any) -> str

将数据转换为JSON字符串。

```python
json_str = processor.convert_to_json({"name": "测试", "value": 123})
```

##### get_statistics() -> Dict[str, Any]

获取处理统计信息。

```python
stats = processor.get_statistics()
# 返回: {
#   "processor_name": "my_processor",
#   "total_processed": 3,
#   "history_count": 3,
#   "created_at": "2025-07-26T23:44:13.504780"
# }
```

##### get_history() -> List[Dict[str, Any]]

获取处理历史记录。

##### clear_history() -> None

清空处理历史。

## 开发

### 使用 uv 进行开发

```bash
# 同步依赖
uv sync

# 安装开发版本
uv pip install -e .

# 运行测试
uv run python tests/test_processor.py

# 构建包
uv build

# 运行示例
uv run python examples/simple_usage.py
```

### 项目结构

```
pkg20/
├── src/
│   └── pkg20/
│       ├── __init__.py          # 包入口
│       ├── processor.py         # 核心功能模块
│       └── __main__.py          # 命令行入口
├── examples/
│   ├── basic_usage.py          # 基本使用示例
│   └── simple_usage.py         # 简单使用示例
├── tests/
│   └── test_processor.py       # 测试文件
├── pyproject.toml              # 项目配置
└── README.md                   # 说明文档
```

## 测试

```bash
# 运行简单测试
uv run python tests/test_processor.py

# 使用pytest（需要安装）
uv add pytest
uv run pytest tests/
```

## 构建和发布

```bash
# 构建包
uv build

# 检查构建结果
ls dist/
```

## 许可证

MIT License

## 作者

lwmacct (lwmacct@icloud.com)
