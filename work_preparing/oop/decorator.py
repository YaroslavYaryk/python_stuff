from time import perf_counter


def timer(funk):
    def wrapper(*args, **kwargs):
        time1 = perf_counter()
        res = funk(*args, **kwargs)
        print(perf_counter() - time1)
        return res

    return wrapper


class Timer:

    def __init__(self, funk):
        self.__funk = funk

    def __call__(self, *args, **kwargs):
        time1 = perf_counter()
        res = self.__funk(*args, **kwargs)
        print(perf_counter() - time1)
        return res


@Timer
def get_pow(n):
    res = n ** n ** n


get_pow(8)
