"""
{{PACKAGE_NAME}} - {{PACKAGE_DESCRIPTION}}

这是一个通用的 __init__.py 模板，可以直接复制到任何项目使用。
它会自动从 pyproject.toml 中读取包名、版本号和作者信息。
"""

# 导入你的主要模块
# from .your_module import YourClass
# from .another_module import AnotherClass


def _get_package_info():
    """
    自动获取包信息，支持复制到其他项目使用

    这个函数会自动：
    1. 获取当前包名（通过 __package__ 或 __name__）
    2. 从 pyproject.toml 读取版本号
    3. 获取作者信息
    4. 提供错误处理和兼容性支持

    Returns:
        tuple: (version, author)
    """
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

# 定义导出的类和函数
# 修改这个列表来包含你想要导出的类和函数
__all__ = [
    # "YourClass",
    # "your_function",
    # "AnotherClass",
]

# 使用示例：
# 1. 将整个 _get_package_info 函数复制到你的 __init__.py
# 2. 调用 __version__, __author__ = _get_package_info()
# 3. 确保 pyproject.toml 中有正确的项目信息
# 4. 修改 __all__ 列表来包含你的类和函数
