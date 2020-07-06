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


# 내가 작성한 스택
class MyStack(object):
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        if self.items:
            return False
        else:
            return True

    def size(self):
        return len(self.items)

s = MyStack()
print("my stack")
print(s.isEmpty())
for i in range(10):
    s.push(i)
print(s.size())
print(s.peek)
print(s.pop())
print(s.size())
print(s.isEmpty())
print()
print()
print()


# 책에서 제시한 스택
class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Stack is empty.")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Stack is empty.")

    def __repr__(self):
        return repr(self.items)

if __name__ == "__main__":
    stack = Stack()
    print("The Book's stack")
    print(stack.isEmpty())
    for i in range(10):
        stack.push(i)
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    print(stack.isEmpty())
    print(stack)