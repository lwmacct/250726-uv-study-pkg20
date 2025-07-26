# 自动包信息获取功能使用指南

## 概述

这个功能允许你的 Python 包自动从 `pyproject.toml` 中读取包名、版本号和作者信息，无需手动维护多个地方的版本号。

## 功能特性

✅ **自动包名获取**：通过 `__package__` 或 `__name__` 自动获取当前包名  
✅ **版本号自动同步**：从 `pyproject.toml` 自动读取版本号  
✅ **作者信息自动获取**：从包元数据中自动获取作者信息  
✅ **代码可移植**：可以直接复制到其他项目使用  
✅ **向后兼容**：提供错误处理和兼容性支持  

## 使用方法

### 1. 基本使用

将以下代码复制到你的 `__init__.py` 文件中：

```python
def _get_package_info():
    """自动获取包信息，支持复制到其他项目使用"""
    # 默认值配置
    DEFAULT_VERSION = "0.1.0"
    DEFAULT_AUTHOR = "Unknown"
    
    try:
        from importlib.metadata import version, metadata
        # 获取当前包名（通过 __package__ 或 __name__）
        package_name = __package__ or __name__.split('.')[0]
        
        # 获取版本和作者信息
        __version__ = version(package_name)
        package_metadata = metadata(package_name)
        __author__ = package_metadata.get("Author", DEFAULT_AUTHOR)
        
        return __version__, __author__
    except ImportError:
        # 兼容性处理：如果 importlib.metadata 不可用，使用默认值
        return DEFAULT_VERSION, DEFAULT_AUTHOR
    except Exception:
        # 如果获取失败，使用默认值
        return DEFAULT_VERSION, DEFAULT_AUTHOR

# 自动获取包信息
__version__, __author__ = _get_package_info()
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
# 基本版本号测试
uv run python examples/version_demo.py

# 包信息获取测试
uv run python examples/package_info_demo.py

# 可移植性测试
uv run python examples/portability_test.py
```

## 模板文件

- `templates/universal_init_template.py`：通用模板，可直接复制使用
- `templates/__init__.py.template`：基础模板

## 优势

1. **单一数据源**：版本号只在 `pyproject.toml` 中维护
2. **自动同步**：更新 `pyproject.toml` 后，包中的版本号自动更新
3. **代码可移植**：可以直接复制到其他项目使用，无需修改包名
4. **向后兼容**：如果 `importlib.metadata` 不可用，会回退到硬编码值
5. **标准化**：符合现代 Python 包开发的最佳实践

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