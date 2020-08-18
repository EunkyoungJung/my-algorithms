"""
7.7.1 스택을 이용해서 문제 풀기
"""

"""
스택은 데이터를 역순으로 정렬하거나 검색할 때 사용할 수  있다.
스택을 이용해서 문자열을 뒤집어 보자.
"""

import doctest


class Stack(object):
    def __init__(self):
        """
        >>> s = Stack()
        >>> assert(s.items == [])
        """
        self.items = []

    def peek(self):
        """
        :return:
        >>> s = Stack()
        >>> s.peek()
        'Stack is Empty'
        >>> s.items = [1, 2, 3]
        >>> s.peek()
        3
        """
        return self.items[-1] if self.items else "Stack is Empty"

    def size(self) -> int:
        """
        :return: stack의 사이즈 리턴
        >>> s = Stack()
        >>> s.items = [1, 2, 3, 4]
        >>> s.size()
        4
        """
        return len(self.items)

    def is_empty(self):
        """
        :return:
        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.items = [1, 2, 3]
        >>> s.is_empty()
        False
        """
        return False if self.items else True

    def pop(self):
        """
        :return:
        >>> s = Stack()
        >>> s.pop()
        Stack is empty
        >>> s.items = [1, 2, 3, 4]
        >>> s.pop()
        4
        """
        return self.items.pop() if self.items else print("Stack is empty")

    def push(self, item):
        """
        :param item:
        :return:
        >>> s = Stack()
        >>> s.push(1)
        >>> assert(s.items == [1])
        """
        self.items.append(item)

    def __repr__(self):
        """
        :return:
        >>> s = Stack()
        >>> s.items = [1, 2, 3, 4, 5]
        >>> s.__repr__()
        '[1, 2, 3, 4, 5]'
        """
        return repr(self.items)


def reverse_string_with_stack(line: str) -> str:
    """
    :param line: 입력 문장
    :return: 입력된 문장의 역순으로 된 문장
    >>> reverse_string_with_stack('abc')
    'cba'
    """
    s = Stack()

    for char in line:
        s.push(char)

    reversed_string = ""
    for i in range(s.size()):
        reversed_string += s.pop()

    return reversed_string


def balance_partner_string_with_stack(data: str) -> bool:
    """
    :param data: 괄호( '(', ')' )로 이루어진 문자열
    :return: 입력된 괄호가 균형이면 True 리턴 아니면 False 리턴
    >>> balance_partner_string_with_stack("((()))")
    True
    >>> balance_partner_string_with_stack('(()')
    False
    """
    s = Stack()
    balanced = True
    index = 0

    while index < len(data) and balanced:
        symbol = data[index]

        if symbol == "(":
            s.push(symbol)
        else:
            balanced = False if s.is_empty() else s.pop()

        index += 1

    return True if balanced and s.is_empty() else False


def convert_decimal_into_binary_with_stack(decimal_number: int) -> str:
    """
    :param decimal_number: 십진수 숫자
    :return: 십진수를 이진수로 변환한 문자열
    >>> convert_decimal_into_binary_with_stack(1)
    '1'
    >>> convert_decimal_into_binary_with_stack(5)
    '101'
    """
    s = Stack()
    str_aux = ""

    while decimal_number > 0:
        leftover = decimal_number % 2 # 나머지
        decimal_number = decimal_number // 2 #
        s.push(leftover)

    while not s.is_empty():
        str_aux += str(s.pop())

    return str_aux


"""
스택으로 최소값 찾기
"""


class NodeWithMin(object):
    def __init__(self, value=None, minimum=None):
        self.value = value
        self.minimum = minimum


class StackMin(Stack):
    def __init__(self):
        self.items = []
        self.minimum = None

    def push(self, value):
       if self.is_empty() or self.minimum > value: self.minimum = value
       self.items.append(NodeWithMin(value, self.minimum))

    def peek(self):
       return self.items[-1] if self.items else "Stack is empty."

    def peekMinimum(self):
        return self.items[-1].minium if self.items else "Stack is empty."

    def pop(self):
       item = self.items.pop()
       if item:
           if item.value == self.minimum: self.minimum = self.peekMinimum()
           return item.value
       else:
           print("Stack is empty.")

    def __repr__(self):
        aux = []
        for i in self.items:
            aux.append(i.value)
        return repr(aux)


class SetOfStacks(Stack):
    def __init__(self, capacity=4):
        self.setofstacks = []
        self.items = []
        self.capacity = capacity

    def push(self, value):
        if self.size() >= self.capacity:
            self.setofstacks.append(self.items)
            self.items = []
        self.items.append(value)

    def pop(self):
        value = self.items.pop()
        if self.is_empty() and self.setofstacks:
            self.items = self.setofstacks.pop()
        return value

    def sizeStack(self):
        return len(self.setofstacks) * self.capacity + self.size()

    def __repr__(self):
        aux = []
        for s in self.setofstacks:
            aux.extend(s)
        aux.extend(self.items)
        return repr(aux)


def test_set_of_stacks():
    capacity = 5
    stack = SetOfStacks(capacity)
    assert(stack.is_empty() is True)
    for i in range(10):
        stack.push(i)
    assert(stack.sizeStack() == 10)
    assert(stack.peek() == 9)
    assert(stack.pop() == 9)
    assert(stack.peek() == 8)
    assert(stack.is_empty() is False)


print("hello")
test_set_of_stacks()
doctest.testmod()
reverse_string_with_stack("abc")
convert_decimal_into_binary_with_stack(9)


