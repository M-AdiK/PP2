import re

s = input()
x = input()

cnt = 0
for i in re.finditer(x , s):
    cnt += 1
print(cnt)