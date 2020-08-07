""""
깊이 우선 탐색 (Depth First Search)
- 그래프 또는 트리에서 깊이를 우선하여 탐색하는 알고리즘
- 그래프의 경우는 방문한 노드를 표시해야 한느데, 그렇게 하지 않으면 무한 반복에 빠질 수 있기 때문이다.
- 시간복잡도는 O(도달할 수 있는 도드 수 + 도달할 노드에서 나가는 간선 수) = O(V + E)다.
- 깊이 우선 탐색은 후입선출(LIFO) 구조의 스택을 사용하여 구현한다.
- 정점의 자식들을 먼저 탐색하는 방식
"""

import doctest


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
def inorder(root):
    if root != 0:
        inorder(root.left)
        yield root.value
        inorder(root.right)


# 자료구조 스택과 큐를 사용하여 DFS 구현하기
def deep_first_search(graph: dict, start_node) -> list:
    """
    파라미터로 전달받은 시작노드(start_node)부터 graph의 끝까진 DFS로 순회한 결과를 리스트로 출력하는 함수
    :param graph: graph정보가 담기 dictionary
    :param start_node: dictionary의 키
    :return: dfs 결과를 list로 반환

    >>> graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'G', 'H', 'I'], 'D': ['B', 'E', 'F'],'E': ['D'], 'F': ['D'], 'G': ['C'], 'H': ['C'], 'I': ['C', 'J'], 'J': ['I']}
    >>> deep_first_search(graph, 'A')
    ['A', 'C', 'I', 'J', 'H', 'G', 'B', 'D', 'F', 'E']
    """
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited


if __name__ == "__main__":
    doctest.testmod()
    graph = dict()
    graph['A'] = ['B', 'C']
    graph['B'] = ['A', 'D']
    graph['C'] = ['A', 'G', 'H', 'I']
    graph['D'] = ['B', 'E', 'F']
    graph['E'] = ['D']
    graph['F'] = ['D']
    graph['G'] = ['C']
    graph['H'] = ['C']
    graph['I'] = ['C', 'J']
    graph['J'] = ['I']
    deep_first_search(graph, 'A')