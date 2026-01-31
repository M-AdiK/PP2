x = int(input())
nums = list(map(int, input().split()))

imax = nums[0]
imin = nums[0]

for i in nums:
    if i > imax :
        imax = i

for i in nums:
    if i < imin:
        imin = i

for inx in range(len(nums)):
    if nums[inx] == imax :
        nums[inx] = imin

for i in nums:
    print(i , end=" ")