from time import localtime

a = (1, 2, 3, [1, 2, 3])
a[3].append([elem for elem in [4, 5, 6]])
# print(a)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(list(set(a) & set(b)))

dictionary = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
for elem in sorted(dictionary, key=lambda x: dictionary.get(x))[-3:]:
    print(elem, dictionary[elem], sep="-", end="  ")

dct_1 = {1: 2}
dct_2 = {2: 3}
dct_3 = {3: 4}
res = {}
for elem in (dct_1, dct_2, dct_3):
    res.update(elem)
print("\n", res)

nums = [45, 55, 60, 37, 100, 105, 220]
b = list(filter(lambda x: not x % 15, nums))
print(b)