"""
pkg20 - 简单计算机器工具包
"""

from .processor import Calculator

# 自动获取包信息
try:
    from importlib.metadata import version, metadata
    __version__ = version("pkg20")
    package_metadata = metadata("pkg20")
    __author__ = package_metadata.get("Author", "lwmacct")
except ImportError:
    __version__ = "0.1.1"
    __author__ = "lwmacct"
except Exception:
    __version__ = "0.1.1"
    __author__ = "lwmacct"

__all__ = ["Calculator"]
