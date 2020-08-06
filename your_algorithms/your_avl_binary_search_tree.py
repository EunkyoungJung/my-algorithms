"""
AVL 트리
- 왼쪽과 오른쪽 하위 트리의 높이 차이가 1보다 클 수 없는 자체 균형 조건을 가진 이진 탐색 트리
- 트리에 노드를 추가 또는 삭제할 때마다 이진 탐색 트리 클래스에 자가 균형 조정 메서드 호출을 추가하면, AVL 트리를 구현할 수 있다.
- 이 메서드는 노드가 추가 또는 삭제될 때마다 트리의 높이를 계속 확인하여 동작한다.

탐색 AVL 트리의 삽입을 구현하는 순서:
1) 이전에 구현한 이진 탐색 트리 구현과 같이 재귀 함수를 사용하여 상향식으로 구현
2) 현재 노드는 새로 삽입될 노드의 조상 노드 중 하나다. 노드가 삽입될 때 조상 노드의 높이를 갱신한다.
3) 현재 노드의 균형도를 계산한다. (현재 노드의 왼쪽 하위 트리 높이 - 현재 노드의 오른쪽 하위 트리 높이)
4) 트리의 균형도가 맞지 않는 경우는 회전한다.
    4-1) 균형도가 1보다 큰 경우 LL 케이스와 LR 케이스가 있다.
        - 새 노드 값이 현재 노드의 왼쪽 노드 값보다 작다면 LL 케이스다.
          R 회전을 수행한다.
        - 새 노드 값이 현재 노드의 왼쪽 노드보다 크다면 LR 케이스다.
          LR 회전을 수행한다.
    4-2) 균형도가 -1보다 작은 경우 RR 케이스와 RL 케이스가 있다.
        - 새 노드 값이 현재 노드의 오른쪽 노드 값보다 크다면 RR 케이스다.
          L 회전을 수행한다.
        - 새 노드 값이 현재 노드의 오른쪽 노드보다 작다면 RL 케이스다.
          RL 회전을 수행한다.
"""


from your_binary_tree import NodeBT, BinaryTree


class NodeAVL(NodeBT):
    def __init__(self, value=None, height=1):
        self.value = value
        self.height = height # 높이(height)는 +1로 계산한다.
        self.left = None
        self.right = None

    def insert(self, value):
        # 1) 이진 탐색 트리 노드 삽입
        new_node = NodeAVL(value)
        if value < self.value:
            self.left = self.left and self.left.insert(value) or new_node
        elif value > self.value:
            self.right = self.right and self.right.insert(value) or new_node
        else:
            raise Exception("중복 노드를 허용하지 않습니다.")

        # 회전 메서드에서 높이를 설정한다.
        return self.rotate(value)

    def rotate(self, value):
        # 2) (조상) 노드의 높이를 갱신한다.
        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))

        # 3) 균형도(왼쪽 트리 높이 - 오른쪽 트리 높이)
        balance = self.get_balance()

        # 4) 트리의 균형이 맞지 않을 경우 회전한다.
        if balance > 1:
            # [케이스 1] LL - LEFT LEFT
            if value < self.left.value:
                return self.right_rotate()

            # [케이스 2] LR - LEFT RIGHT
            elif value > self.left.value:
                self.left = self.left.left_rotate()
                return self.right_rotate()

        elif balance < -1:
            # [케이스 3] RR - RIGHT RIGHT
            if value > self.right.value:
                return self.left_roate()

            # [케이스 4] RL - RIGHT LEFT
            elif value < self.right.value:
                self.right = self.right.right_rotate()
                return self.left_rotate()

    def left_rotate(self):
        x = self.right
        T2 = x.left

        # 회전한 후,
        x.left = self
        self.right = T2

        # 높이를 갱신한다.
        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def right_rotate(self):
        y = self.left
        T2 = y.right

        y.right = self
        self.left = T2

        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height)

        return y

    def get_height(self, node):
        if not node:
            return 0

        return node.height

    def get_balance(self):
        return self.get_height(self.left) - self.get_height(self.right)

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node

        return self.get_min_value_node(node.left)

    def delete(self, value):
        # 1) 이진 탐색 트리 노드 삭제
        if value < self.value:
            self.left = self.left and self.left.delete(value)
        elif value > self.value:
            self.right = self.right and self.right.delete(value)
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp

            temp = self.get_min_value_node(self.right)
            self.value = temp.value
            self.right = self.right and self.right.delete(temp.value)

        if self is None:
            return None

        return self.rotate(value)


class AVLTree(BinaryTree):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = NodeAVL(value)
        else:
            self.root = self.root.insert(value)

    def delete(self, value):
        self.root = self.root.delete(value)


def preorder(root):
    if root:
        print(f"({root.value}, {root.height-1}) ", end="")
        if root.left:
            preorder(root.left)
        if root.right:
            preorder(root.right)


if __name__ == "__main__":
    myTree = AVLTree()
    for i in range(10, 100, 10):
        myTree.insert(i)

    print(f"{myTree.get_height()}")
    print(f"{myTree.is_binary_search_tree()}")
    print(f"{myTree.is_balanced()}")
    preorder(myTree.root)
    print()