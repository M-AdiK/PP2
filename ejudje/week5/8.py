import re

s = input().strip()
d = input().strip()

x = re.split(d , s)
print(",".join(x))