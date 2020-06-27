from my_fifo_linked_list import LinkedListFifo
from my_node import Node


class KthFromLast(LinkedListFifo):
    def find_kth_to_last(self, k):
        p1, p2 = self.head, self.head
        i = 0
        while p1:
            if i > k-1:
                try:
                    p2 = p2.pointer
                except AttributeError: # AttributeError는 왜 있는 것일까?
                    break
            p1 = p1.pointer
            i += 1
        return p2.data


if __name__ == "__main__":
    ll = KthFromLast()
    for i in range(1, 11):
        ll.addNode(i)
    print("연결 리스트:")
    ll._printList()
    k = 3
    k_from_list = ll.find_kth_to_last(k)
    print(f"연결 리스트의 끝에서 {k}번째 항목은 {k_from_list}입니다.")