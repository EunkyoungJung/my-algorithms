from my_stack import Stack

class SetOfStacks(Stack):
    def __init__(self, capacity=4):
        self.setofstacks = list()
        self.items = list()
        self.capacity = capacity

    def push(self, value):
        if self.size() >= self.capacity:
            self.setofstacks.append(self.items)
            self.items = list()
        self.items.append(value)

    def pop(self):
        value = self.items.pop()
        if self.isEmpty() and self.setofstacks:
            self.items = self.setofstacks.pop()
        return value

    def sizeStack(self):
        return len(self.setofstacks) * self.capacity + self.size()

    def __repr__(self):
        aux = list()
        for s in self.setofstacks:
            aux.extend(s)
        aux.extend(self.items)
        return repr(aux)


if __name__ == "__main__":
    capacity = 5
    stack = SetOfStacks(capacity)
    print(f"스택이 비었나요? {stack.isEmpty()}")
    print("스택에 숫자 0~9를 추가합니다..")
    for i in range(10):
        stack.push(i)
    print(stack)
    print(f"스택 크기: {stack.sizeStack()}")
    print(f"peek : {stack.peek()}")
    print(f"pop : {stack.pop()}")
    print(f"peek : {stack.peek()}")
    print(f"스택이 비었나요? {stack.isEmpty()}")
    print(stack)