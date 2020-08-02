"""
이진 트리
- 이진 트리를 구현하는 가장 단순한 방법은 리스트를 사용하는 것이다.
- 다음 코드는 루트 노드와 두 개의 빈 하위 리스트가 있는 리스트를 만든다.
- 루트 노드의 왼쪽에 서브 트리를 추가하려면 루트 토드의 리스트 두 번째 위치에 새 리스트를 삽입하면 된다.
- 하지만 이 코드는 리스트 중간에 노드를 삽입하거나 꺼낼 때 제한이 있으므로 매우 비효율적이다.
"""


def binary_tree_list(r):
    return [r, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_Right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_rootl_val(root, new_val):
    root[0] = new_val


def get_left_child(root):
    return root[2]


def main():
    r = binary_tree_list(3)
    insert_left(r, 4)
    insert_left(r, 5)
    insert_Right(r, 6)
    insert_Right(r, 7)
    print(get_root_val(r))
    print(get_left_child(r))
    print(get_left_child(r))


if __name__ == "__main__":
    main()
