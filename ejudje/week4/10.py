def f(lst , k):
    for i in range(k):
        for x in lst:
            yield x

lst = input().split()
k = int(input())
for i in f(lst , k):
    print(i , end=" ")