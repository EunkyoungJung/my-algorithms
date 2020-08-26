"""
Linked List
"""

import doctest


class Node(object):
    """
    링크드 리스트의 Node
    """
    def __init__(self, value, pointer=None):
        """
        >>> n = Node(1)
        >>> assert(n.value == 1)
        >>> assert(n.pointer is None)
        """
        self.value = value
        self.pointer = pointer

    def get_data(self):
        """
        >>> n = Node(1)
        >>> n.get_data()
        1
        """
        return self.value

    def get_next(self):
        """
        >>> n = Node(1, Node(2))
        >>> assert(n.get_next().value == 2)
        """
        return self.pointer

    def set_value(self, new_value):
        """
        >>> n = Node(1)
        >>> n.set_value(2)
        >>> assert(n.value == 2)
        """
        self.value = new_value

    def set_next(self, new_pointer):
        """
        >>> n1 = Node(1)
        >>> n2 = Node(2)
        >>> n1.set_next(n2)
        >>> assert(n1.pointer == n2)
        """
        self.pointer = new_pointer


class LinkedListFIFO(object):
    """
    FIFO Linked List
    """
    def __init__(self):
        """
        >>> llfifo = LinkedListFIFO()
        >>> assert(llfifo.head is None)
        >>> assert(llfifo.length == 0)
        >>> assert(llfifo.tail is None)
        """
        self.head = None
        # 링크드 리스트는 전체 개수를 알려면 처음부터 끝까지 타고타고 가야해서, 개수를 기록하는 변수를 두면 좋다
        self.length = 0
        self.tail = None

    def _print_list(self):
        """
        >>> llfifo = LinkedListFIFO()
        >>> llfifo.head = Node(1, Node(2, Node(3)))
        >>> llfifo._print_list()
        1 2 3
        """
        node = self.head
        while node:
            print(f"{node.value}", end=" ")
            node = node.pointer
        print()

    def _add_into_empty_list(self, value):
        """
        >>> llfifo = LinkedListFIFO()
        >>> llfifo._add_into_empty_list(1)
        >>> assert(llfifo.length == 1)
        >>> assert(llfifo.head.value == 1)
        >>> assert(llfifo.tail.value == 1)
        """
        new_node = Node(value)
        self.length += 1
        self.head = new_node
        self.tail = new_node

    def _add_into_not_empty_list(self, value):
        new_node = Node(value)
        self.length += 1
        if self.tail:
            self.tail.pointer = new_node
        self.tail = new_node

    def add_node(self, value):
        new_node = Node(value)
        self.length += 1
        if not self.head:
            self._add_into_empty_list(new_node)
        else:
            self._add_into_not_empty_list(new_node)

    def _find_by_index(self, index):
        prev_node = self.head
        node = self.head
        idx = 0
        while node and idx < index:
            prev_node = node
            node = node.pointer
            idx += 1
        return idx, prev_node, node
        # idx가 index과 동일한지 체크하지 않음에 유의

    def _find_by_value(self, value):
        prev_node = self.head
        node = self.head
        idx = 0
        while node:
            if node.value == value:
                return node.value, prev_node, node
            prev_node = node
            node = node.pointer

    def _delete_all(self):
        self.length = 0
        self.head = None
        self.tail = None
        print("Now the list is empty.")

    def delete_node_by_index(self, index):
        if not self.head or not self.head.pointer:
            self._delete_all()
        else: # 리스트의 원소가 2개 이상부터는 else를 실행
            idx, prev_node, node = self._find_by_index(index)
            if idx == index and node:
                self.length -= 1
                # index가 첫번째 원소를 가리키는 경우
                if i == 0 or not prev_node:
                    self.head = node.pointer
                    self.tail = node.pointer # 이건 왜 해줌?!
                else:
                    prev_node.pointer = node.pointer
            else:
                print(f"The item of index({index}) is not existed.")

    def delete_node_by_value(self, value):
        prev_node = self.head
        node = self.head
        node_value = node.value
        while node and node_value != value:
            prev_node = node
            node = node.pointer
        return node.value, prev_node, node



