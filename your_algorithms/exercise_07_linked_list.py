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

