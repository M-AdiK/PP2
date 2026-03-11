x = int(input())
keys = input().split()
values = input().split()
query = input()

found = False

for k, v in zip(keys , values):
    if k == query:
        print(v)
        found = True
        break
if not found:
    print("Not found")