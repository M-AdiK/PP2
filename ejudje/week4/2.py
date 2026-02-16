def even(x):
    for i in range(x+1):
        if i%2==0:
            yield i

x = int(input())
for i in even(x):
    if i != x and i != x-1:
        print(i, end=",")
    else:
        print(i, end="")