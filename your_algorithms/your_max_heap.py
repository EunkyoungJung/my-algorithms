"""
Max Heap
- 완전이진트리
- 루트 노드의 인덱스가 0일때,
- 인덱스가 i인 노드의 왼쪽 자식: i*2 + 1
- 인덱스가 i인 노드의 오른쪽 자식: i*2 + 2
- 하위에서 부모노드보다 자식 노드가 큰 경우, 부모와 자식을 바꾸는 동작을 루트노드까지 반복한다.
"""


class Heapify(object):
    def __init__(self, data=None):
        self.data = data or []
        # len(data)//2는 트리의 마지막 depth의 첫번째 노드의 인덱스이다
        # 마지막 높이의 첫번째 노드부터 위쪽 부모노드로 올라가면서 __max_heapify__를 실행한다.
        for i in range(len(data)//2, -1, -1):
            self.__max_heapify__(i)

    def __repr__(self):
        return repr(self.data)

    def get_parent(self, i):
        if i & 1:
            return i >> 1 # 오른쪽으로 쉬프트 "%2"한 효과
        else:
            return (i >> 1) - 1

    def get_left_child(self, i):
        return (i << 1) + 1

    def get_right_child(self, i):
        return (i << 1) + 2

    def __max_heapify__(self, i):
        largest = i # 현재노드
        left = self.get_left_child(i)
        right = self.get_right_child(i)
        n = len(self.data)

        # 왼쪽 자식
        largest = (left < n and self.data[left] > self.data[i]) and left or i
        # 오른쪽 자식
        largest = (right < n and self.data[right] > self.data[largest]) and right or largest

        # 현재 노드가 자식들보다 크다면 skip, 자식이 크다면 swap
        if i is not largest:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.__max_heapify__(largest)

    def extract_max(self):
        n = len(self.data)
        max_element = self.data[0]

        # 첫 번째 노드에 마지막 노드를 삽입
        self.data[0] = self.data[n-1]
        self.data = self.data[:n-1]
        self.__max_heapify__(0)
        return max_element

    def insert(self, item):
        i = len(self.data)
        self.data.append(item)
        while (i != 0) and item > self.data[self.parent(i)]:
            print(self.data)
            self.data[i] = self.data[self.get_parent(i)]
            i = self.get_parent(i)
        self.data[i] = item


def test_heapify():
    l1 = [3, 2, 5, 1, 7, 8, 2]
    h = Heapify(l1)
    assert(h.extract_max() == 8)
    print("테스트 통과!")


if __name__ == "__main__""":
    test_heapify()