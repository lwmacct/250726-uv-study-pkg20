# 包信息获取解决方案总结

## 问题描述

在 Python 包开发中，经常需要获取包的版本号、作者等信息。传统做法是在 `__init__.py` 中硬编码这些信息，但这样会导致：

1. 版本号需要手动维护多个地方
2. 容易忘记更新版本号
3. 代码不可移植到其他项目

## 解决方案对比

### 方案一：importlib.metadata（推荐）

**优点：**
- Python 3.8+ 标准库
- 直接从 `pyproject.toml` 读取信息
- 无需额外依赖
- 性能好

**使用方法：**
```python
try:
    from importlib.metadata import version, metadata
    __version__ = version("your_package_name")
    package_metadata = metadata("your_package_name")
    __author__ = package_metadata.get("Author", "Unknown")
except ImportError:
    __version__ = "0.1.0"
    __author__ = "Unknown"
```

**适用场景：** 大多数 Python 项目

### 方案二：setuptools-scm

**优点：**
- 从 git 标签自动生成版本号
- 支持开发版本和发布版本
- 与 git 工作流集成

**配置：**
```toml
[project]
name = "your_package"
dynamic = ["version"]

[tool.setuptools_scm]
version_scheme = "python-simplified-semver"
local_scheme = "node-and-timestamp"
```

**使用方法：**
```python
try:
    from importlib.metadata import version
    __version__ = version("your_package_name")
except ImportError:
    __version__ = "0.1.0"
```

**适用场景：** 使用 git 标签管理版本的项目

### 方案三：versioneer

**优点：**
- 专门为版本管理设计
- 支持多种版本控制工具
- 配置简单

**安装：**
```bash
pip install versioneer
```

**配置：**
```toml
[tool.versioneer]
version_file_source = "src/your_package/_version.py"
```

**适用场景：** 需要复杂版本管理的项目

### 方案四：dunamai

**优点：**
- 动态版本管理
- 支持多种版本控制工具
- 灵活的配置选项

**安装：**
```bash
pip install dunamai
```

**使用方法：**
```python
from dunamai import Version

__version__ = Version.from_git().serialize()
```

**适用场景：** 需要动态版本管理的项目

### 方案五：hatch-vcs

**优点：**
- 与 Hatch 构建系统集成
- 支持多种版本控制工具
- 配置简单

**安装：**
```bash
pip install hatch-vcs
```

**配置：**
```toml
[project]
name = "your_package"
dynamic = ["version"]

[build-system]
requires = ["hatchling", "hatch-vcs"]
build-backend = "hatchling.build"
```

**适用场景：** 使用 Hatch 构建系统的项目

## 推荐方案

### 对于大多数项目

**推荐使用 importlib.metadata：**

```python
# __init__.py
try:
    from importlib.metadata import version, metadata
    __version__ = version("your_package_name")
    package_metadata = metadata("your_package_name")
    __author__ = package_metadata.get("Author", "Unknown")
except ImportError:
    __version__ = "0.1.0"
    __author__ = "Unknown"
```

### 对于使用 git 的项目

**推荐使用 setuptools-scm：**

```toml
# pyproject.toml
[project]
name = "your_package"
dynamic = ["version"]

[tool.setuptools_scm]
version_scheme = "python-simplified-semver"
local_scheme = "node-and-timestamp"
```

```python
# __init__.py
try:
    from importlib.metadata import version
    __version__ = version("your_package_name")
except ImportError:
    __version__ = "0.1.0"
```

## 我们的实现

在本项目中，我们提供了：

1. **工具模块**：`src/pkg20/utils/package_info.py`
   - 封装了包信息获取功能
   - 提供了多种便捷函数
   - 支持自定义默认值

2. **模板文件**：`templates/universal_init_template.py`
   - 可直接复制到其他项目使用
   - 包含完整的错误处理

3. **演示脚本**：`examples/package_solutions_demo.py`
   - 展示了各种解决方案
   - 提供了使用示例

## 总结

- **简单项目**：使用 importlib.metadata
- **git 项目**：使用 setuptools-scm
- **复杂需求**：使用 versioneer 或 dunamai
- **Hatch 项目**：使用 hatch-vcs

选择哪种方案主要取决于：
1. 项目的复杂度
2. 版本管理需求
3. 构建系统选择
4. 团队偏好 