'''
Function

When block of code is named it is know as function.
Funtion are used to write specific take in a program.
Funtions are used for resuabiliy.
Functions are called whenever required.
Funtions have agruments as inputs.
Funtions return one more values as outputs.

Syntax:

def function_name(parameters):
    """Function Doc"""
    block of code
    return [expresion(s)]
'''


from re import M


def add():
    a = 10
    b = 20
    print(a+b)


# print(a)

add()
add()
add()


def add():
    """This is function documentation.
    in this string we can write briefy about current functions.
    fucntion doc is the string that is on the very next line after the function name"""

    a = 10
    """" a is 10 """
    b = 20
    return a*b


print(add())
print(add.__doc__)


def mul(a, b):
    return a*b


z = mul(5, 5)
print(z)


"""
Function Arguments types
Required arguments
Keyword arguments
Default arguments
Variable-length arguments
"""

# Required arguments
# this type of arguments are required when a function is called.


def subs(a, b):
    return a - b


#z = subs()
# Traceback(most recent call last):
#  File "f:/Python/Functions/function.py", line 71, in <module >
#  z = subs()
# TypeError: subs() missing 2 required positional arguments: 'a' and 'b'

z = subs(6, 7)
print(z)

# Keyword arguments
# using Keyword arguments we can assign values to the parameters indiviually

z = subs(b=7, a=6.0)
print(z)


# Default arguments
# while definning a function we can set some default values to a parameter.
# This  value will be used in the function if vlaue to the argument is not given while calling a function.
# default argument should be always after requied argument

def subs(a, b=1):
    return a - b


#z = subs(5, 2)
print(subs(5))

print()
# Variable-length arguments
# Using variable length argument, we can call a function with as many argument as possible.


def p(a, *z):  # *argument_name is a variable argument, this is a tuple.
    print(a)
    for i in z:
        print(i)
    print(z)


p(5)

#p(a = 5,z = {6,7,8,9,10})


j, k, l, m, n = 1, 2, 3, 4, 5

print(j, k, l, m, n)


def add():
    a = 10
    b = 20
    return a, b


q, w = add()

print(q, w)
