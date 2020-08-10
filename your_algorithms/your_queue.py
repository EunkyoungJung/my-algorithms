"""
Queue
- 스택과는 다르게 아이템이 들어온 순서대로 접근 가능함
- 먼저 들어온 데이터가 먼저 나가는 선입선출(FIFO: First in, First out) 구조
- 배열의 인덱스 접근이 제한 됨
- 시간 복잡도 O(1)
- 너비 우선 탐색(BFS)에서 사용됨

enqueue
dequeue
peek/front
empty
size
"""


class QueueWithSingleArray(object):
    """
    queue 클래스 구현
    """

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # 배열의 마지막 [-1]은 항상 가장 오래된 원소가 되도록
        # 배열의 0번 인덱스에다가 새로운 원소를 넣어줌
        self.items.insert(0, item)

    def dequeue(self):
        if self.items:
            return self.items.pop()
        return print("Queue is empty")

    def peek(self):
        return self.items[-1] if self.items else print("Queue is empty.")

    def is_empty(self):
        return False if self.items else True

    def size(self):
        return len(self.items)

    def __repr__(self):
        return repr(self.items)


class QueueWithTwoArrays(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def enqueue(self, item):
        return self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack.pop()
        else:
            print("Queue is empty.")

    def is_empty(self):
        return False if self.in_stack or self.out_stack else True

    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    def peek(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack[-1]
        else:
            print("Queue is empty.")

    def __repr__(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return repr(self.out_stack)
        else:
            print("Queue is empty.")


class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return False if self.count > 0 and self.head else True

    def enqueue(self, item):
        new_item = Node(item)
        if not self.head:
            self.head = new_item
            self.tail = new_item
        else:
            if self.tail:
                self.tail.pointer = new_item
            self.tail = new_item
        self.count += 1

    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            self.count -= 1
            return value
        else:
            print("Queue is empty.")

    def size(self):
        return self.count

    def peek(self):
        return self.head.value

    def print(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()


def test_queue_with_single_array():
    q = QueueWithSingleArray()
    assert(q.is_empty() is True)
    for i in range(10):
        q.enqueue(i)
    assert(q.size() == 10)
    assert(q.peek() == 0)
    assert(q.dequeue() == 0)
    assert(q.size() == 9)
    assert(q.peek() == 1)


def test_queue_with_two_arrays():
    q = QueueWithTwoArrays()
    assert(q.is_empty() is True)
    for i in range(10):
        q.enqueue(i)
    assert(q.size() == 10)
    assert(q.peek() == 0)
    assert(q.dequeue() == 0)
    assert(q.size() == 9)
    assert(q.peek() == 1)


def test_linked_queue():
    q = LinkedQueue()
    assert(q.is_empty() is True)
    for i in range(10):
        q.enqueue(i)
    assert(q.size() == 10)
    assert(q.peek() == 0)
    assert(q.dequeue() == 0)
    assert(q.size() == 9)
    assert(q.peek() == 1)


if __name__ == "__main__":
    test_queue_with_single_array()
    test_queue_with_two_arrays()
    test_linked_queue()

    q1 = QueueWithSingleArray()
    q2 = QueueWithTwoArrays()
    q3 = LinkedQueue()
    for i in range(10):
        q1.enqueue(i)
        q2.enqueue(i)
        q3.enqueue(i)
    print(q1)
    print(q2)
    q3.print()
