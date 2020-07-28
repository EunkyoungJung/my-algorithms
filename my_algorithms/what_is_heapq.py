"""
힙은 일반적으로 가장 작은(또는 가장 큰) 요소에 반복적으로 접근한느 프로그램에 유용
최소(또는 최대) 힙을 사용하면 가장 작은(또는 가장 큰) 요소를 처리하는 시간복잡도는 O(1)이고,
그 외의 조회, 추가, 수정을 처리하는 시간복잡도는 O(log n)이다.
"""

"""
heapq 모듈은 효율적으로 시퀀스를 힙으로 유지하면서
항목을 삽입하고 제거하는 함수를 제공한다.
heapq.heapify() 함수를 사용하면 O(n) 시간에 리스트를 힙으로 변화할 수 있음
"""

import heapq

# 리스트를 heap로 변환
print("EX1. 리스트를 heap으로 변환")
list1 = [4, 6, 8, 1]
print(type(list1))
print(list1)
print("-"*5)

heapq.heapify(list1)
print(type(list1))
print(list1)
print()
print()

# 항목을 힙에 삽입
# heapq.heappush(heap, item)
print("EX2. 항목을 힙에 삽입:")
h = []
print(h, type(h))
heapq.heappush(h, (1, 'food'))
print(h, type(h))
heapq.heappush(h, (2, 'have fun'))
print(h, type(h))
heapq.heappush(h, (2, 'have fun'))
print(h, type(h))
heapq.heappush(h, (3, 'work'))
print(h, type(h))
print()
print()


# 항목을 힙에서 가장작은 항목을 삭제
# heapq.heappop(heap)
print("EX3. 항목을 힙에서 삭제")
print("list1 :", list1)
print("heappop: ", heapq.heappop(list1))
print("list1: ", list1)

## list2를 heapq.heapfiy()를 하지 않았음!
## heapq.heappop()은 그냥 리스트의 첫번째 요소를 pop한당!
list2 = [4, 6, 8, 1]
print("list2: ", list2)
print("heappop: ", heapq.heappop(list2))
print("list2: ", list2)
print()
print()


# heapq.heapreplace(heap, item)
# 힙의 가장 작은 항목을 제거하고 반환한후!
# 새항목을 추가!
# heappush/heappop을 쓸 수 도 있지만
# 편하게! heappushpop()/heapreplace()를 써보세용~~


# heapq.merge(*iterables)
# 여러 개의 정렬된 반복 가능한 객체를 병합하여
# 하나의 정렬된 결과의 이터레이터를 반환
rlt = heapq.merge([1, 3, 5], [2, 4, 6])
print(rlt, type(rlt))
print([x for x in rlt])
"""
<generator object merge at 0x00000269D2C32348> <class 'generator'>
[1, 2, 3, 4, 5, 6]
"""


# heapq.nlargest(n, iterable[, key])와 heapq.nsmallest(n, iterable[, key])
# 데이터(반복 가능한 객체에 의해 정의된)에서 n개의 가장 큰 요소와 가장 작은 요소가 있는 리스트를 반환
print("heapq.nlargest(n, iterable[,key]")
list3 = [1,2,3,4,5,6,7,8,9]
print(heapq.nlargest(3,list3))
print("heapq.nsmallest(n, iterable[,key]")
print(heapq.nsmallest(3,list3))