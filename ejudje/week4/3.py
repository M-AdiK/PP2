def divis(x):
    for i in range(0, x+1):
        if i%3==0 and i%4==0:
            yield i

x = int(input())
for i in divis(x):
    print(i, end=" ")