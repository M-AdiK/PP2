def square(x):
    return x*x

n = int(input())
nums = list(map(int , input().split()))

result = sum(map(square , nums))
print(result)