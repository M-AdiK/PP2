x = int(input())
z = x
cnt = 0
if x%2==1 :
    print("NO")
else:
    while x>0 :
        if(x%2==0):
            cnt += 1
        x = x//2
    if z == pow(2,cnt):
        print("YES")
    else:
        print("NO")
