from itertools import cycle


def infinite(lst, iterations):
    result = ''
    iter_lst = cycle(lst)
    if lst:
        for symbol in range(iterations):
            result += str(next(iter_lst))
    return result


# Тесты
# print(infinite([2, 5, 8], 7))
# print(infinite([], 1000))
# print(infinite([7], 4))

def get_letters(string: str) -> str:
    yield from [elem for elem in string if elem.isalpha()]


# instance = get_letters("34tghiuyh32123")


# print(next(instance))
# print(next(instance))
# print(next(instance))
# print(next(instance))
# print(next(instance))
# print(next(instance))

def fib(elem):
    a = 0
    b = 1
    for _ in range(elem):
        a, b = b, a + b
        yield a


# ff = fib(5)
#
# print(next(ff))
# print(next(ff))
# print(next(ff))
# print(next(ff))
# print(next(ff))


class CartDeck():

    def __init__(self):
        self.length = 52
        self.ind = 0
        self.__cards = [*range(2, 11), 'J', 'Q', 'K', 'A']
        self.__suits = ["pic", "hrest", "bub", "chirv"]
        self.__card_deck = [(val, key) for val in self.__cards for key in self.__suits]

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind < self.length:
            self.ind += 1
            return self.__card_deck[self.ind - 1]
        raise StopIteration


a = CartDeck()
for elem in a:
    print(elem)
