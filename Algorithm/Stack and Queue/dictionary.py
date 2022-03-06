def hashh(elem):
    return int("".join([str(ord(el)) for el in elem]))


print(hashh("apple"))
