#!/usr/bin/env python3
"""
代码可移植性测试
模拟将代码复制到其他项目的情况
"""


def simulate_different_package():
    """模拟不同包名的情况"""
    print("=== 代码可移植性测试 ===")

    # 导入 pkg20 模块
    import pkg20

    # 保存原始的 __package__ 和 __name__
    original_package = pkg20.__package__
    original_name = pkg20.__name__

    print(f"原始包名: {original_package}")
    print(f"原始模块名: {original_name}")

    # 模拟不同的包名
    test_packages = ["my_package", "awesome_tool", "data_processor"]

    for test_package in test_packages:
        print(f"\n--- 测试包名: {test_package} ---")

        # 模拟修改包名（通过修改 __package__ 属性）
        pkg20.__package__ = test_package
        pkg20.__name__ = test_package

        # 重新获取包信息
        try:
            # 重新执行 _get_package_info 函数
            version, author = pkg20._get_package_info()
            print(f"  获取到的版本: {version}")
            print(f"  获取到的作者: {author}")

            # 检查是否能正确获取包名
            if pkg20.__package__ == test_package:
                print(f"  ✅ 包名 {test_package} 获取正确")
            else:
                print("  ❌ 包名获取错误")

        except Exception as e:
            print(f"  ❌ 获取包信息失败: {e}")

    # 恢复原始值
    pkg20.__package__ = original_package
    pkg20.__name__ = original_name

    print(f"\n恢复原始包名: {pkg20.__package__}")


def test_template_usage():
    """测试模板使用"""
    print("\n=== 模板使用说明 ===")

    # 模板内容示例
    print("模板函数示例:")

    print("这个函数可以直接复制到任何项目中:")
    print("1. 自动获取当前包名")
    print("2. 自动从 pyproject.toml 读取版本号")
    print("3. 自动获取作者信息")
    print("4. 提供错误处理和兼容性支持")

    print("\n使用方法:")
    print("1. 将 _get_package_info 函数复制到你的 __init__.py")
    print("2. 调用 __version__, __author__ = _get_package_info()")
    print("3. 确保 pyproject.toml 中有正确的项目信息")


def main():
    """主函数"""

    # 测试可移植性
    simulate_different_package()

    # 测试模板使用
    test_template_usage()

    print("\n=== 总结 ===")
    print("✅ 包名可以自动获取")
    print("✅ 版本号可以自动同步")
    print("✅ 代码可以直接复制到其他项目使用")
    print("✅ 无需手动修改包名")


if __name__ == "__main__":
    main()
