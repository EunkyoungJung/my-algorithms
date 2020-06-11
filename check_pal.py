"""
연결리스트가 회문인지 확인해보는 코드
"""

from my_fifo_linked_list import LinkedListFifo
from my_node import Node

def isPal(l1):
    if l1 < 2:
        return True
    elif l1[0] != l1[-1]:
        return False
    return isPal(l1[1:-1])

def checkllPal(ll):
    node = ll.head
    l = list()
    while node:
        l.append(node.data)
        node = node.pointer

    return isPal(l)

def test_checkllPal():
    ll = LinkedListFifo()
    l1 = [1, 2, 3, 2, 1]
    for i in l1:
        ll.addNode(i)
    assert(checkllPal(ll) is True)

    ll.addNode(2)
    ll.addNode(3)
    assert(checkllPal(ll) is False)

    print("테스트 통과!")


if __name__ == "__main__":
    test_checkllPal()