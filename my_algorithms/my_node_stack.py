"""
- 스택은 배열의 긑에서만 데이터를 접근하는 "선형 자료구조"
- LIFO(Last In First Out)
- 책상 위에 책이 쌓여있는 모습을 상상할 것
- 시간복잡도는 O(1)

스택의 동작들:
    * push : 스택 맨 끝(맨 위)에 항목을 삽입
    * pop : 스택 맨 끝 항목을 반환한느 동시에 제거
    * top/peak : 스택 맨 끝 항목을 조회
    * empty : 스택이 비어 있는 지 확인
    * size : 스택 크기를 확인

출처: [책] 파이썬 자료구조와 알고리즘, 한빛출판사 미아스타인 지음, 최길우 옮김
"""


## 나의 노드 스택 코드
class MyNode(object):
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.pointer = pointer


class MyStack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, data):
        self.head = MyNode(data, self.head)
        self.count += 1

    def pop(self):
        temp = self.head
        self.head = self.head.pointer
        self.count -= 1
        return temp.data

    def peek(self):
        return self.head.data

    def isEmpty(self):
        if self.head:
            return False
        else:
            return True

    def size(self):
        return self.count

s = MyStack()
print(s.isEmpty())
for i in range(10):
    s.push(i)
print(s.peek())
print(s.size())
print()
print()
print()



## 책의 노드 스택 코드
class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


class Stack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def push(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def pop(self):
        if self.count > 0 and self.head:
            node = self.head
            self.head = node.pointer
            self.count -= 1
            return node.value
        else:
            print("Stack is empty.")

    def peek(self):
        if self.count > 0 and self.head:
            return self.head.value
        else:
            print("Stack is empty.")

    def size(self):
        return self.count

    def _printList(self):
        node = self.head
        while node:
            print(node.value, end='')
            node = node.pointer
        print()

if __name__ == "__main__":
    stack = Stack()
    print(stack.isEmpty())
    for i in range(10):
        stack.push(i)
    stack._printList()
    print(stack.size())
    print(stack.pop())
    print(stack.peek())
    print(stack.isEmpty())
    stack._printList()






