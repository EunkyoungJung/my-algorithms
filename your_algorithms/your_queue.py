"""
Queue
- 스택과는 다르게 아이템이 들어온 순서대로 접근 가능함
- 먼저 들어온 데이터가 먼저 나가는 선입선출(FIFO: First in, First out) 구조
- 배열의 인덱스 접근이 제한 됨
- 시간 복잡도 O(1)

enqueue
dequeue
peek/front
empty
size
"""


class Queue(object):
    """
    queue 클래스 구현
    """

    def __init__(self):
        self.items = []
        self.count = 0

    def enqueue(self, item):
        self.items.append(item)
        self.count += 1

    def dequeue(self):
        self.count -= 1
        return self.items.pop(0)

    def peek(self):
        return self.items[0] if self.items else print("Queue is empty.")

    def is_empty(self):
        if self.items and self.count > 0:
            return False
        return True

    def size(self):
        return len(self.items)

    def __repr__(self):
        return repr(self.items)


def test_queue():
    q = Queue()
    assert(q.is_empty() is True)
    for i in range(10):
        q.enqueue(i)
    assert(q.size() == 10)
    assert(q.peek() == 0)
    assert(q.dequeue() == 0)
    assert(q.size() == 9)
    assert(q.peek() == 1)


if __name__ == "__main__":
    test_queue()
    q = Queue()
    for i in range(10):
        q.enqueue(i)
    print(q)
