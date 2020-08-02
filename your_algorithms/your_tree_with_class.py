"""
Tree
- 클래스로 트리를 구현해보자
"""


class SimpleTree(object):
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children
        if self.children is None:
            self.children = []

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


def main():
    st = SimpleTree('a', [
        SimpleTree('b', [
            SimpleTree('d'),
            SimpleTree('e'),
        ]),
        SimpleTree('c', [
            SimpleTree('h'),
            SimpleTree('g')
        ])
    ])
    print(st)


if __name__ == "__main__":
    main()