"""
包信息工具模块
提供自动获取包名、版本号和作者信息的功能
"""

from typing import Tuple, Optional


def get_package_info(
    package_name: Optional[str] = None,
    default_version: str = "0.1.0",
    default_author: str = "Unknown"
) -> Tuple[str, str]:
  """
  自动获取包信息，支持复制到其他项目使用

  Args:
      package_name: 包名，如果为 None 则自动获取
      default_version: 默认版本号
      default_author: 默认作者名

  Returns:
      tuple: (version, author)

  Examples:
      >>> version, author = get_package_info()
      >>> print(f"版本: {version}, 作者: {author}")

      >>> version, author = get_package_info("my_package", "1.0.0", "张三")
      >>> print(f"版本: {version}, 作者: {author}")
  """
  try:
    from importlib.metadata import version, metadata

    # 获取包名
    if package_name is None:
      # 通过调用栈获取包名
      import inspect
      frame = inspect.currentframe()
      try:
        # 查找调用者的包名
        while frame:
          if frame.f_globals.get('__package__'):
            package_name = frame.f_globals['__package__']
            break
          frame = frame.f_back

        # 如果还是没找到，尝试从 __name__ 获取
        if not package_name:
          frame = inspect.currentframe()
          while frame:
            if frame.f_globals.get('__name__'):
              package_name = frame.f_globals['__name__'].split('.')[
                  0]
              break
            frame = frame.f_back
      finally:
        # 清理 frame 引用
        del frame

    # 如果还是没找到包名，使用默认值
    if not package_name:
      return default_version, default_author

    # 获取版本和作者信息
    __version__ = version(package_name)
    package_metadata = metadata(package_name)
    __author__ = package_metadata.get("Author", default_author)

    return __version__, __author__

  except ImportError:
    # 兼容性处理：如果 importlib.metadata 不可用，使用默认值
    return default_version, default_author
  except Exception:
    # 如果获取失败，使用默认值
    return default_version, default_author


def get_package_name() -> Optional[str]:
  """
  自动获取当前包名

  Returns:
      包名，如果无法获取则返回 None
  """
  try:
    import inspect
    frame = inspect.currentframe()
    try:
      while frame:
        if frame.f_globals.get('__package__'):
          return frame.f_globals['__package__']
        frame = frame.f_back
      return None
    finally:
      del frame
  except Exception:
    return None


def get_version(package_name: Optional[str] = None, default: str = "0.1.0") -> str:
  """
  获取包版本号

  Args:
      package_name: 包名，如果为 None 则自动获取
      default: 默认版本号

  Returns:
      版本号字符串
  """
  version, _ = get_package_info(package_name, default, "Unknown")
  return version


def get_author(package_name: Optional[str] = None, default: str = "Unknown") -> str:
  """
  获取包作者信息

  Args:
      package_name: 包名，如果为 None 则自动获取
      default: 默认作者名

  Returns:
      作者名字符串
  """
  _, author = get_package_info(package_name, "0.1.0", default)
  return author


# 便捷函数，用于直接获取当前包的信息
def get_current_package_info() -> Tuple[str, str]:
  """
  获取当前包的信息（版本和作者）

  Returns:
      tuple: (version, author)
  """
  # 直接使用 __package__ 或 __name__ 获取包名
  package_name = None

  # 从当前模块获取包名
  if '__package__' in globals():
    package_name = globals()['__package__']
  elif '__name__' in globals():
    package_name = globals()['__name__'].split('.')[0]

  return get_package_info(package_name)


def get_current_version() -> str:
  """
  获取当前包的版本号

  Returns:
      版本号字符串
  """
  return get_version()


def get_current_author() -> str:
  """
  获取当前包的作者信息

  Returns:
      作者名字符串
  """
  return get_author()
