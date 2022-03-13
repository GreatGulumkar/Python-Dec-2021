"""
Data hiding

In python we can hide data of a class by defining a variable with __ at prefix;

Syntax

__varaible_name
"""


class login:
    def __init__(self):
        self.user = 'defualt'
        # we cannot access this variable anywhere outside this class.
        self.__password = 'pass'


class forgot(login):
    def show(self):
        print(self.__password)


l1 = login()
#l1.user = "John"
f1 = forgot()
f1.show()

print(l1.user)
print(l1.__password)
