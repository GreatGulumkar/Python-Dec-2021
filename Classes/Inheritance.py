"""
Inheritance

Inheritance is one of th four pillers of OOP.
Accessing members of one class into another.

Syntax:
class ChildClassName (ParentClass1[, ParentClass2, ...]):
   'Optional class documentation string'
   class_suite


Polymorphism

In polymorphism we can create multiple functions with same name.
In python we can create multiple functions with same name in one class,
but only the last defination will be the final one. (Func Overloding is not possible)
To implement polymorphism in pyhton we can define multiple function with same name
in different classes.

"""


class animals:

    def __init__(self):
        self.legs = 0  # no of legs of the animals - 1,2,3,4,5
        self.place = ''  # places where they live like land water desert ice

    def showData(self):
        print(self.legs, self.place)

    def fromAnimal(self):
        print("I am an animal")


class fish(animals):

    def __init__(self):
        self.type = ''  # type water in which fish live - salt, black, fresh

    def showData(self):
        print(self.type, self.legs, self.place)


class reptiles(animals):

    def __init__(self):
        self.color = ''

    def showData(self):
        print(self.color, self.legs, self.place)


r1 = reptiles()
r1.color = "Red"
r1.legs = 0
r1.place = "Land/Water"
r1.showData()
r1.fromAnimal()
print()
f1 = fish()
f1.legs = 0
f1.place = "water"
f1.type = "Salt"
f1.showData()
f1.fromAnimal()
print()
a1 = animals()
a1.legs = 2
a1.place = "Sky"
a1.showData()
