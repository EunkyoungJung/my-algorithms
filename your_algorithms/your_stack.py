"""
stack
"""


class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self) -> bool:
        return False if self.items else True

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def size(self) -> int:
        return len(self.items)

    def peek(self):
        return self.items[-1] if self.items else None

    def __repr__(self):
        return repr(self.items)


def test_stack():
    s = Stack()
    assert(s.isEmpty() is True)
    for i in range(10):
        s.push(i)
    assert(s.size() == 10)
    assert(s.peek() == 9)
    assert(s.pop() == 9)
    assert(s.peek() == 8)
    assert(s.isEmpty() is False)


if __name__ == "__main__":
    test_stack()
    s = Stack()
    for i in range(10):
        s.push(i)
    print(s)