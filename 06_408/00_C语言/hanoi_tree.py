def generate_hanoi_mermaid(n=5, start_from='A', start_buffer='B', start_to='C'):
    """
    生成汉诺塔递归调用树的 Mermaid 流程图代码。
    采用深度优先遍历顺序为节点编号，每个节点包含调用参数和序号。
    """
    nodes = []       # 存储节点信息: (id, label)
    edges = []       # 存储边信息: (parent_id, child_id)
    counter = 1      # 节点计数器（从1开始）

    def dfs(n, from_, buffer_, to_, parent_id=None):
        nonlocal counter
        current_id = counter
        # 节点标签：序号 + 调用参数
        label = f"{current_id}: hanoi({n},{from_},{buffer_},{to_})"
        nodes.append((current_id, label))
        if parent_id is not None:
            edges.append((parent_id, current_id))
        counter += 1

        if n > 1:
            # 左子：将 n-1 个盘子从 from 移到 buffer
            dfs(n-1, from_, to_, buffer_, current_id)
            # 中子：将第 n 个盘子从 from 移到 to
            dfs(1, from_, buffer_, to_, current_id)
            # 右子：将 n-1 个盘子从 buffer 移到 to
            dfs(n-1, buffer_, from_, to_, current_id)
        # n == 1 时无子调用，直接返回（叶子节点）

    dfs(n, start_from, start_buffer, start_to)

    # 生成 Mermaid 代码
    mermaid_lines = ["flowchart TD"]
    for nid, label in nodes:
        # 节点文本需用双引号包裹以避免特殊字符冲突
        mermaid_lines.append(f'    {nid}["{label}"]')
    for parent, child in edges:
        mermaid_lines.append(f"    {parent} --> {child}")
    return "\n".join(mermaid_lines)

# 生成 n=5 的代码
mermaid_code = generate_hanoi_mermaid(4)
print(mermaid_code)
