#!/usr/bin/env python3
"""
包信息获取解决方案演示
展示不同的方法来获取包信息
"""

import pkg20
from pkg20.utils.package_info import (
    get_package_info,
    get_version,
    get_author,
    get_current_package_info
)


def demo_solution_1_importlib_metadata():
    """方案一：直接使用 importlib.metadata"""
    print("=== 方案一：直接使用 importlib.metadata ===")

    try:
        from importlib.metadata import version, metadata
        package_name = "pkg20"

        version_str = version(package_name)
        package_metadata = metadata(package_name)
        author = package_metadata.get("Author", "Unknown")

        print(f"包名: {package_name}")
        print(f"版本: {version_str}")
        print(f"作者: {author}")
        print("✅ 成功")
    except Exception as e:
        print(f"❌ 失败: {e}")


def demo_solution_2_our_utils():
    """方案二：使用我们的工具模块"""
    print("\n=== 方案二：使用我们的工具模块 ===")

    # 方法1：获取当前包信息
    version, author = get_current_package_info()
    print(f"当前包版本: {version}")
    print(f"当前包作者: {author}")

    # 方法2：指定包名
    version = get_version("pkg20")
    author = get_author("pkg20")
    print(f"指定包名版本: {version}")
    print(f"指定包名作者: {author}")

    # 方法3：自定义默认值
    version, author = get_package_info(
        package_name="pkg20",
        default_version="0.0.0",
        default_author="自定义作者"
    )
    print(f"自定义默认值版本: {version}")
    print(f"自定义默认值作者: {author}")

    print("✅ 成功")


def demo_solution_3_setuptools_scm():
    """方案三：使用 setuptools-scm（需要配置）"""
    print("\n=== 方案三：使用 setuptools-scm ===")

    try:
        # 这个需要在 pyproject.toml 中配置
        # [tool.setuptools_scm]
        # version_scheme = "python-simplified-semver"
        # local_scheme = "node-and-timestamp"

        print("需要配置 pyproject.toml:")
        print("[tool.setuptools_scm]")
        print("version_scheme = \"python-simplified-semver\"")
        print("local_scheme = \"node-and-timestamp\"")
        print("⚠️  需要额外配置")
    except Exception as e:
        print(f"❌ 失败: {e}")


def demo_solution_4_pkg_resources():
    """方案四：使用 pkg_resources（已弃用）"""
    print("\n=== 方案四：使用 pkg_resources（已弃用） ===")

    try:
        import pkg_resources
        version = pkg_resources.get_distribution("pkg20").version
        print(f"版本: {version}")
        print("⚠️  pkg_resources 已弃用，建议使用 importlib.metadata")
    except Exception as e:
        print(f"❌ 失败: {e}")


def demo_solution_5_third_party_packages():
    """方案五：第三方包解决方案"""
    print("\n=== 方案五：第三方包解决方案 ===")

    # 1. versioneer
    print("1. versioneer:")
    print("   - 从 git 标签自动生成版本号")
    print("   - 适合使用 git 标签管理版本的项目")

    # 2. dunamai
    print("2. dunamai:")
    print("   - 动态版本管理")
    print("   - 支持多种版本控制工具")

    # 3. hatch-vcs
    print("3. hatch-vcs:")
    print("   - Hatch 的版本控制插件")
    print("   - 与 Hatch 构建系统集成")

    print("⚠️  需要安装相应的包")


def main():
    """主函数"""
    print("包信息获取解决方案演示")
    print("=" * 50)

    # 显示当前包信息
    print("当前包信息:")
    print(f"  包名: {pkg20.__package__}")
    print(f"  版本: {pkg20.__version__}")
    print(f"  作者: {pkg20.__author__}")
    print()

    # 演示各种解决方案
    demo_solution_1_importlib_metadata()
    demo_solution_2_our_utils()
    demo_solution_3_setuptools_scm()
    demo_solution_4_pkg_resources()
    demo_solution_5_third_party_packages()

    print("\n=== 推荐方案 ===")
    print("✅ 方案一：importlib.metadata - 标准库，推荐")
    print("✅ 方案二：我们的工具模块 - 封装好的，易用")
    print("⚠️  方案三：setuptools-scm - 需要配置，适合 git 项目")
    print("❌ 方案四：pkg_resources - 已弃用")
    print("⚠️  方案五：第三方包 - 根据项目需求选择")


if __name__ == "__main__":
    main()
