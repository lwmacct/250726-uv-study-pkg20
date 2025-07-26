#!/usr/bin/env python3
"""
版本号自动同步演示
展示如何从 pyproject.toml 自动读取版本号
"""

import pkg20
import subprocess


def get_pyproject_version():
    """从 pyproject.toml 读取版本号"""
    try:
        result = subprocess.run(
            ["uv", "run", "python", "-c",
                "import tomllib; print(tomllib.load(open('pyproject.toml', 'rb'))['project']['version'])"],
            capture_output=True,
            text=True,
            cwd="."
        )
        return result.stdout.strip()
    except Exception:
        return "无法读取"


def main():
    """演示版本号自动同步"""
    print("=== 版本号自动同步演示 ===")

    # 显示包中的版本号
    print(f"包中的版本号: {pkg20.__version__}")
    print(f"包中的作者: {pkg20.__author__}")

    # 显示 pyproject.toml 中的版本号
    pyproject_version = get_pyproject_version()
    print(f"pyproject.toml 中的版本号: {pyproject_version}")

    # 检查是否同步
    if pkg20.__version__ == pyproject_version:
        print("✅ 版本号已同步！")
    else:
        print("❌ 版本号不同步！")

    print("\n说明:")
    print("- 包中的版本号通过 importlib.metadata 自动从 pyproject.toml 读取")
    print("- 当更新 pyproject.toml 中的版本号时，包中的版本号会自动更新")
    print("- 这避免了手动维护两个地方的版本号")


if __name__ == "__main__":
    main()
