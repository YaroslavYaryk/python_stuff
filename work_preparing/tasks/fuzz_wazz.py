from fuzzywuzzy import fuzz

"""Fuzzy string matching like a boss. It uses Levenshtein Distance to calculate the differences between sequences 
in a simple-to-use package."""

a = "hello world"
b = "Hello World"
print(fuzz.ratio(a, b))
