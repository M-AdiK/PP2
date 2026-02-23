import re

s = input()
x = re.findall("\\d" , s)
if x :
    print(" ".join(x))
else:
    print("")