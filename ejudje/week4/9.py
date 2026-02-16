def sqr(x):
    for i in range(x+1):
        yield 2**i

x = int(input())
for i in sqr(x):
    print(i, end=" ")