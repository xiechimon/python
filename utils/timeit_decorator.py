import time
from functools import wraps


def timeit(func):
    """测量函数运行时间"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} running time: {end - start:.6f} s")
        return result

    return wrapper
