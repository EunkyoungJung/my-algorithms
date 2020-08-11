from collections import deque

"""
컬렉션의 deque 모듈은 동적배열이 아닌 이중 연결리스트임!

deque
append : 오른쪽 끝에 삽입
appendleft: 왼쪽 끝에 삽입
pop : 오른쪽 끝에서 제거
popleft : 왼쪽 끝에서 제거

rotate(n) : n이 양수이면 오른쪽으로 n만큼 시프트 / n이 음수이면 왼쪽으로 n만큼 시프트
"""

q = deque(['a', 'b', 'c'])
print(q)
# deque(['a', 'b', 'c'])

q.append('d')
print(q)
# deque(['a', 'b', 'c', 'd'])

q.popleft()
print(q)
# deque(['b', 'c', 'd'])

q.pop()
print(q)
# deque(['b', 'c'])

q.appendleft('e')
print(q)
# deque(['e', 'b', 'c'])


# rotate(양수)
q = deque([0, 1, 2, 3])
print(q)
# deque([0, 1, 2, 3])
q.rotate(1)
print(q)
# deque([3, 0, 1, 2])


# rotate(음수)
q = deque([0, 1, 2, 3])
print(q)
# deque([0, 1, 2, 3])
q.rotate(-1)
print(q)
# deque([1, 2, 3, 0])
