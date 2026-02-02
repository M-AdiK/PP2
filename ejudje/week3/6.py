class Rectangle:
    def getint(self):
        x , y = input().split()
        self.x = int(x)
        self.y = int(y)

    def prnt(self):
        print(self.x * self.y)

obj = Rectangle()
obj.getint()
obj.prnt()