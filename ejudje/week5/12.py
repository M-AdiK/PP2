import re

s = input()
x = re.findall(r"[0-9]{2,}" , s)

if x:
    print(" ".join(x))
else:
    print("")