"""
[3, 2, 5, 1, 7, 8, 2]
[0, 1, 2, 3, 4, 5, 6]
"""

items = [3, 2, 5, 1, 7, 8, 2]

for index, item in enumerate(items):
    print(index, ": ", item)
print()
print()
"""
       3
      (0)
   2       5
  (1)     (2)
 1   7   8   2
(3) (4) (5) (6)

부모: 왼쪽자식, 오른쪽 자식 => 규칙
0  : 1,2                => (X*2+1), (X*2+2)
1  : 3,4                => (X*2+1), (X*2+2)
2  : 5,6                => (X*2+1), (X*2+2)
"""

"""
max-heap 구하는 로직
1. 우선 전체리스트의 절반인 인덱스(템프인덱스라고 하겠음)에서 시작! (이유는 트리의 최하단 레벨의 원소중 인덱스가 가장 작은 아이부터 시작하는 것임!)
2. 템프인덱스를 1씩 줄이면서 하위에 자신보다 큰 원소가 있으면 바꾸고 계속해서 템프인덱스를 1씩 줄이는 행위를 함
"""

class MyHeapify(object):
    def __init__(self, data=None):
        self.data = data or []
        for i in range(len(data)//2, -1, -1):
            self.__max_heapify__(i)

    def __repr__(self):
        return repr(self.data)

    def __max_heapify__(self, index):
        # 왼쪽 자식
        if (index*2+1) < len(self.data):
            if self.data[index*2+1] > self.data[index]:
                self.data[index], self.data[index*2+1] = self.data[index*2+1], self.data[index]
        # 오른쪽 자식
        if (index*2+2) < len(self.data):
            if self.data[index*2+2] > self.data[index]:
                self.data[index], self.data[index*2+2] = self.data[index*2+2], self.data[index]

print(items)
t = MyHeapify(items)
print(t)
print()
print()
"""
출력 결과:
[3, 2, 5, 1, 7, 8, 2]
[8, 3, 7, 1, 2, 5, 2]
"""


class Heapify(object):
    def __init__(self, data=None):
        self.data = data or []
        for i in range(len(data)//2, -1, -1):
            self.__max_heapify__(i)

    def __repr__(self):
        return repr(self.data)

    def parent(self, i):
        if i & 1: # i가 0보다 큰 조건
            return i >> 1
            # 오른쪽 시프트 연산자. 변수의 값을 오른쪽으로 지정된 비트 수 만큼 이동
            # 1칸 오른쪽 이동한다는 의미는 나누기한다는 의미!
            # 나누기를 쓰지 않고 쉬프트 연사자를 쓰는 이유가 있음?! 더 빠름?!
        else: # i가 1보다 작은 조건?!?! 이 조건 왜있음?!?!
            return (i >> 1) - 1

    def left_child(self, i):
        return (i << 1) + 1

    def right_child(self, i):
        return (i << 1) + 2

    def __max_heapify__(self, i):
        largest = i  # 현재 노드
        left = self.left_child(i)
        right = self.right_child(i)
        n = len(self.data)

        # 왼쪽 자식
        largest = (left < n and self.data[left] > self.data[i]) and left or i
        # 오른쪽 자식
        largest = (right < n and self.data[right] > self.data[i]) and right or largest

        # 현재 노드가 자식들보다 크다면 skip, 자식이 크다면 swap
        if i is not largest:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            # print(self.data)
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
        while(i != 0) and item > self.data[self.parent(i)]:
            print(self.data)
            self.data[i] = self.data[self.parent(i)]
            i = self.parent(i)
        self.data[i] = item

def test_heapify():
    l1 = [3, 2, 5, 1, 7, 8, 2]
    h = Heapify(l1)
    assert(h.extract_max() == 8)
    print("Passed the test")

if __name__ == "__main__":
    test_heapify()



