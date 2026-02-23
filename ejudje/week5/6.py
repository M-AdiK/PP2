import re

s = input().strip()

match = re.search(r"\S+@\S+\.\S+", s)

if match:
    print(match.group())
else:
    print("No email")