"""
트리 순회 구현하기
"""
from collections import deque
from your_binary_search_tree import BinarySearchTree, NodeBST


class BSTwithTransversalIterative(BinarySearchTree):

    def inorder(self):
        current = self.root
        nodes, stack = [], []
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                nodes.append(current.value)
                current = current.right
        return nodes

    def preorder(self):
        current = self.root
        nodes, stack = [], []
        while stack or current:
            if current:
                nodes.append(current.value)
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right

    def preorder2(self):
        nodes = []
        stack = [self.root]
        while stack:
            current = stack.pop()
            if current:
                nodes.append(current.value)
                stack.append(current.right)
                stack.append(current.left)
        return nodes

    def BST(self):
        current = self.root
        nodes = []
        queue = deque()
        queue.append(current)
        while queue:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return nodes


def test_transversal_bst():
    bst = BSTwithTransversalIterative()
    l = [10, 5, 6, 3, 8, 2, 1, 11, 9, 4]
    for i in l:
        bst.add_node(i)
    assert(bst.is_leaf(8) is True)
    assert(bst.get_node_level(8) == 3)
    assert(bst.is_root(10) is True)
    assert(bst.is_root(1) is False)
    assert(bst.get_height() == 5)
    assert(bst.get_height() == 5)
    assert(bst.is_binary_search_tree() is False)
    assert(bst.is_balanced() is False)
    assert(bst.preorder() is None)
    assert(bst.preorder2() == [10, 5, 3, 2, 11, 4, 9, 1, 8, 6])
    assert(bst.inorder() == [4, 11, 2, 9, 3, 1, 5, 8, 10, 6])
    assert(bst.BST() == [])


if __name__ == "__main__":
    test_transversal_bst()

    bst = BSTwithTransversalIterative()
    l = [10, 5, 6, 3, 8, 2, 1, 11, 9, 4]
    for i in l:
        bst.add_node(i)

    print(f"{bst.is_leaf(8)}")
    print(f"{bst.get_node_level(8)}")
    print(f"{bst.is_root(10)}")
    print(f"{bst.is_root(1)}")
    print(f"{bst.get_height()}")
    print(f"{bst.get_height()}")
    print(f"{bst.is_binary_search_tree()}")
    print(f"{bst.is_balanced()}")
    print(f"{bst.preorder()}")
    print(f"{bst.preorder2()}")
    print(f"{bst.inorder()}")
    print(f"{bst.BST()}")

