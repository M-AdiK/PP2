s = input()
l = []
m = []
for i in s:
    if i.isdigit():
        l.append(i)
    else :
        m.append(i)
letts = ''.join(m)
dig = ''.join(l)
print(letts+dig)