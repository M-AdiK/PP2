def func(animal,name):
    print("I have a" , animal)
    print("My", animal + "s name is" , name)

func(name = "Buddy" , animal = "Dog")

#при использований именованных аргументов порядок их не важен

def func1(fruits):
    for fruit in fruits:
        print("I like "+ fruit)

fruitss = list(map(str, input().split()))
func1(fruitss)

def calc(x,y):
    return x+y+x+y

print(calc(48,1))


def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

def my_function(name, /):
  print("Hello", name)

my_function("Emil")


def my_function(name, /):
  print("Hello", name)

my_function(name = "Emil")


def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

