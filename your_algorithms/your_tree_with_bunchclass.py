"""
트리와 같은 자료구조를 프로토타이핑할 때는,
생성자에서 임의의 속성을 지정하여 유연하게 구연하는 것이 좋다.
딕셔너리 클래스 특수화한 다음 클래스를 살펴보자.
"""


class BunchClass(dict):
    def __init__(self, *args, **kwargs):
        super(BunchClass, self).__init__(*args, **kwargs) # BunchClass에서 상속받은 __init__을 오버라이딩
        self.__dict__ = self


def main():
    # 1) 딕셔너리 특수화
    bc = BunchClass
    tree = bc(
        left=bc(left="Buffy", right="Angel"),
        right=bc(left="Willow", right="Xander")
    )
    print(tree)

    # 2) 일반 딕셔너리
    tree2 = dict(
        left=dict(left="Buffy", right="Angle"),
        right=dict(left="willow", right="Xander")
    )
    print(tree)


if __name__ == "__main__":
    main()