text = 'lorem ipsum dolor sit amet amet amet'

text_part = text.split()
max_count = max(text_part.count(elem) for elem in text_part)
print(" ".join({elem for elem in text_part if text_part.count(elem) == max_count}))
print(sorted(text_part, key=len, reverse=True)[0])

