'''
Class

Class is an user define data type.
Class is template.
Class have variables. Class variables are known as objects.
Class has -
    Data members (attributes):
        Class variable
        instance variable
    Methods
        Constructor
        Member functions

Syntax:

class classname:
    """ Class Documentation """
    #class_suite
'''


class myFirstClass:
    """This my First Class in Python
    This is the class documentation"""

    a = 5


c1 = myFirstClass()  # c1 object created
print(type(c1))  # <class '__main__.myFirstClass'>
print(c1.a)  # '.' is called as dot operator


i = int()
l = list()
t = tuple()

c2 = myFirstClass()
