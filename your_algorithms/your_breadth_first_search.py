"""
너비 우선 검색 (breath first search)
- 정점들과 같은 레벨에 있는 노드들 (형제 노드들)을 먼저 탐색하는 방식
- 한 노드의 자식을 타고 끝까지 순회한 후, 다시 돌아와서 다른 형제들의 자식을 타고 내려가면 순회함
"""

import doctest


# 자료구조 스택과 큐를 사용하여 DFS 구현하기
def deep_first_search(graph: dict, start_node) -> list:
    """
    파라미터로 전달받은 시작노드(start_node)부터 graph의 끝까진 DFS로 순회한 결과를 리스트로 출력하는 함수
    :param graph: graph정보가 담기 dictionary
    :param start_node: dictionary의 키
    :return: dfs 결과를 list로 반환

    >>> graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'G', 'H', 'I'], 'D': ['B', 'E', 'F'],'E': ['D'], 'F': ['D'], 'G': ['C'], 'H': ['C'], 'I': ['C', 'J'], 'J': ['I']}
    >>> deep_first_search(graph, 'A')
    ['A', 'B', 'C', 'D', 'G', 'H', 'I', 'E', 'F', 'J']
    """
    visited, need_visit = list(), list()
    # print(f"visited: {visited} / need_visit: {need_visit}")
    need_visit.append(start_node)

    while need_visit:
        # print(f"visited: {visited} / need_visit: {need_visit}")
        node = need_visit.pop(0)
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
