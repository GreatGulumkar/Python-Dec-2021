"""
Function overloading

Function overloading allows us to create multiple functions with same name but 
different parameter.

THIS IS NOT ALLOWED IN PYTHON

creating multiple functions with same name will not give an error but 
the last defination will be the final one.
"""


from pyrsistent import b


def add():
    return 5+6


print(id(add))


def add(a, b):
    return 5+7


# print(add())
print(id(add))


a = 5
print(id(a))

a = 6
print(id(a))
print(a)


int add(int a, int b):
    a+b

int add(float a, float b):
    a+b


def add(a, b):
    a+b


def add(a, b):
    a+b


add()
