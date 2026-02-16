def f(x):
    for i in range(1 , x+1):
        yield i*i

x = int(input())
for x in f(x):
    print(x)