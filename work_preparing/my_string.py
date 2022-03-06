import re


string = "Python is a programming language"
print(string.isalnum())
string = "world hello"
print(string.isalnum())
print("hello world hello".isalnum())
print(str(re.search("hello", string)))  # find pattern in the whole string

print(str(re.match("hello", string)))  # find pattern only in the beginning
