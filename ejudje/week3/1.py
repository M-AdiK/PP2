def func(x): 
    b = True
    lst = list(map(int, x))
    for i in lst:
        if i%2!=0:
            return False
    return True

x = input()   
if func(x)==True:
    print("Valid")
else:
    print("Not valid")