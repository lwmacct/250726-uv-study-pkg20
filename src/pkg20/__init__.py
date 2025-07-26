"""
pkg20 - 简单计算机器工具包
"""

from .processor import Calculator

try:
    from importlib.metadata import version, metadata
    __version__ = version("pkg20")
    __author__ = metadata("pkg20")["Author"]
except ImportError:
    # 兼容性处理：如果 importlib.metadata 不可用，使用硬编码值
    __version__ = "0.1.1"
    __author__ = "lwmacct"

__all__ = ["Calculator"]
