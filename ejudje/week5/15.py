import re

s = input()

x = re.sub(r"(\d)", r"\1\1" , s)
print(x)