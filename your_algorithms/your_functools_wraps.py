"""
functools.wraps를 사용하면 __name__과 __doc__ 정보를 확인할 수 있어요
"""

from functools import wraps


def logged(func):
    def with_logging(*args, **kwargs):
        """with_logging() 함수"""
        print(func.__name__ + "호출")
        return func(*args, **kwargs)
    return with_logging


@logged
def f(x):
    """첫 번째, 데코레이터 사용"""
    return x + x * x


def f2(x):
    """두 번째, 데코레이터 사용 X"""
    return x + x * x


def logged2(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " 호출")
        return func(*args, **kwargs)
    return with_logging


@logged2
def f3(x):
    """세 번째, wraps와 데코레이터 사용"""
    return x + x * x


if __name__ == "__main__":
    print(f"결과: {f(5)}")
    print(f"__name__: {f.__name__}")
    print(f"__doc__: {f.__doc__}")
    print('-'*20)
    f2 = logged2(f2)
    print(f"결과: {f2(5)}")
    print(f"__name__: {f2.__name__}")
    print(f"__doc__: {f2.__doc__}")
    print('-'*20)
    print(f"결과: {f3(5)}")
    print(f"__name__: {f3.__name__}")
    print(f"__doc__: {f3.__doc__}")

