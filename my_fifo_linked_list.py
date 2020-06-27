from my_node import Node

class LinkedListFifo(object):
    def __init__(self):
        self.head = None # 헤드(머리)
        self.length = 0
        self.tail = None # 테일(꼬리)

    # 헤드부터 각 노드의 값을 출력한다
    def _printList(self):
        node = self.head
        while node:
            print(node.data, end=" ")
            node = node.pointer
        print()

    # 첫 번째 위치에 노드를 추가한다 (노드가 0개)
    def _addFirst(self, data):
        self.length = 1
        node = Node(data)
        self.head = node
        self.tail = node

    # 첫 번째 위치의 노드를 삭제한다 (노드가 1개)
    def _deleteFirst(self):
        self.length = 0
        self.head = None
        self.tail = None
        print("연결리스트가 비었습니다.")

    # 새 노드를 추가한다. 테일이 있다면, 테일의 다음 노드는
    # 새 노드를 가리키고, 테일은 새 노드를 가리킨다
    def _add(self, data):
        self.length += 1
        node = Node(data)
        if self.tail:
            self.tail.pointer = node
        self.tail = node

    # 새 노드를 추가한다
    # 경우에 따라서 _addFirst 메소드와 _add 메소드를 사용
    def addNode(self, data):
        if not self.head:
            self._addFirst(data)
        else:
            self._add(data)

    # 인덱스로 노드를 찾는다
    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i

    # 값으로 노드를 찾는다
    def _find_by_value(self, data):
        prev = None
        node = self.head
        found = False
        while node:
            if node.data == data:
                found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found

    # 인덱스에 해당하는 노드를 삭제한다
    # 경우에 따라서 _deleteFirst 메소드와 _delete 메소드를 사용
    def deleteNode(self, index):
        if not self.head or not self.head.pointer:
            self._deleteFirst()
        else:
            node, prev, i = self._find(index)
            if i == index and node:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = node.pointer
                    self.tail = node.pointer
                else:
                    prev.pointer = node.pointer
            else:
                print(f"인덱스 {index}에 해당하는 노드가 없습니다.")

    # 값에 해당하는 노드를 삭제한다
    def deleteNodeByValue(self, data):
        if not self.head or not self.head.pointer:
            self._deleteFirst()
        else:
            node, prev, i = self._find_by_value(data)
            if node and node.data == data:
                self.length -= 1
                if i == 0 and not prev:
                    self.head = node.pointer
                    self.tail = node.pointer
                else:
                    prev.pointer = node.pointer
            else:
                print(f"값 {data}에 해당하는 노드가 없습니다.")


if __name__ == "__main__":
    ll = LinkedListFifo()
    for i in range(1, 5):
        ll.addNode(i)
    ll._printList()
    ll.deleteNode(2)
    ll._printList()
    ll.addNode(15)
    ll._printList()

