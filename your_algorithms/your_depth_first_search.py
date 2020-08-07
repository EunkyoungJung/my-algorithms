""""
깊이 우선 탐색 (Depth First Search)
- 그래프 또는 트리에서 깊이를 우선하여 탐색하는 알고리즘
- 그래프의 경우는 방문한 노드를 표시해야 한느데, 그렇게 하지 않으면 무한 반복에 빠질 수 있기 때문이다.
- 시간복잡도는 O(도달할 수 있는 도드 수 + 도달할 노드에서 나가는 간선 수) = O(V + E)다.
- 깊이 우선 탐색은 후입선출(LIFO) 구조의 스택을 사용하여 구현한다.
"""

# 깊이 우선 탐색의 세가지 경우:
#1) 전위 순회 (pre-order traversal)
#    : 루트 노드 -> 왼쪽 노드 -> 오른쪽 노드
def preorder(root):
    if root != 0:
        yield root.value
        preorder(root.left)
        preorder(root.right)

#2) 후위 순회 (post-order traversal)
#    : 왼쪽 노드 -> 오른쪽 노드 -> 루트 노드
def postorder(root):
    if root != 0:
        postorder(root.left)
        postorder(root.right)
        yield root.value

#3) 중위 순회 (in-order traversal)
#    : 왼쪽 노드 -> 루트 노드 -> 오른쪽 노드
def inorder(root)
    if root != 0:
        inorder(root.left)
        yield root.value
        inorder(root.right)
