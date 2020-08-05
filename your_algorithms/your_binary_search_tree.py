"""
이진 탐색 트리 (Binary Search Tree)
- 노드를 정렬된 순서로 유지하는 이진 트리
- 노드의 왼쪽 하위 트리에는 노드의 값보다 작은 값의 노드만 존재
- 노드의 오른쪽 하위 트리에는 노드의 값보다 큰 값의 노드만 존재
- 왼쪽과 오른쪽 하위 트리 모드 이진 탐색 트리여야 함
- 중복 노드가 없어야 함
- 이진 탐색 트리가 균형 트리인 경우 노드 검색/삽입/삭제에 대한 시간복잡도는 O(log n)이다.
"""

from your_binary_tree import NodeBT, BinaryTree


class NodeBST(NodeBT):

    def __init__(self, value=None, level=1):
        self.value = value
        self.level = level
        self.left = None
        self.right = None

    def _add_next_node(self, value, level_here=2):
        new_node = NodeBT(value, level_here)
        if value > self.value:
            self.right = self.right and self.right._add_next_node(value, level_here + 1) or new_node
        elif value < self.value:
            self.left = self.left and self.left._add_next_node(value, level_here + 1) or new_node
        else:
            print("중복 노드를 허용하지 않습니다.")
        return self

    def _search_for_node(self, value):
        if self.value == value:
            return self
        elif self.left and value < self.value:
            return self.left._search_for_node(value)
        elif self.right and value > self.value:
            return self.right._search_for_node(value)
        else:
            return False


class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None

    def add_node(self, value):
        if not self.root:
            self.root = NodeBT(value)
        else:
            self.root._add_next_node(value)


if __name__ == "__main__":
    bst = BinarySearchTree()
    for i in [6, 4, 8, 2, 5, 7, 9, 1, 3]:
        bst.add_node(i)

    print(f"{bst.is_leaf(8)}")
    print(f"{bst.get_node_level(1)}")
    print(f"{bst.is_root(10)}")
    print(f"{bst.is_root(1)}")
    print(f"{bst.get_height()}")
    print(f"{bst.is_bst()}")
    print(f"{bst.is_balanced()}")
