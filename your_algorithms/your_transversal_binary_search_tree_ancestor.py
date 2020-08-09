"""
이진 검색 트리에서 두 노드의 최소 공통 조상(lowest common anscestor)을 찾는 문제
"""


from your_transversal_binary_search_tree_recursively import BSTwithTransversalRecursively


def find_ancestor(path, low_value, high_value):
    while path:
        current_value = path[0]
        if current_value < low_value:
            try:
                path = path[2:]
            except:
                return current_value
        elif current_value > high_value:
            try:
                path = path[1:]
            except:
                return current_value
        elif low_value <= current_value <= high_value:
            return current_value


if __name__ == "__main__":
    bst = BSTwithTransversalRecursively()
    l = [10, 5, 6, 3, 8, 2, 1, 11, 9, 4]
    for i in l:
        bst.add_node(i)
    path = bst.preorder()
    print(f"전위 순회: {path}")
    print(f"{find_ancestor(path, 1, 6)}")
    print(f"{find_ancestor(path, 1, 11)}")
    print(f"{find_ancestor(path, 1, 4)}")
    print(f"{find_ancestor(path, 8, 9)}")