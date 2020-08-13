"""
Priority Queue
"""

import heapq


class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Item({self.name})"


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0
    
    def push(self, item, priority):
        # 디폴트 heap은 min heap이다.
        # mean heap을 이용해서 priority 큐를 만들려고하니
        # priority가 크면 클 수록 작은 숫자가 되어야 해서
        # "-priority"를 해준다
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    
    def pop(self):
        # self._queue에는 [(우선순위, 인덱스번호, 아이템), (우선순위, 인덱스번호, 아이템), ...]의 리스트이다
        # 그래서 아이테을 꺼내려면 끝에 [-1]을 해준다
        return heapq.heappop(self._queue)[-1]


def test_priority_queue():
    q = PriorityQueue()
    q.push(Item('test1'), 1)
    q.push(Item('test4'), 4)
    q.push(Item('test2'), 2)
    q.push(Item('test3'), 3)
    assert(str(q.pop()) == "Item(test4)")


if __name__ == "__main__":
    test_priority_queue()
