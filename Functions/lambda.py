"""
Lambda

Lambda is a one line function.
Lambda is anonymous function. Lambda is a function with no name.
Lambda can take as many argument as possible. 
But lambda has only one expression in the body.
Lambda has inbuild return function that will always return the output of the expression.

Syntax:

variable = lambda argument1[,argument2] : expression

"""

# double = lambda x : x*2 == def double(x): return x*2


#double = lambda x : x*2

p = (lambda x: x*2)(5)
print(p)

greater = (lambda x, *y: 50 if(x > y[0]) else 500)

print(greater(5, 6))

print(greater)


def greater(x, y):
    if x > y:
        return 50
    else:
        return 500
