"""
재귀 함수를 이용해서 트리 순회 구현하기
"""


from your_binary_search_tree import BinarySearchTree, NodeBST


class BSTwithTransversalRecursively(BinarySearchTree):

    def __init__(self):
        self.root = None
        self.nodes_BFS = []
        self.nodes_pre = []
        self.nodes_post = []
        self.nodes_in = []

    def BFT(self):
        self.root.level = 1
        queue = [self.root]
        current_level = self.root.level

        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.level > current_level:
                current_level += 1
            self.nodes_BFS.append(current_node.level)

            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)

            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)

        return self.nodes_BFS

    def inorder(self, node=None, level=1):
        if not node and level == 1:
            node = self.root
        if node:
            self.inorder(node.left, level+1)
            self.nodes_in.append(node.value)
            self.inorder(node.right, level+1)
        return self.nodes_in

    def preorder(self, node=None, level=1):
        if not node and level == 1:
            node = self.root
        if node:
            self.nodes_pre.append(node.value)
            self.preorder(node.left, level+1)
            self.preorder(node.right, level+1)
        return self.nodes_pre

    def postorder(self, node=None, level=1):
        if not node and level == 1:
            node = self.root
        if node:
            self.postorder(node.left, level+1)
            self.postorder(node.right, level+1)
            self.nodes_post.append(node.value)
        return self.nodes_post


def test_transversal_recursive_bst():
    bst = BSTwithTransversalRecursively()
    l = [10, 5, 6, 3, 8, 2, 1, 11, 9, 4]
    for i in l:
        bst.add_node(i)

    assert(bst.is_leaf(8) is True)
    assert(bst.get_node_level(8) == 3)
    assert(bst.is_root(8) is False)
    assert(bst.is_root(1) is False)
    assert(bst.get_height() == 5)
    assert(bst.is_binary_search_tree() is False)
    assert(bst.is_balanced() is False)
    assert(bst.preorder() == [10, 5, 3, 2, 11, 4, 9, 1, 8, 6])
    assert(bst.postorder() == [4, 11, 9, 2, 1, 3, 8, 5, 6, 10])
    assert(bst.inorder() == [4, 11, 2, 9, 3, 1, 5, 8, 10, 6])
    assert(bst.BFT() == [1, 2, 2, 3, 3, 4, 4, 5, 5, 6])


if __name__== "__main__":
    test_transversal_recursive_bst()
    bst = BSTwithTransversalRecursively()
    l = [10, 5, 6, 3, 8, 2, 1, 11, 9, 4]
    for i in l:
        bst.add_node(i)

    print(f"{bst.is_leaf(8)}")
    print(f"{bst.get_node_level(8)}")
    print(f"{bst.is_root(8)}")
    print(f"{bst.is_root(1)}")
    print(f"{bst.get_height()}")
    print(f"{bst.is_binary_search_tree()}")
    print(f"{bst.is_balanced()}")
    print(f"{bst.preorder()}")
    print(f"{bst.postorder()}")
    print(f"{bst.inorder()}")
    print(f"{bst.BFT()}")