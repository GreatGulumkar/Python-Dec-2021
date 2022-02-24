"""
Scope 

Scope is of avariable. It defines the reach or accessability of the variable.

"""

maxi = 999


def compare(a):
    if(a > maxi):   # maxi was defined outside the function yet we can access it inside.
        print("From global")
    else:
        mini = 0
    print(mini)


compare(5)
# print(mini)


def compare1(a):
    # global keywork will make this variable accesseable all over the program.
    global mini
    if(a > maxi):   # maxi was defined outside the function yet we can access it inside.
        print("From global")
    else:
        mini = 0
    print(mini)


compare1(5)
print(mini)
