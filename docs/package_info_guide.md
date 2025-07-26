# 自动包信息获取功能使用指南

## 概述

这个功能允许你的 Python 包自动从 `pyproject.toml` 中读取包名、版本号和作者信息，无需手动维护多个地方的版本号。

**推荐方案：使用 importlib.metadata（Python 3.8+ 标准库）**

## 功能特性

✅ **自动包名获取**：通过 `__package__` 或 `__name__` 自动获取当前包名  
✅ **版本号自动同步**：从 `pyproject.toml` 自动读取版本号  
✅ **作者信息自动获取**：从包元数据中自动获取作者信息  
✅ **代码可移植**：可以直接复制到其他项目使用  
✅ **向后兼容**：提供错误处理和兼容性支持  

## 使用方法

### 1. 基本使用

**方案一：直接使用 importlib.metadata（推荐）**

```python
# __init__.py
try:
    from importlib.metadata import version, metadata
    __version__ = version("your_package_name")
    package_metadata = metadata("your_package_name")
    __author__ = package_metadata.get("Author", "Unknown")
except ImportError:
    __version__ = "0.1.0"
    __author__ = "Unknown"
```

**方案二：使用工具模块**

```python
# __init__.py
from .package_info import get_current_package_info

# 自动获取包信息
__version__, __author__ = get_current_package_info()
```

### 2. 确保 pyproject.toml 配置正确

```toml
[project]
name = "your-package-name"
version = "1.0.0"
description = "Your package description"
authors = [
    { name = "Your Name", email = "your.email@example.com" }
]
```

### 3. 使用包信息

```python
import your_package

print(f"版本: {your_package.__version__}")
print(f"作者: {your_package.__author__}")
```

## 测试功能

运行以下命令来测试功能是否正常工作：

```bash
# 基本使用示例
uv run python examples/simple_usage.py

# 基础使用示例
uv run python examples/basic_usage.py

# 直接测试包信息
uv run python -c "import pkg20; print(f'版本: {pkg20.__version__}'); print(f'作者: {pkg20.__author__}')"
```

## 模板文件

- `templates/universal_init_template.py`：通用模板，可直接复制使用

## 优势

1. **零依赖**：只使用 Python 标准库
2. **简单可靠**：代码简洁，易于维护
3. **性能优秀**：直接读取包元数据
4. **广泛支持**：Python 3.8+ 原生支持
5. **向后兼容**：提供完整的错误处理
6. **标准化**：符合现代 Python 包开发的最佳实践

## 注意事项

1. 确保你的项目使用 `pyproject.toml` 进行配置
2. 确保包已经正确安装（使用 `uv pip install -e .` 或类似命令）
3. 如果遇到问题，检查 `pyproject.toml` 中的项目名称是否正确

## 示例输出

```
=== 包信息自动获取演示 ===
包名 (__package__): my_package
模块名 (__name__): my_package
包中的版本号: 1.0.0
包中的作者: Your Name

pyproject.toml 中的信息:
  项目名称: my_package
  项目版本: 1.0.0
  项目作者: Your Name
✅ 包名自动获取正确！
✅ 版本号已同步！
``` 