"""
Queue
 * 항목이 들어온 순서대로 접근
 * FIFO(First In First Out)
 * 시간복잡도 O(1)

Queue의 기능:
 * enqueue : 큐 뒤쪽에 항목을 삽입
 * dequeue : 큐 앞쪽의 항목을 반환하고 제거
 * peek/front : 큐 앞쪽의 항목을 조회
 * empty : 큐가 비어 있는 지 확인
 * size : 큐의 크기를 확인
"""

# 내가 구현한 Queue
class MyQueue(object):
    def __init__(self):
        self.queue = list()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        item = self.queue.pop(0)
        return item

    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        if self.queue:
            return False
        else:
            return True

    def size(self):
        return len(self.queue)

q = MyQueue()
for i in range(10):
    q.enqueue(i)

print(q.size())
print(q.peek())
print(q.dequeue())
print(q.peek())
print(q.size())


# 책에서 제시한 Queue
class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Queue is empty.")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Queue is empty.")

    def __repr__(self):
        return repr(self.items)


if __name__ == "__main__":
    print()
    print()
    queue = Queue()
    print(queue.isEmpty())
    for i in range(10):
        queue.enqueue(i)
    print(queue.size())
    print(queue.peek())
    print(queue.dequeue())
    print(queue.peek())
    print(queue.isEmpty())
    print(queue)


