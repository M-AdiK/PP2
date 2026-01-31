
import math as m
x = int(input())

prime = False

for i in range(2 , int(m.sqrt(x))+1):
    if n % i == 0:
        prime = True
        break
if prime == True:
    print("Yes")
else:
    print("No")