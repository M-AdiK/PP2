class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self , len):
        self.len = len

    def area(self):
        return self.len*self.len

x = int(input())
obj = Square(x)
print(obj.area())