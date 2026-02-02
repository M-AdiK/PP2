def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil") #error потому что функция ожидает 2 параметра а там 1

def func(name = "Adik"):
    print("Hello" + name )

func("Bro")
func("CHto")

