"""
이진 트리 구현하기
"""


class Height(object):
    def __init__(self):
        self.height = 0


class NodeBT(object):
    def __init__(self, value=None, level=1):
        self.value = value
        self.level = level
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.value}"

    def _add_next_node(self, value, level_here=2):
        new_node = NodeBT(value, level_here)
        if not self.value:
            self.value = new_node
        elif not self.left:
            self.left = new_node
        elif not self.right:
            self.right = new_node
        else:
            # 노드에서 왼쪽 오른쪽 자식이 모두 있다면
            # 왼쪽 자식 노드에 새 노드를 추가한다
            # 그래서 예제의 트리가 왼쪽으로 치우져 있다
            self.left = self.left._add_next_node(value, level_here+1)
        return self

    def _search_for_node(self, value):
        # 전위 순회(pre-order)로 값을 찾는다
        if self.value == value:
            return self
        else:
            found = None
            if self.left:
                found = self.left._search_for_node(value)
            if self.right:
                found = self.right._search_for_node(value)
            return found

    def _is_leaf(self):
        # 왼쪽/오른쪽 자식이 모두 없는 노드
        return not self.right and not self.left

    def _get_max_height(self):
        # 노드의 최대 높이
        height_left, height_right = 0, 0
        if self.right:
            height_right = self.right._get_max_height() + 1
        if self.left:
            height_left = self.left._get_max_height() + 1
        return max(height_right, height_left)

    def _is_balanced(self, height=Height()):
        # 균형 트리인지 확인
        left_height = Height()
        right_height = Height()

        if self.value is None:
            return True

        left, right = True, True
        if self.left:
            left = self.left._is_balanced(left_height)
        if self.right:
            right = self.right._is_balanced(right_height)

        height.height = max(left_height.height, right_height.height) + 1

        if abs(left_height.height - right_height.height) <= 1:
            return left and right

        return False

    def _is_binary_search_tree(self, left=None, right=None):
        # 이진 탐색 트리인지 확인
        #  left child < parent node < right child
        if self.value:
            if left and self.value < left:
                return False
            if right and self.value > right:
                return False

            left, right = True, True
            if self.left:
                left = self.left._is_binary_search_tree(left, self.value)
            if self.right:
                right = self.right._is_binary_search_tree(self.value, left)
            return left and right
        else:
            return True


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def add_node(self, value):
        if not self.root:
            self.root = NodeBT(value)
        else:
            self.root._add_next_node(value)

    def is_leaf(self, value):
        node = self.root._search_for_node(value)
        if node:
            return node._is_leaf()
        else:
            return False

    def get_node_level(self, value):
        node = self.root._search_for_node(value)
        if node:
            return node.level
        else:
            return False

    def is_root(self, value):
        return self.root.value == value

    def get_height(self):
        return self.root._get_max_height()

    def is_balanced(self):
        return self.root._is_balanced()

    def is_binary_search_tree(self):
        return self.root._is_binary_search_tree()


if __name__ == "__main__":
    bt = BinaryTree()
    for i in range(1, 10):
        bt.add_node(i)
    print(f"{bt.is_leaf(8)}")
    print(f"{bt.get_node_level(8)}")
    print(f"{bt.is_root(10)}")
    print(f"{bt.is_root(1)}")
    print(f"{bt.get_height()}")
    print(f"{bt.is_binary_search_tree()}")
    print(f"{bt.is_balanced()}")