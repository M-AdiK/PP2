import re

pat = re.compile(r"\w+")

s = input()
x = pat.findall(s)
print(len(x))