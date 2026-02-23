import re

txt = input()
x = re.findall(r"\w+" , txt)
cnt = 0
for i in x:
    if len(i)==3 :
        cnt += 1
print(cnt)