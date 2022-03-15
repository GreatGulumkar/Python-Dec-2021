"""
Operator overloading




Operator that you can overload 
Operator	Magic Method
+	__add__(self, other)
-	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)

<	__lt__(self, other)
>	__gt__(self, other)
<=	__le__(self, other)
>=	__ge__(self, other)
==	__eq__(self, other)
!=	__ne__(self, other)


-=	__isub__(self, other)
+=	__iadd__(self, other)
*=	__imul__(self, other)
/=	__idiv__(self, other)
//=	__ifloordiv__(self, other)
%=	__imod__(self, other)
**=	__ipow__(self, other)
>>=	__irshift__(self, other)
<<=	__ilshift__(self, other)
&=	__iand__(self, other)
|=	__ior__(self, other)
^=	__ixor__(self, other)

-	__neg__(self)
+	__pos__(self)
~	__invert__(self)

"""
# a = 4
# b = 5
# c = a+b
# print(9)


class rectangle:
    def __init__(this, l=1, h=1):
        this.length = l
        this.height = h

    def area(this):
        return this.length * this.height

    #    middle left  right -> obj1 + obj2
    def __add__(obj1, obj2):
        temp = rectangle()  # new temp object of rectangle class is created
        temp.length = obj1.length + obj2.length
        temp.height = obj1.height + obj2.height
        return temp

    def __gt__(obj1, obj2):
        return obj1.area() > obj2.area()

    def __sub__(obj1, obj2):
        temp = rectangle()  # new temp object of rectangle class is created
        temp.length = obj1.length - obj2.length
        temp.height = obj1.height - obj2.height
        return temp


r1 = rectangle(5, 6)
print(r1.area())

r2 = rectangle(2, 3)
print(r2.area())

r3 = r1+r2  # call __add__()
"""
def __add__(r1, r2):
        temp = rectangle()  # new temp object of rectangle class is created
        temp.length = 5 + 2
        temp.height = 6 + 3
        return temp
"""

print(type(r3))
print(r3.length)
print(r3.height)
print(r3.area())


print(r2 > r1)


print(dir(5))
print()
print(dir(r1))

print(r1.__module__)


class temp:
    pass


print('\n\n', dir(temp))


"""
method      -> is just a normal method
_method     -> should not be called unless you know what you are doing, which normally means that you have written the method yourself.
__method    -> the 2 underscores are used to prevent name mangeling. Attributes or methods like this are accessible over instance._ClassName__method. Although a lot of people call this "private" it is not. You should never use this to prevent someone from accessing this method, use _method instead.
__method__  -> is used for special methods which modify the behavior of the instance. Do not name your own methods like this.
"""
