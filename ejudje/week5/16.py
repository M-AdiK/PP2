import re

s = input()

x = re.search(r"Name: ([^,]+), Age: (\d+)", s)
if x:
    print(x.group(1) , x.group(2))
