import heapq
from typing import List, Any


class PriorityQueue(object):
    _queue: List[Any]

    def __init__(self):
        self._queue = list()
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def __repr__(self):
        return repr(self._queue)


class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({0!r})".format(self.name)
        # {0!r}의 의미는 무엇일까?


def test_priority_queue():
    q = PriorityQueue()
    q.push(Item('test1'), 1)
    print(q)
    q.push(Item('test2'), 4)
    print(q)
    q.push(Item('test3'), 3)
    print(q)
    assert(str(q.pop()) == "Item('test2')")
    print("테스트 통과!")


if __name__ == "__main__":
    test_priority_queue()