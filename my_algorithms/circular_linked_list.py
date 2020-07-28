from my_algorithms.my_fifo_linked_list import LinkedListFifo
from my_algorithms.my_node import Node


class CircularLinkedListFifo(LinkedListFifo):
    def _add(self, data):
        self.length += 1
        node = Node(data, self.head)
        if self.tail:
            self.tail.pointer = node
        self.tail = node


def isCircularll(ll):
    p1 = ll.head
    p2 = ll.head

    while p2:
        try:
            p1 = p1.pointer
            p2 = p2.pointer.pointer
        except:
            break

        if p1 == p2:
            return True
    return False


def test_isCircularll():
    ll = LinkedListFifo()
    for i in range(10):
        ll.addNode(i)
    assert(isCircularll(ll) is False)

    lcirc = CircularLinkedListFifo()
    for i in range(10):
        lcirc.addNode(i)
    assert(isCircularll(lcirc) is True)

    print("테스트 통과!")


if __name__ == "__main__":
    test_isCircularll()

