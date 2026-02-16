def func(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

x = int(input())
ctr = func(x)
for i in ctr:
    print(i)

sq = (x*x for x in range(1,6))
for i in sq:
    print(i)

def fun():
    yield 1            
    yield 2            
    yield 3            
 
# Driver code to check above generator function
for val in fun(): 
    print(val)


def fun():
    return 1 + 2 + 3

res = fun()
print(res)


