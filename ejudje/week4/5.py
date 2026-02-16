def revers(x):
    for i in range(x ,-1 ,-1):
        yield i

x = int(input())
for i in revers(x):
    print(i)