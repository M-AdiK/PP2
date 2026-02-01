x = int(input())
nums = []

for i in range(x):
    phone = input()
    nums.append(phone)

cnt = {}

for i in nums:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

d = 0

for i in cnt:
    if cnt[i] == 3:
        d += 1

print(d)