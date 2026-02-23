import re

s = input()
x = re.search(r"cat|dog" , s)

if x:
    print("Yes")
else:
    print("No")