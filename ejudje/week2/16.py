x = int(input())
nums = list(map(int, input().split()))

seen = set()

for i in nums:
    if i not in seen:
        print("YES")
        seen.add(i)
    else:
        print("NO")