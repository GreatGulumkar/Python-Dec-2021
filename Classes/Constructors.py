"""
Constructor

Constructors are used to initialize the objects.
In constructors are made using __inti__().

Syntex:

class class_name:
    def __init__(self,[parameters]):
        #Object initialization

Class variables
Class variables are variables defined in the class. and they are can accessed with classname
When you can call a variable usings classname then it is a Class variables .
Class variables are independent of instances.

Instance variables
Instance variables are defined in __init__().but is not compulsary.
When you can call a variable usings instance then it is an instance.

"""


class myStudentClass:
    """In this class we are going to learn about 
    constructors,
    self,
    class varables
    instance variables
    in Python"""

    # class variables
    std_count = []

    def __init__(self):  # self is used to access instance variable, in classes, first arg of a function is
        # is always self.
        # following are the instance variables.
        self.name = ''
        self.roll = -1
        self.marks = -1

        # we dont need self with class variables, but we need class name.
        myStudentClass.std_count.append(1)

    '''__init__(s1):   #self is replaced my object/instance name
        s1.name =''
        s1.roll =-1
        s1.marks =-1'''


s1 = myStudentClass()  # we dont need to mention self while calling a function.
print(s1.name, s1.roll, s1.marks)

print(myStudentClass.std_count, id(myStudentClass.std_count))

s2 = myStudentClass()
print(s2.name, s2.roll, s2.marks, s2.std_count)


print(myStudentClass.std_count, id(myStudentClass.std_count))
