class Node(object):
    def __init__(self, animalName=None, animalKind=None, pointer=None):
        self.animalName = animalName
        self.animalKind = animalKind
        self.pointer = pointer
        self.timestamp = 0


class AnimalShelter(object):
    def __init__(self):
        self.headCat = None
        self.headDog = None
        self.tailCat = None
        self.tailDog = None
        self.animalNumber = 0

    def enqueue(self, animalName, animalKind):
        self.animalNumber += 1
        newAnimal = Node(animalName, animalKind)
        newAnimal.timestamp = self.animalNumber

        if animalKind == "cat":
            if not self.headCat:
                self.headCat = newAnimal
            if self.tailCat:
                self.tailCat.pointer = newAnimal
            self.tailCat = newAnimal

        elif animalKind == "dog":
            if not self.headDog:
                self.headDog = newAnimal
            if self.tailDog:
                self.tailDog.pointer = newAnimal
            self.tailDog = newAnimal

    def dequeueDog(self):
        if self.headDog:
            newAnimal = self.headDog
            self.headDog = self.headDog.pointer
            return str(newAnimal.animalName)
        else:
            print("No dogs!")

    def dequeueCat(self):
        if self.headCat:
            newAnimal = self.headCat
            self.headCat = self.headCat.pointer
            return str(newAnimal.animalName)
        else:
            print("No cats!")

    def dequeueAny(self):
        if self.headCat and not self.headDog:
            return self.dequeueCat()
        elif not self.headCat and self.headDog:
            return self.dequeueDog()
        elif self.headCat and self.headDog:
            if self.headDog.timestamp < self.headCat.timestamp:
                return self.dequeueDog()
            else:
                return self.dequeueCat()
        else:
            print("No animals!")

    def _print(self):
        print("Cats: ")
        cats = self.headCat
        while cats:
            print(cats.animalName)
            cats = cats.pointer
        print("Dogs: ")
        dogs = self.headDog
        while dogs:
            print(dogs.animalName)
            dogs = dogs.pointer


if __name__ == "__main__":
    qs = AnimalShelter()
    qs.enqueue("bob", "cat")
    qs.enqueue("mia", "Cat")
    qs.enqueue("yoda", "dog")
    qs.enqueue("wolf", "dog")
    qs._print()

    print("하나의 개와 고양이에 대해서 dequeue를 실행합니다.")
    qs.dequeueDog()
    qs.dequeueCat()
    qs._print()


