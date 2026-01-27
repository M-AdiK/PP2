#Logical Operators
x = 5
print(x > 0 and x < 10)

x = 5
print(x < 5 or x > 10)

x = 5
print(not(x > 3 and x < 10))

#identiti operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y) #is false becouse x!=y in memory

#Membership Operators
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)

x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

x = ["apple", "banana"]
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list

#Bitwise Operators
print(6 & 3)

print(6 | 3)

print(6 ^ 3)

print(~3)

print(3 << 2)

print(8 >> 2)

#Operator Predences
print((6 + 3) - (6 + 3))

print(100 - 3 ** 3)

print(100 + ~3)

print(5 == 4 + 1)

print(1 or 2 and 3)

