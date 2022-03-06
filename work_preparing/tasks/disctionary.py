dictionary = {}
dictionary["str"] = 123
dictionary[(123,)] = [1, 2, 3]

print(dictionary[(123,)])
dictionary.pop("str")
print(dictionary.keys())

a = {1, 2, 3, 4, 5}
b_frozen = frozenset({3, 4, 5, 6})
print(a, b_frozen)
print(a | b_frozen)
print(a & b_frozen)
print(a ^ b_frozen)