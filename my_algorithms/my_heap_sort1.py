"""
힘 정렬 (heap sort)
- 정렬되지 않은 영역이 힙이라는 점을 제외하면 선택 정렬과 비슷
- 힙 정렬은 가장 큰(또는 작은) 요소를 n번 찾을 때, 로그 선형의 시간복잡도를 가짐
- 힙에서 루트가 아닌 다른 모든 노드는 부모 노드의 값보다 작은(또는 큰) 값을 갖음
- 가장 작은(또는 큰) 요소는 루트에 저장됨
- 루트의 하위 트리에는 루트보다 더 큰(또는 작은) 값들이 포함됨
- 힙의 삽입 시간복잡도는 O(1)임
- 힙 순서를 확인하는 데 드는 시간복잡도는 O(log n)이고,
- 힙을 순회하는 시간복잡도는 O(n)
- 힙 정렬은 파이썬의 내장 heapq모듈을 사용하여 모든 값을 힙에 push한 다음
- 한번에 하나씩 가장 작은 값을 꺼내어 구현할 수 있음
"""

import heapq


def heap_sort1(seq):
    h = []
    for value in seq:
        heapq.heappush(h, value)
    return [heapq.pop(h) for _ in range(len(h))]


def test_heap_sort1():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    print(f"heap_sort1(seq): {heap_sort1(seq)}")
    assert(heap_sort1(seq) == sorted(seq))
    print("테스트 통과!")


if __name__ == "__main__":
    test_heap_sort1()