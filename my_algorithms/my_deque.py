from my_algorithms.my_queue import Queue

"""
Deque(데크) : 스택 + 큐
양쪽 끝에서 항목의 조회, 삽입, 삭제가 가능
"""

class Deque(Queue):
    def enqueue_back(self, item):
        self.items.append(item)

    def dequeue_front(self):
        value = self.items.pop(0)
        if value is not None:
            return value
        else:
            print("Deque is empty.")

if __name__ == "__main__":
    deque = Deque()
    print(deque.isEmpty())

    for i in range(10):
        deque.enqueue(i)

    print(deque.size())
    print(deque.peek())
    print(deque.dequeue())
    print(deque.peek())
    print(deque.isEmpty())
    print(deque)
    print(deque.dequeue_front())
    print(deque.peek())
    print(deque)

