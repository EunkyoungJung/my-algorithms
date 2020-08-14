"""
Linked List
- 값과 다음 노드에 대한 포인터(참조)가 포함된 노드로 이루어진 선형 리스트
- 마지막 노드는 nul값을 갖는다
- 또한, 연결 리스트로 스택(새 항목을 head에 추가)과 큐(새 항목을 tail에 추가)를 구현할 수 있음
"""
import doctest


class Node(object):
    def __init__(self, value, pointer=None):
        self.value = value
        self.pointer = pointer

    def getData(self):
        """
        :return:

        >>> n = Node(3)
        >>> n.getData()
        3
        """
        return self.value

    def getNext(self):
        """
        :return:

        >>> n1 = Node(1)
        >>> n2 = Node(2, n1)
        >>> assert(n2.getNext() == n1)
        """
        return self.pointer

    def setData(self, newData):
        """
        :param newData:
        :return:

        >>> n = Node(1)
        >>> n.setData(2)
        >>> assert(n.value == 2)
        """
        self.value = newData

    def setNext(self, newPointer):
        """
        :param newPointer:
        :return:

        >>> n1 = Node(1)
        >>> n2 = Node(2, n1)
        >>> n3 = Node(3)
        >>> n2.setNext(n3)
        >>> assert(n2.pointer == n3)
        """
        self.pointer = newPointer


def test_node():
    L = Node("a", Node("b", Node("c", Node("d"))))
    assert(L.pointer.pointer.value == "c")
    assert(L.getData() == "a")
    assert(L.getNext().getData() == "b")
    L.setData("aa")
    assert(L.getData() == "aa")
    L.setNext(Node("e"))
    assert(L.getNext().getData() == "e")


if __name__ == '__main__':
    test_node()
    doctest.testmod()
