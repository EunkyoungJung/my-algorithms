from my_node import Node


class LinkedListLifo(object):
    def __init__(self):
        self.head = None
        self.length = 0

    # 헤드부터 각 노드의 값을 출력한다
    def _printList(self):
        node = self.head
        while node:
            print(node.data, end=" ")
            node = node.pointer
        print()

    # 이전 노드(prev)를 기반으로 노드(node)를 삭제한다
    def _delete(self, prev, node):
        self.length -= 1
        if not prev:
            self.head = node.pointer
        else:
            prev.pointer = node.pointer

    # 새 노드를 추가한다. 다음 노드로 헤드를 가리키고,
    # 헤드는 새 노드를 가리킨다
    def _add(self, data):
        self.length += 1
        self.head = Node(data, self.head)

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
        while node and not found:
            if node.data == data:
                found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found

    # 인덱스에 해당하는 노드를 찾아서 삭제한다
    def deleteNode(self, index):
        node, prev, i = self._find(index)
        if index == i:
            self._delete(prev, node)
        else:
            print(f"인덱스 {index}에 해당하는 노드가 없습니다.")

    # 값에 해당하는 노드를 찾아서 삭제한다.
    def deleteNodeByValue(self, data):
        node, prev, found = self._find_by_value(data)
        if found:
            self._delete(prev, node)
        else:
            print(f"값 {data}에 해당하는 노드가 없습니다.")
            

if __name__ == "__main__":
    print("1. ll생성")
    ll = LinkedListLifo()
    ll._printList()
    print("2. ll에 데이터 추가")
    for i in range(1, 5):
        ll._add(i)
    ll._printList()
    print("3. ll의 2번 노드 삭제")
    ll.deleteNode(2)
    ll._printList()
    print("4. ll의 값 3 삭제")
    ll.deleteNodeByValue(3)
    ll._printList()
    print("5. ll의 값 15 추가")
    ll._add(15)
    ll._printList()
    print("6. ll의 값 전체 삭제")
    for i in range(ll.length-1, -1, -1):
        ll.deleteNode(i)
    ll._printList()