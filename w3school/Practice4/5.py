import math
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)


x = abs(-7.25)
print(x)

x = pow(4, 3)
print(x)


x = math.sqrt(64)
print(x)


x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1

x = math.pi
print(x)

# Print the lowest value
print(min(5,10))
# Print the highest value
print(max(5,10))
# Print the absolute value
print(abs(-7.25))
# Print 4 to the power of 3
print(pow(4,3))



import random

random.seed(10)
print(random.random())

print(random.getstate())

mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))

x = "WELCOME"
print(random.choice(x))

print(random.randint(3, 9))

mylist = ["apple", "banana", "cherry" , "amore mia"]
random.shuffle(mylist)
print(mylist)


