x = int(input())
nums = list(map(int, input().split()))

imax = nums[0]
iin = 0

for inx in range(len(nums)):
    if nums[inx] > imax:
        imax = nums[inx]
        iin = inx
print(iin+1)