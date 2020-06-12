from my_fifo_linked_list import LinkedListFifo
from my_node import Node


class LinkedListFifoYield(LinkedListFifo):
    def _printList(self):
        node = self.head
        while node:
            yield node.data
            node = node.pointer


def sumlls(l1, l2):
    lsum = LinkedListFifoYield()
    dig1 = l1.head
    dig2 = l2.head
    pointer = 0

    while dig1 and dig2:
        d1 = dig1.data
        d2 = dig2.data
        sum_d = d1 + d2 + pointer
        if sum_d > 9:
            pointer = sum_d//10
            lsum.addNode(sum_d % 10)

        else:
            lsum.addNode(sum_d)
            pointer = 0
            dig1 = dig1.pointer
            dig2 = dig2.pointer

    if dig1:
        sum_d = pointer + dig1.data
        if sum_d > 9:
            lsum.addNode(sum_d % 10)
        else:
            lsum.addNode(sum_d)
        dig1 = dig1.pointer

    if dig2:
        sum_d = pointer + dig2.data
        if sum_d > 9:
            lsum.addNode(sum_d % 10)
        else:
            lsum.addNode(sum_d)
        dig2 = dig2.pointer

    return lsum


if __name__ == "__main__":
    print("start")
    l1 = LinkedListFifoYield() # 2671
    l1.addNode(1)
    l1.addNode(7)
    l1.addNode(6)
    l1.addNode(2)

    l2 = LinkedListFifoYield() # 455
    l2.addNode(5)
    l2.addNode(5)
    l2.addNode(4)

    lsum = sumlls(l1, l2)
    l = list(lsum._printList())
    for i in reversed(l):
        print(i, end="")
    print()
    print("done")

