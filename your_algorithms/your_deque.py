"""
Deque (데크)
- 스택과 큐의 결합체
- 양쪽 끝에서 항목의 조회, 삽입, 삭제가 가능
"""


from your_queue import QueueWithSingleArray


class Deque(QueueWithSingleArray):
    """
    front [] back <- 데이터 삽입
    front [a,] back
    front [b, a] back
    front [c, b, a] back (<-queue의 peek)
    """
    def enqueue_back(self, item):
        self.items.append(item)

    def dequeue_front(self):
        if self.items:
            return self.items.pop(0)
        return print("Queue is empty")


def test_deque():
    d = Deque()
    assert(d.is_empty() is True)
    for i in range(10):
        d.enqueue(i)
    assert(d.is_empty() is False)
    assert(d.size() == 10)
    assert(d.peek() == 0)
    assert(d.dequeue_front() == 9)
    assert (d.size() == 9)
    d.enqueue_back(10)
    assert(d.peek() == 10)
    assert (d.size() == 10)


if __name__ == "__main__":
    test_deque()
    d = Deque()
    q = Deque()
    for i in range(10):
        d.enqueue_back(i)
        q.enqueue(i)

    print(f"끝으로 삽입하는 enqueue_back의 결과 d: {d}")
    print(f"앞으로 삽입하는 enqueue의 결과 q: {q}")