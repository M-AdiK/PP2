def fib(x):
    a, b = 0, 1
    for i in range(x):
        yield a
        a, b = b, a + b

x = int(input())
cnt  = 0
for i in fib(x):
    cnt += 1
    if cnt != x:
        print(i, end=",")
    else:
        print(i, end="")