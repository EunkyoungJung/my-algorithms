"""
Heap (디폴트가 최소힙)
- 각 노드가 하위 노드보다 작은(또는 큰) 이진 트리
- 균형 트리의 모양이 수정될 때, 다시 이를 균형 트리로 만드는 시간복잡도는 O(log n)
- 힙은 일반적으로, 리스트에서 가장 작은(또는 가장 큰) 요소에 반복적으로 접근하는 프로그램에 유용함
- 최소(또는 최대) 힙을 사용하면 가장 작은(또는 가장 큰) 요소를 처리하는 시간복잡도는 O(1)이고,
- 그 외의 조회, 추가, 수정을 처리하는 시간복잡도는 O(log n)임
"""


# play with heapq module
import heapq

"""
list1과 list2는 원소를 같지만 그 순서가 다름
각각을 heapq.heapify()를 한 결과로 출력되는 리스트가 똑같지는 않음!
다만, 어쟀든! 
heapq.heqpify()를 하면 가장 작은 원소인 "1"이 첫번째 원소로 배치됨을 알 수 있음!
그리고 어쨌는 heappop()을 하면 가장 작은 것들부터 출력됨을 알 수 있음!
"""
list1 = [4, 6, 8, 1]
heapq.heapify(list1)
print(list1)
# [1, 4, 8, 6]

list2 = [8, 6, 4, 1]
heapq.heapify(list2)
print(list2)
# [1, 6, 4, 8]

for i in range(4):
    print(f"list1.heappop: {heapq.heappop(list1)}, list2.heappop: {heapq.heappop(list2)}")
"""
list1.heappop: 1, list2.heappop: 1
list1.heappop: 4, list2.heappop: 4
list1.heappop: 6, list2.heappop: 6
list1.heappop: 8, list2.heappop: 8
"""



"""
우선순위 힙
"""
h = []
heapq.heappush(h, (1, 'ab'))
heapq.heappush(h, (1, 'a'))
heapq.heappush(h, (1, 'a'))
heapq.heappush(h, (1, 'ac'))
heapq.heappush(h, (2, 'b'))
heapq.heappush(h, (3, 'c'))
heapq.heappush(h, (4, 'c'))
print(h)
# [(1, 'a'), (1, 'ab'), (1, 'a'), (1, 'ac'), (2, 'b'), (3, 'c'), (4, 'c')]


print(heapq.heappop(h))
# (1, 'a')
print(h)
# [(1, 'a'), (1, 'ab'), (3, 'c'), (1, 'ac'), (2, 'b'), (4, 'c')]


print(heapq.heappop(h))
# (1, 'a')
print(h)
# [(1, 'ab'), (1, 'ac'), (3, 'c'), (4, 'c'), (2, 'b')]


print(heapq.heappop(h))
# (1, 'ab')
print(h)
# [(1, 'ac'), (2, 'b'), (3, 'c'), (4, 'c')]