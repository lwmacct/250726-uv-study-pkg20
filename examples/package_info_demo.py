#!/usr/bin/env python3
"""
包信息自动获取演示
展示如何自动获取包名、版本号和作者信息
"""

import pkg20
import tomllib


def get_pyproject_info():
    """从 pyproject.toml 读取项目信息"""
    try:
        with open("pyproject.toml", "rb") as f:
            data = tomllib.load(f)

        project = data.get("project", {})
        return {
            "name": project.get("name", "unknown"),
            "version": project.get("version", "0.1.0"),
            "authors": project.get("authors", [])
        }
    except Exception:
        return {"name": "unknown", "version": "0.1.0", "authors": []}


def get_author_name(authors):
    """从作者列表中提取作者名称"""
    if not authors:
        return "Unknown"

    author = authors[0]
    if isinstance(author, dict):
        return author.get("name", "Unknown")
    elif isinstance(author, str):
        return author
    else:
        return "Unknown"


def main():
    """演示包信息自动获取"""
    print("=== 包信息自动获取演示 ===")

    # 显示包中的信息
    print(f"包名 (__package__): {pkg20.__package__}")
    print(f"模块名 (__name__): {pkg20.__name__}")
    print(f"包中的版本号: {pkg20.__version__}")
    print(f"包中的作者: {pkg20.__author__}")

    # 显示 pyproject.toml 中的信息
    pyproject_info = get_pyproject_info()
    print("\npyproject.toml 中的信息:")
    print(f"  项目名称: {pyproject_info['name']}")
    print(f"  项目版本: {pyproject_info['version']}")
    print(f"  项目作者: {get_author_name(pyproject_info['authors'])}")

    # 检查包名是否自动获取正确
    if pkg20.__package__ == pyproject_info['name']:
        print("✅ 包名自动获取正确！")
    else:
        print("❌ 包名获取不正确！")

    # 检查版本号是否同步
    if pkg20.__version__ == pyproject_info['version']:
        print("✅ 版本号已同步！")
    else:
        print("❌ 版本号不同步！")

    print("\n说明:")
    print("- 包名通过 __package__ 或 __name__ 自动获取")
    print("- 版本号通过 importlib.metadata 自动从 pyproject.toml 读取")
    print("- 作者信息也通过 importlib.metadata 自动获取")
    print("- 代码可以直接复制到其他项目使用，无需修改包名")


if __name__ == "__main__":
    main()
