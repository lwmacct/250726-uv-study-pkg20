"""
pkg20 - 简单计算机器工具包
"""

from .processor import Calculator
from .package_info import get_current_package_info

# 自动获取包信息
__version__, __author__ = get_current_package_info()

__all__ = ["Calculator"]
