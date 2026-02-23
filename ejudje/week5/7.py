import re 

s = input()
p = input()
r = input()

y = re.sub(p , r , s)
print("".join(y))