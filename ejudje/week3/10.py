class Person:
    def __init__(self, name , gpa):
        self.name = name
        self.gpa = gpa

    def prnt(self):
        print("Student: "+ self.name + ", GPA:", self.gpa)

name , gpa = input().split()

obj = Person(name,float(gpa))
obj.prnt()