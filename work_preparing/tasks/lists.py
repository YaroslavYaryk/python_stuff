lst = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
lst.append("str")
lst[5] = 123
lst.append([1, 2, 3, 4, 5])
lst[3] = (1, 2, 3, 5)
print(lst[5])
print(lst)
lst.remove(1)
print(lst)
print(lst.count(1))
print(lst[0], lst[-1])

a = 3
b = 5
a, b = b, a
print(a, b, sep="\n")

k = [1, 2, 3, 1, 4, 4, 2, 9]
print(len(k) == len(set(k)))

lister = [elem for elem in range(18, 0, -4)]
print(lister)
print(end="\n\n")

summ = 0
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
for elem in lst:
    if elem < 30 and elem % 3 == 0:
        print(elem)
        summ -= elem
print(sum(lst) + summ)

elem = 123456
print(sum(int(i) for i in str(elem)))