# Linked List (링크드 리스트)

"""
1. 링크드 리스트 구조
* 연결 리스트라고도 함
* 배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 궂
* 링크드 리스트는 떨어진 곳에 존재하는 데이터를 연결해서 관리하는 데이터 구조
* 본래 C언어에서는 주요한 데이터 구조이지만, 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원

2. 링크드 리스트의 장단점 (전통적인 C언어에서의 배열과 링크드 리스트)
* 장점:
    * 미리 데이터 공간을 미리 할당하지 않아도 됨
    * 참고: 배열은 미리데이터 공간을 할당해야 함
* 단점:
    * 연결을 위한 별도 데이터 공간이 필요하므로, 저장공간 효율이 높지 않음
    * 연결 정보를 찾는 시간이 필요하므로, 접근속도가 느림
    * 중간 데이터 삭제 시, 앞뒤 데이터의 연결을 재구성해야하는 부가적인 작업 필요
"""


# Node
# 노드(node) : 데이터 저장 단위 (데이터값, 포인터)로 구성
# 포인터(pointer) : 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간
class Node(object):
    def __init__(self, data,  prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


# Linked List
class SingleLinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node
        else:
            self.head = new_node

    def delete(self, data):
        node = self.head
        if not node:
            return None
        if self.head.data == data:
            self.head = self.head.next
            return data
        while node.next:
            if node.next.data == data:
                node.next = node.next.next
                return data
            node = node.next

    def desc(self):
        node = self.head
        items = []
        while node:
            items.append(node.data)
            node = node.next
        print(', '.join([str(x) for x in items]))

    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = self.head

    def insert_before(self, data, before_data):
        if not self.head:
            self.add(data)
            return True

        new_node = Node(data)
        node = self.tail
        while node.data != before_data:
            node = node.prev
            if node is None:
                return False
        new_node.next = node
        before_new = node.prev
        before_new.next = new_node
        return True

    def insert_after(self, data, after_data):
        if not self.head:
            self.add(data)
            return True

        new_node = Node(data)
        node = self.head
        while node.data != after_data:
            node = node.next
            if node is None:
                return False
        new_node.next = node
        new_node.prev = node.prev
        node.prev = new_node
        if new_node.next is None:
            self.tail = new_node
        return True

    def add(self, data):
        new_node = Node(data)
        if self.head and self.tail:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node
            new_node.prev = node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = self.head

    def delete(self, data):
        node = self.head
        if not node:
            return None
        if self.head.data == data:
            self.head, self.head.next.prev = self.head.next, None
            return data
        while node:
            if node.data == data:
                if node.next:
                    node.next.prev, node.prev.next = node.prev, node.next
                else:
                    self.tail = node.prev
                    self.tail.next = None
                return data
            node = node.next
        return None

    def desc(self):
        node = self.head
        items = []
        while node:
            items.append(node.data)
            node = node.next
        print(', '.join([str(x) for x in items]))
        # print(f"head: ${self.head.data}, tail: ${self.tail.data}")

    def search_node(self, data, reverse=False):
        node = self.head
        if not node:
            return None

        if reverse:
            node = self.tail
            while node:
                if node.data == data:
                    return node
                node = node.prev
            return None
        else:
            node = self.head
            while node:
                if node.data == data:
                    return node
                node = node.next
            return None


# FIFO Linked List
class LinkedListFIFO(object):
    def __init__(self):
        pass


if __name__ == "__main__":
    # ll = SingleLinkedList()
    # for i in range(1, 9):
    #     ll.add(i)
    # ll.desc()
    # ll.delete(8)
    # ll.desc()
    # print(ll.search_node(5).data)

    ll = DoubleLinkedList()
    for i in range(1, 9):
        ll.add(i)
    ll.desc()
    print(f"삭제 1: ${ll.delete(1)}")
    ll.desc()
    print(f"삭제 8: ${ll.delete(8)}")
    ll.desc()
    print(ll.search_node(5).data)
    print(ll.search_node(5, reverse=True).data)