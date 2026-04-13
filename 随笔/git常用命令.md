---
tags:
  - 随笔
  - git常用命令
创建时间: 2026-04-13T11:40:00
---
以下是日常开发中最常用的 Git 命令及简要说明，按使用场景分类：

## 1. 仓库初始化与克隆
| 命令 | 说明 |
|------|------|
| `git init` | 在当前目录初始化一个新的 Git 仓库 |
| `git clone <url>` | 克隆远程仓库到本地 |

## 2. 基本快照操作
| 命令 | 说明 |
|------|------|
| `git status` | 查看工作区和暂存区的状态 |
| `git add <file>` | 将文件添加到暂存区（`git add .` 添加所有） |
| `git commit -m "message"` | 提交暂存区内容并附上提交信息 |
| `git commit -a -m "message"` | 跳过暂存区，直接提交所有已跟踪的修改 |
| `git diff` | 查看工作区与暂存区的差异 |
| `git diff --staged` | 查看暂存区与最新提交的差异 |

## 3. 分支与合并
| 命令 | 说明 |
|------|------|
| `git branch` | 列出本地分支（`-r` 远程分支，`-a` 所有分支） |
| `git branch <name>` | 创建新分支 |
| `git checkout <branch>` | 切换到指定分支 |
| `git switch <branch>` | 新式切换分支（Git 2.23+） |
| `git checkout -b <branch>` | 创建并切换到新分支 |
| `git merge <branch>` | 将指定分支合并到当前分支 |
| `git branch -d <branch>` | 删除分支（`-D` 强制删除） |

## 4. 远程操作
| 命令 | 说明 |
|------|------|
| `git remote -v` | 查看远程仓库地址 |
| `git remote add origin <url>` | 添加远程仓库地址 |
| `git fetch` | 拉取远程更新但不合并 |
| `git pull` | 拉取远程更新并合并（相当于 `fetch + merge`） |
| `git push origin <branch>` | 推送本地分支到远程 |
| `git push -u origin <branch>` | 推送并建立上游追踪关系 |
| `git push --force` | 强制推送（慎用） |

## 5. 历史与日志
| 命令 | 说明 |
|------|------|
| `git log` | 查看提交历史（`--oneline` 单行显示，`--graph` 图形化） |
| `git log -p` | 显示每次提交的差异 |
| `git blame <file>` | 查看文件的每一行是谁在什么时候修改的 |
| `git reflog` | 记录所有 HEAD 的移动（用于找回丢失的提交） |

## 6. 撤销与重置
| 命令 | 说明 |
|------|------|
| `git reset HEAD <file>` | 将文件从暂存区撤出（不影响工作区） |
| `git reset --soft <commit>` | 撤销到指定提交，保留工作区和暂存区修改 |
| `git reset --hard <commit>` | 撤销到指定提交，丢弃所有修改（危险） |
| `git revert <commit>` | 用一次新提交来撤销指定提交（安全） |
| `git restore <file>` | 丢弃工作区的修改（Git 2.23+） |
| `git restore --staged <file>` | 将文件从暂存区撤出（同 `reset HEAD`） |

## 7. 暂存与清理
| 命令 | 说明 |
|------|------|
| `git stash` | 暂时保存未提交的修改 |
| `git stash pop` | 恢复最近一次暂存并删除该暂存记录 |
| `git stash list` | 查看所有暂存记录 |
| `git clean -fd` | 删除未跟踪的文件和目录 |

## 8. 标签
| 命令 | 说明 |
|------|------|
| `git tag` | 列出所有标签 |
| `git tag <name>` | 创建轻量标签 |
| `git tag -a <name> -m "msg"` | 创建附注标签 |
| `git push origin --tags` | 推送所有标签到远程 |

## 9. 配置与帮助
| 命令 | 说明 |
|------|------|
| `git config --global user.name "name"` | 设置全局用户名 |
| `git config --global user.email "email"` | 设置全局邮箱 |
| `git config --list` | 查看当前配置 |
| `git help <command>` | 查看某个命令的帮助文档 |

---

> **提示**：实际使用中，建议结合 `git status` 频繁确认状态，并养成写清晰提交信息的习惯。对于复杂操作（如 rebase、cherry-pick 等），可根据需要进一步学习。