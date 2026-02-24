import re

s = input()

y = re.findall("No dates", s)
if s == "No dates":
    print(0)
else :
    x = re.findall(r"([0-9][0-9])(/)([0-9]{2,})(/)([0-9]{4,})" , s)
    print(len(x))