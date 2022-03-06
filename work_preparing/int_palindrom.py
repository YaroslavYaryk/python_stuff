def get_palindrom(elem: int):

    element = elem + int(str(elem)[::-1])
    while str(element) != str(element)[::-1]:
        element += int(str(element)[::-1])

    return element
print(get_palindrom(48))
