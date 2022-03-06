from algorithms.sort import bubble_sort


def binary_search(collection, elem):
    low = 0
    high = len(collection) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = collection[mid]
        if guess == elem:
            return mid
        elif guess > elem:
            high = mid - 1
        else:
            low = mid + 1
    return None


b = [3, 1, 2, 3, 4, 5, 6, 66, 77, 55, 4, 3, 2, 1, 2, 2, 3, 44, 5]
print(bubble_sort(b, True))

# print(binary_search(coll, 1))
