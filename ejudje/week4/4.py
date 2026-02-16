def sqr(x,y):
    for i in range(x, y+1):
        yield i*i

x , y = map(int, input().split())

for i in sqr(x,y):
    print(i)