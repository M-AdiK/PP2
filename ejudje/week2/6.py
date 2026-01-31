x = int(input())
nums = list(map(int, input().split()))

imax = nums[0]
for i in nums:
    if i > imax:
        imax = i 
print(imax)