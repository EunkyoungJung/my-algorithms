"""
Dequeue로 문제 풀기
"""


import doctest
import string
import collections


class Queue(object):
    """
    Queue 구현하기: 선입선출
    dequeue는 -1에서
    enqueue는 0에 다가 insert
    """
    def __init__(self):
        """
        >>> q = Queue()
        >>> assert(q.items == [])
        """
        self.items = []

    def enqueue(self, item):
        """
        :param item: queue에 삽입할 원소
        :return:
        >>> q = Queue()
        >>> q.enqueue(1)
        >>> assert(q.items == [1])
        >>> q.enqueue(2)
        >>> assert(q.items == [2, 1])
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        :return: 가장 오래된 원소 리턴
        >>> q = Queue()
        >>> q.items = [2, 1]
        >>> q.dequeue()
        1
        >>> q.dequeue()
        2
        """
        return self.items.pop() if self.items else print("Queue is empty.")

    def is_empty(self) -> bool:
        """
        :return: Queue가 비었으면 True 리턴
        >>> q = Queue()
        >>> q.items = []
        >>> q.is_empty()
        True
        >>> q.items = [1]
        >>> q.is_empty()
        False
        """
        return False if self.items else True

    def size(self) -> int:
        """
        :return: Queue의 self.items의 사이즈 리턴
        >>> q = Queue()
        >>> q.items = []
        >>> q.size()
        0
        >>> q.items = [1, 2, 3]
        >>> q.size()
        3
        """
        return len(self.items)

    def __repr__(self):
        """
        :return:
        >>> q = Queue()
        >>> q.items = []
        >>> q.__repr__()
        '[]'
        >>> q.items = [1, 2, 3]
        >>> q.__repr__()
        '[1, 2, 3]'
        """
        return repr(self.items)


class Deque(Queue):
    """
    Deque구현하기
    - 스택 + 큐
    - 양쪽 끝에서 조회/삽입/삭제 가능
    """
    def enqueue_back(self, item) -> None:
        """
        self.items의 -1에 아이템 삽입
        :param item: deque에 삽입하고자 하는 아이템
        :return: None
        >>> q = Deque()
        >>> q.items = []
        >>> q.enqueue_back(1)
        >>> assert(q.items == [1])
        >>> q.enqueue_back(2)
        >>> assert(q.items == [1, 2])
        """
        self.items.append(item)

    def dequeue_front(self):
        """
        queue의 0번 인덱스에서 아이템 pop
        :return: self.items이 있다면 0번째 인덱스 원소 리턴, self.items가 없다면 문장 출력
        >>> q = Deque()
        >>> q.items = [1, 2, 3]
        >>> q.dequeue_front()
        1
        >>> q.dequeue_front()
        2
        """
        return self.items.pop(0) if self.items else print("Queue is empty.")


def palindrome_checker_with_deque(line, STRIP = (string.whitespace + string.punctuation + "/"'')):
    d1 = Deque()
    d2 = collections.deque()

    for char in line.lower():
        if char not in STRIP:
            d2.append(char)
            d1.enqueue(char)

    # 내가 작성한 queue를 이용해서 체크
    eq1 = True
    while d1.size() > 1 and eq1:
        if d1.dequeue_front() != d1.dequeue():
            eq1 = False

    # collections.deque를 이용해서 체크
    eq2 = True
    while len(d2) > 1 and eq2:
        if d2.pop() != d2.popleft():
            eq2 = False

    return eq1 == eq2


class Animal(object):
    def __init__(self, animalName=None, animalKind=None, pointer=None):
        """
        :param animalName:
        :param animalKind:
        :param pointer:
        >>> a = Animal('Yoda', 'cat')
        >>> assert(a.animalName == 'Yoda')
        >>> assert(a.animalKind == 'cat')
        >>> assert(a.pointer is None)
        """
        self.animalName = animalName
        self.animalKind = animalKind
        self.pointer = pointer
        self.timestamp = 0 # Animal 인스턴스 생성 당시의 AnimalShelter 인스턴스의 animalNumber 숫자


class AnimalShelter(object):
    def __init__(self):
        """
        >>> s = AnimalShelter()
        >>> assert(s.headCat is None)
        >>> assert(s.headDog is None)
        >>> assert(s.tailCat is None)
        >>> assert(s.tailDog is None)
        >>> assert(s.animalNumber == 0)
        """
        self.headCat = None
        self.headDog = None
        self.tailCat = None
        self.tailDog = None
        self.animalNumber = 0

    def enqueue(self, animalName: string, animalKind: string) -> None:
        """
        :param animalName: string
        :param animalKind: string
        :return: None
        >>> s = AnimalShelter()
        >>> s.enqueue('Yoda', 'cat')
        >>> assert(s.headCat.animalName == 'Yoda')
        >>> assert(s.headDog is None)
        >>> assert(s.tailCat.animalName == 'Yoda')
        >>> assert(s.tailDog is None)
        >>> assert(s.animalNumber == 1)
        """
        self.animalNumber += 1
        newAnimal = Animal(animalName, animalKind)
        newAnimal.timestamp = self.animalNumber

        if animalKind == "cat":
            """
            첫번째 동물이라면
            head == newAnimal == tail
            """
            if not self.headCat:
                self.headCat = newAnimal
            if self.tailCat: # tailCat이 있다는 자체가 지금의 animalKind는 첫번째 원소가 아니라는 의미 (최소 두전째 원소)
                self.tailCat.pointer = newAnimal
            self.tailCat = newAnimal

        elif animalKind == "dog":
            if not self.headDog:
                self.headDog = newAnimal
            if self.tailDog:
                self.tailDog.pointer = newAnimal
            self.tailDog = newAnimal

    def dequeueDog(self):
        """
        sel.items의 [0]번 인덱스 pop
        :return: 개가 있다면 개의 이름을 리턴
        """
        if self.headDog:
            tempAnimal = self.headDog
            self.headDog = tempAnimal.pointer
            return str(tempAnimal.animalName)
            # 강아지가 한마리일 경우, tail 처리는 안해줌?
        else:
            print("Nog dogs.")

    def dequeueCat(self):
        if self.headCat:
            tempAnimal = self.headCat
            self.headCat = tempAnimal.pointer
            return str(tempAnimal.animalName)
        else:
            print("No cats.")

    def dequeueAny(self):
        if self.headCat and not self.headDog:
            return self.dequeueCat()
        elif self.headDog and not self.headCat:
            return self.dequeueDog()
        elif self.headCat and self.headDog:
            if self.headCat.timestamp < self.headDog.timestamp:
                return self.dequeueDog()
            else:
                return self.dequeueCat()
        else:
            print("No animals.")

    def _print(self):
        print("Cats: ", end="")
        cats = self.headCat
        while cats:
            print(f"{cats.animalName}", end=", ")
            cats = cats.pointer
        print()
        print("Dogs: ", end="")
        dogs = self.headDog
        while dogs:
            print(f"{dogs.animalName}", end=", ")
            dogs = dogs.pointer
        print()


def test_animal_shelter():
    qs = AnimalShelter()
    qs.enqueue("Bab", "cat")
    qs.enqueue("Mia", "cat")
    qs.enqueue("Yoda", "dog")
    qs.enqueue("Wolf", "dog")
    qs._print()
    print(qs.dequeueDog())
    print(qs.dequeueCat())
    qs._print()


if __name__ == "__main__":
    doctest.testmod()
    line1 = "Madam Im Adam"
    line2 = "Buffy is a Slayer"
    print(palindrome_checker_with_deque(line1))
    print(palindrome_checker_with_deque(line2))
    test_animal_shelter()