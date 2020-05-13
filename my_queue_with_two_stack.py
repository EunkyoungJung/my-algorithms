"""
파이썬 코드에서는 리스트의 insert() 메서드를 썻지만,
이는 모든 요소가 메모리에서 이동될 수 있으므로 비효율적이다(O(n))
두 개의 스택을 사용하면 효율적인 큐를 다음과 같이 작성할 수 있다
"""

class Queue(object):
    def __init__(self):
        self.in_stack = list()
        self.out_stack = list()

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
            print("Queue is empty!")

    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    def peek(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return repr(self.out_stack)
        else:
            print("Queue is empty!")

    def isEmpty(self):
        return not (bool(self.in_stack)) or bool(self.out_stack)


if __name__ == "__main__":
    queue = Queue()
    print(queue.isEmpty())
    for i in range(10):
        queue.enqueue(i)
    print(queue.size())
    print(queue.peek())
    print(queue.dequeue())
    print(queue.peek())
    print(queue.isEmpty())

