import re
s1 = input()
s2 = input()
x = re.search(s2 , s1)
if x : print("Yes")
else: print("No")