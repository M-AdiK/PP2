x = int(input())
nums = list(map(int , input().split()))

st = set(nums)
srt = sorted(st)
print(" ".join(map(str , srt)))