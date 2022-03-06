import time


with open("python.txt", "r") as f:
    first_ten = f.read(10)
    # print(first_ten)

with open("python.txt", "r") as f:
    all_file = f.read()
    # print(all_file)

b = time.localtime(time.time())
# print(b)

def get_ext(filename:str):
    file_part = filename.split(".")
    if len(file_part) < 2:  # filename has no dots
        raise ValueError('the file has no extension')
    if file_part[-1]:
        return filename.split(".")[-1]
    raise ValueError

print(get_ext("sfsd/fdsfds/sdfs/test.py"))

def get_elems(a:list, b:list):
    return [elem for elem in a if elem not in b]

print(get_elems([1,2,3,4,5], [3,4,5,6,7]))