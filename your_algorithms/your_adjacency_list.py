"""
인접리스트 (adjacency list)
- 각 노드에서 이웃 리스트(set 또는 container와 같은 iterable한 객체)에 접근할 수 있음
- n개의 노드가 있을 때, 각 노드의 인접(또는 이웃) 리스트는 단순히 숫자 리스트다.
- 숫자로 노드에 접근 가능한(인덱싱 가능한) n개의 메인 리스트에 각 노드의 인접 리스트를 추가하면 된다.
- 인접 리스트의 추가 순서를 보통 임의적이다.
"""


a, b, c, d, e, f = range(6) # 6개 노드
N = [{b, c, d, f}, {a, d, f}, {a, b,d, e}, {a, e}, {a, b, c}, {b, c, d, e}]
print(b in N[a]) # True
print(b in N[b]) # False
print(len(N[f])) # 4

