class Person:
    def __init__(self) -> None:
        self.name: str = ""
        self.age: int = 0

    def __str__(self):
        return f"Person({self.name}, {self.age})"

    def say_hello(self, element:int) -> str:
        a = element
        return f"hello, {a}"

    def __setattr__(self, key:str, value):
        super().__setattr__(key, value)
        return self


a = globals().get("Person")().__setattr__("name", "count").__setattr__("age", 18)
# a.__setattr__("name", "count")
# a.__setattr__("age", 18)
for elem in a.__dir__():
    try:
        res = getattr(a, elem).__annotations__
        if res:
            print(res)
    except AttributeError:
        pass
print(__file__)
print(__file__.split("/")[-1])



# for elem in a.__dict__:
#     print(elem.__annotations__)
# print(getattr(a, "name"))
# print(getattr(a, "age"))

# print(a.__getattribute__("say_hello")())
