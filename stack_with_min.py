from my_stack import Stack


class NodeWithMin(object):
    def __init__(self, value=None, minimum=None):
        self.value = value
        self.minimum = minimum


class StackMin(Stack):
    def __init__(self):
        self.items = list()
        self.minimum = None

    def push(self, value):
        if self.isEmpty() or self.minimum > value:
            self.minimum = value
        self.items.append(NodeWithMin(value, self.minimum))

    def peek(self):
        return self.items[-1].value

    def peekMinimum(self):
        return self.items[-1].minimum

    def pop(self):
        item = self.items.pop()
        if item:
            if item.value == self.minimum:
                self.minimum = self.peekMinimum()
            return item.value
        else:
            print("Stack is empty.")

    def __repr__(self):
        aux = []
        for i in self.items:
            aux.append(i.value)
        return repr(aux)


if __name__ == "__main__":
    stack = StackMin()
    print(f"스택이 비었나요? {stack.isEmpty()}")
    print("스택에 숫자 10~1과 1~4를 추가합니다.")
    for i in range(10, 0, -1):
        stack.push(i)
    for i in range(1,5):
        stack.push(i)
    print(stack)

    print(f"스택 크기: {stack.size()}")
    print(f"peek: {stack.peek()}")
    print(f"peekMinimum: {stack.peekMinimum()}")
    print(f"pop: {stack.pop()}")
    print(f"peek: {stack.peek()}")
    print(f"peekMinimum: {stack.peekMinimum()}")
    print(f"스택이 비었나요? {stack.isEmpty()}")
    print(stack)