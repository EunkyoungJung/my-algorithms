"""
이중 연결 리스트 (Doubly Linked List)
포인터가 두 개가 있어
하나는 앞 노드를,
하나는 뒤 노드를 가리킨다.
"""

from my_fifo_linked_list import LinkedListFifo


class DNode(object):
    def __init__(self, data=None, pointer=None, previous=None):
        self.data = data
        self.pointer = pointer
        self.previous = previous


class DLinkedList(LinkedListFifo):
    def printListInverse(self): # tail부터 거꾸로 출력
        node = self.tail
        while node:
            print(node.data, end=" ")
            try:
                node = node.previous
            except AttributeError:
                break
        print()

    def _add(self, data): # tail에 노드 추가
        self.length += 1
        node = DNode(data)
        if self.tail:
            self.tail.pointer = node
            node.previous = self.tail
        self.tail = node

    def _delete(self, node): # tail의 노드 제거
        self.length -= 1
        node.previous.pointer = node.pointer
        if not node.pointer:
            self.tail = node.previous

    def _find(self, index): # linkedfifo에도 _find가 있는데 왜?! 요거 없어도 잘됨
        node = self.head
        i = 0
        while node and i < index:
            node = node.pointer
            i += 1
        return node, i

    def deleteNode(self, index): # linkedfifo에도 _find가 있는데 왜?! 요거 없어도 잘됨
        if not self.head or not self.head.pointer:
            self._deleteFirst()
        else:
            node, i = self._find(index)
            if i == index:
                self._delete(node)
            else:
                print(f"인덱스 {index}에 해당한느 노드가 없습니다.")


if __name__ == "__main__":
    from collections import Counter

    ll = DLinkedList()
    for i in range(1, 5):
        ll.addNode(i)
    print("연결 리스트 출력: ")
    ll._printList()
    print("연결 리스트 반대로 출력: ")
    ll.printListInverse()
    print("값이 15인 노드 추가 후, 연결 리스트 출력: ")
    ll._add(15)
    ll._printList()
    print("모든 노드 모두 삭제 후, 연결 리스트 출력: ")
    for i in range(ll.length-1, -1, -1):
        ll.deleteNode(i)
    ll._printList()
