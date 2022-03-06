# class A():
#     pass
#
# class B(A):
#     pass
#
# class C(A):
#     pass
#
# class D(B, C):
#     pass
#
# print(D.mro())

def fff(A, B, *args):
    arr = [0 for elem in range(A)] + [elem for elem in list(range(A, B + 1))]
    for elem in args:
        arr[elem[0]:elem[1] + 1] = [0 for k in range(elem[0], elem[1] + 1)]
    return len(list(filter(lambda x: x, arr))) + 1


print(fff(15, 165, [37, 68], [52, 74], [118, 146], [35, 44], [37, 65], [46, 74]))


a = list(range(0, 99, 2))


def chank(array: list, size):
    var = len(array)//size
    ell = [el for el in range(len(array)) if not el % var]
    arr = [array[ell[i]:ell[i + 1]] if i < len(ell)-1 else array[ell[i]:] for i in range(len(ell))]
    return arr


# print(chank(a, 5))
