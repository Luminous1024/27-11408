def generate_full_tree(n=5):
    """生成完整汉诺塔递归树的节点和边，节点序号全局唯一（从1开始）"""
    nodes = []      # 存储 (id, label)
    edges = []      # 存储 (parent_id, child_id)
    counter = 1

    def dfs(n, from_, buffer_, to_, parent_id=None):
        nonlocal counter
        current_id = counter
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

    dfs(n, 'A', 'B', 'C')  # 根节点参数
    return nodes, edges

def extract_subtree(root_id, nodes, edges):
    """从完整树中提取以 root_id 为根的子树的所有节点和边"""
    reachable = set()
    stack = [root_id]
    while stack:
        node = stack.pop()
        if node in reachable:
            continue
        reachable.add(node)
        # 找出所有以 node 为起点的边的终点
        for parent, child in edges:
            if parent == node and child not in reachable:
                stack.append(child)
    # 过滤节点和边
    sub_nodes = [node for node in nodes if node[0] in reachable]
    sub_edges = [edge for edge in edges if edge[0] in reachable and edge[1] in reachable]
    return sub_nodes, sub_edges

def generate_subtree_mermaid_from_data(sub_nodes, sub_edges, title):
    """根据节点和边数据生成 Mermaid 代码块"""
    mermaid_lines = ["flowchart TD"]
    for nid, label in sub_nodes:
        mermaid_lines.append(f'    {nid}["{label}"]')
    for parent, child in sub_edges:
        mermaid_lines.append(f"    {parent} --> {child}")
    return f"### {title}\n```mermaid\n" + "\n".join(mermaid_lines) + "\n```"

# 主程序：生成完整树并输出四个子图
if __name__ == "__main__":
    # 1. 生成完整树（n=5）
    nodes, edges = generate_full_tree(5)

    # 2. 找出根节点的三个孩子（按深度优先顺序）
    root_children = [child for parent, child in edges if parent == 1]

    # 3. 输出四个子图
    # 根节点图
    root_nodes = [node for node in nodes if node[0] == 1]
    root_edges = []
    print(generate_subtree_mermaid_from_data(root_nodes, root_edges, "根节点：hanoi(5, A, B, C)"))

    # 左子树图
    left_nodes, left_edges = extract_subtree(root_children[0], nodes, edges)
    print(generate_subtree_mermaid_from_data(left_nodes, left_edges, "左子树：hanoi(4, A, C, B)"))

    # 中子树图
    mid_nodes, mid_edges = extract_subtree(root_children[1], nodes, edges)
    print(generate_subtree_mermaid_from_data(mid_nodes, mid_edges, "中子树：hanoi(1, A, B, C)"))

    # 右子树图
    right_nodes, right_edges = extract_subtree(root_children[2], nodes, edges)
    print(generate_subtree_mermaid_from_data(right_nodes, right_edges, "右子树：hanoi(4, B, A, C)"))