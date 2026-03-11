import re

word = input()
x = re.search(r"[aeiouAEIOU]", word)
if x:
    print("Yes")
else:
    print("No")