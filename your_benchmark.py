from functools import wraps
import time


def benchmark(method):
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