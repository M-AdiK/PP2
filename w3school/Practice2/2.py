print (10+5) #+ operator

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)


#Arifmetic operators
print(10-5)
print(10*5)
print(10/5)
print(10%5)
print(10**5)
print(10//5)

#Assignment operators
=	 x = 5	    x = 5	
+=	 x += 3	    x = x + 3	
-=	 x -= 3	    x = x - 3	
*=	 x *= 3	    x = x * 3	
/=	 x /= 3	    x = x / 3	
%=	 x %= 3	    x = x % 3	
//=	 x //=3	    x = x //3	
**=	 x ** 3	    x = x **3	
&=	 x &= 3	    x = x & 3	
|=	 x |= 3	    x = x | 3	
^=	 x ^= 3	    x = x ^ 3	
>>=	 x >>=3	    x = x >>3	
<<=	 x <<=3	    x = x <<3	

#Warlus operator only >=3.8
numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")


#Comparison operators
x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 5

print(1 < x < 10)

print(1 < x and x < 10)