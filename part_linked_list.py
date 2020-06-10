from my_fifo_linked_list import LinkedListFifo
from my_node import Node


def partList(ll, n):
    more = LinkedListFifo()
    less = LinkedListFifo()

    node = ll.head

    while node:
        item = node.data
        if item < n:
            less.addNode(node)
        elif item > n:
            more.addNode(node)
        node = node.pointer

    less.addNode(n)
    nodemore = more.head

    while nodemore:
        less.addNode(nodemore.value)
        nodemore = nodemore.pointer

    return less


if __name__ == "__main__":
    ll = LinkedListFifo()
    l = [6, 7, 3, 4, 9, 5, 1, 2, 8]
    for i in l:
        ll.addNode(i)

    print("분할 전:", end=" ")
    ll._printList()
    newll = partList(ll, 6)
    newll._printList()