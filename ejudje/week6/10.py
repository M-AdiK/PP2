x = int(input())
nums = list(map(int , input().split()))

def nnzr(x):
    return x != 0

z = sum(map(nnzr , nums))
print(z)