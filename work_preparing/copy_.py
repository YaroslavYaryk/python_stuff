from copy import deepcopy, copy

a = [123, [123]]
b = copy(a)
c = deepcopy(a)
print(a, b, c)


b[1][0] = 321
# c[1][0] = 222
#
print(a, b, c, sep="\n")
