x = int(input())
num = list(map(int, input().split()))

num.sort()
num.reverse()

for i in num:
    print(i , end=" ")