def even(x):
    return x % 2 == 0

n = int(input())
nums = list(map(int, input().split()))

result = len(list(filter(even , nums)))
print(result)