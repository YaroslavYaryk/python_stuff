import random
from functools import wraps
import  math

#
# a = random.randint(3, 10)
# b = random.sample(range(1, 10001), 20)
# print(sum(elem for elem in b))

def fiban_gen(n):
    """ this function get fibo number of element in breckets """

    stor = {}
    a = 0
    b = 1
    for elem in range(1, n + 2):
        if elem not in stor:
            a, b = b, a + b
            stor[elem] = a
    return stor[n]


def fact_wrap():
    stor = {}

    def wrapper(n):
        if not n:
            return 1
        if n not in stor:
            stor[n] = wrapper(n - 1) * n
        return stor[n]

    return wrapper


@wraps(123)
def factorial(n):
    if not n:
        return 1
    return factorial(n - 1) * n


# a = fact_wrap()
# print(a(116))

b = [1, 2, 3, 4, 5]
print(math.fabs((-100.5)))