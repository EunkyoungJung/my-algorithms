from functools import wraps
import time


def benchmark(method):
    # 파이썬 코드에서 데코레이터를 사용한다면,
    # 디버깅을 위해서 functools.wraps 모듈을 사용!
    # 결과의 차이는 없으나
    # __name__과 __doc__값은 차이가 있다!
    @wraps(method)
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        # print(f"{method.__name__} : {((te - ts) * 1000)}")
        # print(f"{method.__name__} : {((te - ts) * 1000)}ms")
        print(f"{method.__name__}: {(te-ts) * 1000} ms")
        return result

    return timed