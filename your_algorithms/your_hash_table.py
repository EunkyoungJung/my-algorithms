"""
Hash Table
- key를 value에 연결하여, 하나의 키가 0 또는 1개의 값과 연관된다
- 각 키는 해시 함수를 계산할 수 있어야 한다
- 해시 테이블은 해시 버킷의 배열로 구성된다
- 예를 들어, 해시 값이 42이고 5개의 버킷이 있는 경우 나머지 여산을 사용하여 버킷 2(42 mod 5)에 매핑힌다

Hash Collision
- 두 개의 키가 동일한 버킷에 해시될 때 충돌이 발생한다
- 충돌을 처리하는 한 가지 방법은, 각 버킷에 대해 키-값 쌍의 연결 리스트를 저장하는 것이다
- 해시 테이블의 조회, 삽입, 삭제의 시간복잡도는 O(1)이다.
- 최악의 경우 각 키가 동일한 버킷으로 해시된다면(해시 충돌이 발생한다면), 각 작업의 시간복잡도는 O(n)이다.
"""


from your_linked_list_FIFO import LinkedListFIFO


class HashTableLL():
    def __init__(self, size):
        self.size = size
        self.slots = []
        self._createHashTable()

    def _createHashTable(self):
        for i in range(self.size):
            self.slots.append(LinkedListFIFO())

    def _find(self, item):
        return item % self.size

    def _add(self, item):
        index = self._find(item)
        self.slots[index].addNode(item)

    def _delete(self, item):
        index = self._find(item)
        self.slots[index].deleteNodeByValue(item)

    def _print(self):
        for i in range(self.size):
            print(f"슬롯(slot) {i}")
            self.slots[i]._printList()


def test_hash_table():
    H1 = HashTableLL(3)
    for i in range(0, 20):
        H1._add(i)
    H1._print()
    print("항목 0, 1, 2를 삭제합니다.")
    H1._delete(0)
    H1._delete(1)
    H1._delete(2)
    H1._print()


if __name__ == "__main__":
    test_hash_table()
