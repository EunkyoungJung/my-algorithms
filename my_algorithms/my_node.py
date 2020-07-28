"""
연결 리스트(linked list)
값과 다음 노드에 대한 포인터(참조)가 포함된 노드르로 이루어진 "선형 리스트"
마지막 노드는 Nnull값을 갖음
연결 리스트로 스택과 큐를 구현할 수 있음
"""


class Node(object):
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.pointer = pointer
        self.count = 1

    def getData(self):
        return self.data

    def getNext(self):
        return self.pointer

    def setData(self, new_data=None):
        self.data = new_data
        self.count += 1

    def setNext(self, new_pointer=None):
        self.pointer = new_pointer

    def __repr__(self):
        rlt = list()
        for i in range(self.count):
            if i == 0:
                rlt.append(self.data)
                next = self.pointer
            else:
                rlt.append(next.data)
                next = next.pointer
        return repr(rlt)


if __name__ == "__main__":
    L = Node("a", Node("b", Node("c", Node("d"))))
    assert (L.pointer.pointer.data == "c")

    print("print L: ", L)
    print("#"*10)
    print(L.getData())
    print(L.getNext().getData())
    L.setData("aa")
    print("print L: ", L)
    print("#" * 10)
    L.setNext(Node("e"))
    print("print L: ", L)
    print("#" * 10)
    print(L.getData())
    print(L.getNext().getData())


