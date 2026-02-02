class Circle:
    def rad(self):
        self.radius = int(input())
    def area(self):
        return (self.radius**2)*3.14159

obj = Circle()
obj.rad()
print(f"{obj.area():.2f}")