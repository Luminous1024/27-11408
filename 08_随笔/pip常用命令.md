---
tags:
  - 随笔
  - pip常用命令
创建时间: 2026-04-13T11:40:00
---
pip 的常用命令主要围绕 Python 包的整个生命周期来划分，涵盖了安装、卸载、查看、管理依赖等关键环节。

### 📦 包管理核心命令

| 命令 | 功能描述 | 示例 |
| :--- | :--- | :--- |
| **`install`** | 安装 Python 包，可指定版本、从文件批量安装或升级包。 | `pip install requests` <br> `pip install requests==2.25.1` <br> `pip install -r requirements.txt` <br> `pip install --upgrade pip` |
| **`uninstall`** | 卸载已安装的 Python 包。 | `pip uninstall requests` <br> `pip uninstall -r requirements.txt -y` |
| **`list`** | 列出当前环境中已安装的所有包。 | `pip list` <br> `pip list --outdated` <br> `pip list --not-required` |
| **`show`** | 显示一个或多个已安装包的详细信息（如版本、依赖、位置）。 | `pip show requests` |
| **`freeze`** | 以 `requirements.txt` 的格式输出当前环境所有已安装的包及其精确版本，用于环境复制。 | `pip freeze > requirements.txt` |
| **`download`** | 下载包但不安装，可配合 `-d` 指定下载目录。 | `pip download requests -d ./packages` |
| **`wheel`** | 为指定的包构建 `.whl` 格式的安装包。 | `pip wheel requests` |

### ⚙️ 环境与管理命令

| 命令 | 功能描述 | 示例 |
| :--- | :--- | :--- |
| **`--version` / `-V`** | 查看当前 pip 的版本号及关联的 Python 版本。 | `pip --version` |
| **`--help`** | 获取 pip 的通用帮助信息或特定命令的详细用法。 | `pip --help` <br> `pip install --help` |
| **`check`** | 检查当前环境中已安装的包是否具有兼容的依赖关系。 | `pip check` |
| **`config`** | 管理 pip 的配置文件。 | `pip config list` <br> `pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple` |
| **`cache`** | 管理 pip 的本地下载缓存，如清理、列出缓存内容等。 | `pip cache list` <br> `pip cache purge` |
| **`hash`** | 计算包的哈希值，通常用于确保下载的包未被篡改。 | `pip hash requirements.txt` |

> **关于 `search` 命令**：`pip search` 在较新版本中已被官方禁用。如需搜索，可直接访问 [PyPI 官网](https://pypi.org/search)。

### 💡 通用选项与最佳实践

这些选项常与其他命令搭配使用，以调整 pip 的行为：

*   `-i, --index-url <url>`：指定一个镜像源来安装包，可有效提升下载速度。例如使用清华源：`pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple`。
*   `-r, --requirement <file>`：从一个 `requirements.txt` 文件批量安装或卸载包。
*   `-U, --upgrade`：将已安装的包升级到最新版本。
*   `-e, --editable`：以"可编辑"模式安装本地项目，通常用于开发。
*   `-v, --verbose`：在命令执行时输出更详细的运行信息，有助于调试。
*   `-q, --quiet`：减少命令的输出信息，使其更简洁。
*   `--no-cache-dir`：禁用本地缓存，所有包都重新下载。

**💎 最佳实践**

*   **使用虚拟环境**：强烈建议使用 `venv` 或 `conda` 为每个项目创建独立的虚拟环境，以避免包版本冲突。
*   **依赖管理**：请使用 `pip freeze > requirements.txt` 精确记录项目依赖，并通过 `pip install -r requirements.txt` 在其他环境中一键重建。
*   **版本固定**：在 `requirements.txt` 中明确指定包的版本号，可确保不同环境安装的版本一致，避免意外错误。

如果你对某个具体命令的用法或场景想了解更多，可以随时再问我。