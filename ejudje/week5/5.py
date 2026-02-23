import re

s = input()
x = re.search("^[a-zA-Z]", s)
y = re.search("[0-9]$" , s)
if x and y:
    print("Yes")
else:
    print("No")

if re.fullmatch(r"^[a-zA-Z].*[0-9]$" , s):
    print("YES")
else:
    print("NO")