def func(x):
    while x%2==0:
        x //= 2
    while x%3==0:
        x //= 3
    while x%5==0:
        x //= 5
    if x == 1:
        print("Yes")
    else:
        print("No")


x = int(input())
func(x)