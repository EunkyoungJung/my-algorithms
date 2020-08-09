"""
node로 스택만들기
"""
class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


class Stack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return False if self.count else True

    def push(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def pop(self):
        if self.head and self.count > 0:
            node = self.head
            self.head = node.pointer
            self.count -= 1
            return node.value
        else:
            print("Stack is empty")

    def peek(self):
        return self.head.value if self.count > 0 and self.head else print("Stack is Empty")

    def size(self):
        return self.count

    def _print_list(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()


def test_node_stack():
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
    test_node_stack()
    s = Stack()
    for i in range(10):
        s.push(i)
    s._print_list()

