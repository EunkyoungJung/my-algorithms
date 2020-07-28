from collections import deque

"""
collections 패키지의 deque 모듈은 동적 배열이 아닌
"이중 연결리스트"를 기반으로 한다!
"""

q = deque([1, 2, 3])
print(q)
q.append(4)
print(q)
print(q.popleft())
print(q)
print(q.pop())
print(q)
print(q.appendleft(0))
print(q)
print("="*20)

"""
실행결과:
deque([1, 2, 3])
deque([1, 2, 3, 4])
1
deque([2, 3, 4])
4
deque([2, 3])
None
deque([0, 2, 3])
"""

q = deque([1,2,3,4])
print(q)

print(q.rotate(1))
print(q)
print(q.rotate(2))
print(q)

print(q.rotate(-1))
print(q)
print(q.rotate(-2))
print(q)

"""
실행결과:
deque([1, 2, 3, 4])
None
deque([4, 1, 2, 3])
None
deque([2, 3, 4, 1])
None
deque([3, 4, 1, 2])
None
deque([1, 2, 3, 4])
"""