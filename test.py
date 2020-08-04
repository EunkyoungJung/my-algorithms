class Foo:
    def func1():
        print("function 1")

    def func2(self):
        print(f"function 2 - id {id(self)}")
        print("function 2")


print(f"Foo 클래스의 id: {id(Foo())}")
a = Foo()
print(f"Foo 클래스의 인스턴스 a의 id: {id(a)}")


## 클래스로 함수 호출
Foo.func1()
# Foo.func2()
"""
Traceback (most recent call last):
  File "C:/jek_study/practice_algorithm/test.py", line 15, in <module>
    Foo.func2()
TypeError: func2() missing 1 required positional argument: 'self'
"""
Foo.func2(a)


print("-"*10)


## 클래스 인스턴스로 함수 호출
# a.func1()
"""
Traceback (most recent call last):
  File "C:/jek_study/practice_algorithm/test.py", line 31, in <module>
    a.func1()
TypeError: func1() takes 0 positional arguments but 1 was given
"""

a.func2()
