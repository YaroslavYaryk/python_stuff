class HelloWorld:

    def __init__(self, number):
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.number:
            raise StopIteration
        self.index += 1
        return "Hello World"


a = HelloWorld(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
