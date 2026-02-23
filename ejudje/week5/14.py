import re

s = input()
x = re.compile(r"[0-9]+|[a-zA-Z]+")
result = x.fullmatch(s)
if result :
    print("Match")
else:
    print("No match")