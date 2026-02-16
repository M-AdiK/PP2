import math as m

def primes(n):
    for x in range(2, n + 1):
        for i in range(2, int(m.sqrt(x)) + 1):
            if x % i == 0:
                break
        else:
            yield x

n = int(input())
for p in primes(n):
    print(p, end=" ")
