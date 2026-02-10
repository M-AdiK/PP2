s = input().lower().replace(" ","")
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else :
        d[i] += 1
mx = 0
ans = ""
for i in s:
    if d[i] > mx:
        mx = d[i]
        ans = i
print(ans)