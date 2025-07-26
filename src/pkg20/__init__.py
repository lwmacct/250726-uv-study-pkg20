"""
pkg20 - 简单计算机器工具包
"""

from .processor import Calculator


def _get_package_info():
    """自动获取包信息，支持复制到其他项目使用"""
    try:
        from importlib.metadata import version, metadata
        # 获取当前包名（通过 __package__ 或 __name__）
        package_name = __package__ or __name__.split('.')[0]

        # 获取版本和作者信息
        __version__ = version(package_name)
        package_metadata = metadata(package_name)
        __author__ = package_metadata.get("Author", "Unknown")

        return __version__, __author__
    except ImportError:
        # 兼容性处理：如果 importlib.metadata 不可用，使用硬编码值
        return "0.1.1", "lwmacct"
    except Exception:
        # 如果获取失败，使用默认值
        return "0.1.1", "lwmacct"


__version__, __author__ = _get_package_info()

__all__ = ["Calculator"]
