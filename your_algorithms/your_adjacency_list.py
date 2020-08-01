"""
인접리스트 (adjacency list)
- 각 노드에서 이웃 리스트(set 또는 container와 같은 iterable한 객체)에 접근할 수 있음
- n개의 노드가 있을 때, 각 노드의 인접(또는 이웃) 리스트는 단순히 숫자 리스트다.
- 숫자로 노드에 접근 가능한(인덱싱 가능한) n개의 메인 리스트에 각 노드의 인접 리스트를 추가하면 된다.
- 인접 리스트의 추가 순서를 보통 임의적이다.
"""


# Set을 이용한 인접 리스트
a, b, c, d, e, f = range(6) # 6개 노드
N = [{b, c, d, f}, {a, d, f}, {a, b,d, e}, {a, e}, {a, b, c}, {b, c, d, e}]
print(b in N[a]) # True
print(b in N[b]) # False
print(len(N[f])) # 4


# List를 이용한 인접 리스트
"""
<List를 이용한 인접 리스트>
- 모든 노드 V에서 N(V)를 효율적으로 순회할 수 있음
- 셋을 리스트로 바꾸면 멤버십 테스트의 시간복잡도가 O(n)이 된다.
- 알고리즘을 수행하는 어떤 작업이 이웃 노드를 반복해서 접근하는 경우 리스트를 사용하는 것이 좋을 것이다. 
- 그래프가 촘촘한 경우 (간선이 많은 경우)에는 set을 사용하는 게 더 좋다. 
- 파이썬 리스트 중간에서 어떤 한 객체를 삭제하는 시간복잡도는 O(n)이지만,
- 리스트 끝에서 삭제한다면 O(1)이다.
- 이웃 노드의 순서가 중요하지 않다면, 삭제하려는 임의이 이웃을 마지막 항목으로 위치를 바꾼(swap)다음, pop()을 호출하여 O(1)에 임의의 이웃을 삭제할 수 있다.
"""
a, b, c, d, e, f = range(6) # 6개 노드
N = [[b, c, d, f], [a, d, f], [a, b, d, e], [a, e], [a, b, c], [b, c, d, e]]
print(b in N[a]) # True
print(b in N[b]) # False
print(len(N[f])) # 4


# Dictionary
"""
<Dictionary를 이용한 인접 리스트>
- 노드가 키가 되고, 각 노드를 간선 가중치 등의 값으로 연결할 수 있다.
- 딕셔너리의 기본 구조를 활용하면 조금 더 유연하게 인접 리스트를 만들 수 있다.
"""
a, b, c, d, e, f = range(6) # 6개 노드
N = [
    {b: 2, c: 1, d: 4, f: 1}, {a: 4, d: 1, f: 4}, {a: 1, b: 1, d: 2, e: 4},
    {a: 3, e: 2}, {a: 3, b: 4, c: 1}, {b: 1, c: 2, d: 4, d: 3}
    ]
print(b in N[a]) # True
print(len(N[f])) # 3
print(N[a][b]) # 2

a, b, c, d, e, f = range(6) # 6개 노드
N = {'a': set('bcdf'), 'b': set('adf'), 'c': set('abde'), 'd': set('ae'), 'e': set('abc'), 'f': set('bcde')}
print('b' in N['a']) # True
print(len(N['f'])) # 4
