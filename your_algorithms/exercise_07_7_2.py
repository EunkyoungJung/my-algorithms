"""
Dequeue로 문제 풀기
"""


import doctest
import string
import collections


class Queue(object):
    """
    Queue 구현하기: 선입선출
    dequeue는 -1에서
    enqueue는 0에 다가 insert
    """
    def __init__(self):
        """
        >>> q = Queue()
        >>> assert(q.items == [])
        """
        self.items = []

    def enqueue(self, item):
        """
        :param item: queue에 삽입할 원소
        :return:
        >>> q = Queue()
        >>> q.enqueue(1)
        >>> assert(q.items == [1])
        >>> q.enqueue(2)
        >>> assert(q.items == [2, 1])
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        :return: 가장 오래된 원소 리턴
        >>> q = Queue()
        >>> q.items = [2, 1]
        >>> q.dequeue()
        1
        >>> q.dequeue()
        2
        """
        return self.items.pop() if self.items else print("Queue is empty.")

    def is_empty(self) -> bool:
        """
        :return: Queue가 비었으면 True 리턴
        >>> q = Queue()
        >>> q.items = []
        >>> q.is_empty()
        True
        >>> q.items = [1]
        >>> q.is_empty()
        False
        """
        return False if self.items else True

    def size(self) -> int:
        """
        :return: Queue의 self.items의 사이즈 리턴
        >>> q = Queue()
        >>> q.items = []
        >>> q.size()
        0
        >>> q.items = [1, 2, 3]
        >>> q.size()
        3
        """
        return len(self.items)

    def __repr__(self):
        """
        :return:
        >>> q = Queue()
        >>> q.items = []
        >>> q.__repr__()
        '[]'
        >>> q.items = [1, 2, 3]
        >>> q.__repr__()
        '[1, 2, 3]'
        """
        return repr(self.items)


class Deque(Queue):
    """
    Deque구현하기
    - 스택 + 큐
    - 양쪽 끝에서 조회/삽입/삭제 가능
    """
    def enqueue_back(self, item) -> None:
        """
        self.items의 -1에 아이템 삽입
        :param item: deque에 삽입하고자 하는 아이템
        :return: None
        >>> q = Deque()
        >>> q.items = []
        >>> q.enqueue_back(1)
        >>> assert(q.items == [1])
        >>> q.enqueue_back(2)
        >>> assert(q.items == [1, 2])
        """
        self.items.append(item)

    def dequeue_front(self):
        """
        queue의 0번 인덱스에서 아이템 pop
        :return: self.items이 있다면 0번째 인덱스 원소 리턴, self.items가 없다면 문장 출력
        >>> q = Deque()
        >>> q.items = [1, 2, 3]
        >>> q.dequeue_front()
        1
        >>> q.dequeue_front()
        2
        """
        return self.items.pop(0) if self.items else print("Queue is empty.")


def palindrome_checker_with_deque(line, STRIP = (string.whitespace + string.punctuation + "/"'')):
    d1 = Deque()
    d2 = collections.deque()

    for char in line.lower():
        if char not in STRIP:
            d2.append(char)
            d1.enqueue(char)

    # 내가 작성한 queue를 이용해서 체크
    eq1 = True
    while d1.size() > 1 and eq1:
        if d1.dequeue_front() != d1.dequeue():
            eq1 = False

    # collections.deque를 이용해서 체크
    eq2 = True
    while len(d2) > 1 and eq2:
        if d2.pop() != d2.popleft():
            eq2 = False

    return eq1 == eq2


if __name__ == "__main__":
    doctest.testmod()
    line1 = "Madam Im Adam"
    line2 = "Buffy is a Slayer"
    print(palindrome_checker_with_deque(line1))
    print(palindrome_checker_with_deque(line2))