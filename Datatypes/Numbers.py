"""
Datatypes in Python

Datatype are the structure in which data is store.
It also define what kind of data is to be store.
There some methods and operation on them.

Datatypes
1.Numbers
    1.1 Interger
    1.2 Float
    1.3 Complex
2.String
3.Boolean
4.list
5.tuple
6.sets
7.dictionary 



There are not set fix sizes of the datatypes in python

Mutable Datatypes
Non Mutable Datatypes
"""

# nunbers

# integers
# All integer numbers comes under integers.

a = 5
print(type(a))

b = 6
print(type(b))

c = 5
print(type(c))
print(a, b, c)

print("a = ", id(a))
print("b = ", id(b))
print("c = ", id(c))

c = 9

print("c = ", id(c))
print("a = ", id(a))

print(dir(int))

print(a.denominator)
print(a.numerator)
print(a.imag)
print(a.__abs__())
print(a.__add__(10))

print(a.__doc__)

print(a)


############### float ######################

p = 1.1

print(p.__doc__)

print(p.__dir__())

print(p.__eq__.__doc__)

print(p.__eq__(1.1))

print(p.is_integer.__doc__)

print(1.0.is_integer())


############# Complex ##############

# in complex data type, there are number in the form of real and img number
# complex numbers
# eg. 1+6i,-2-9i

s = 5 - 6j

print(s)

print(s.real, s.imag)

print(s.__dir__())

print(s.__neg__())
