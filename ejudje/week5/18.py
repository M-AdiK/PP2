import re

s = input()
p = input(' ')
x = re.escape(p)
y = re.findall(x , s)

print(len(y))