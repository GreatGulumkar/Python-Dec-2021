"""
Exception Handling

When a special case happens to handle that situation exception handling is used.

Syntax:

try:
   You do your operations here
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block. 


Types of exception classes:
	
1)Exception
    Base class for all exceptions
2)ArithmeticError
    Base class for all errors that occur for numeric calculation.
3)ZeroDivisonError
    Raised when division or modulo by zero takes place for all numeric types.


try:
    print("Hello")
    a = 10
    b = 10
    c = a/b  # ZeroDivisionError - raise exception.
    print("End of try")
except Exception:
    print("Error")
# Else block is not compulsory.
else:
    print("Thank you!")


try:
    print("Hello")
    a = 10
    b = 0
    c = a/b  # ZeroDivisionError - raise exception.
    print("End of try")
except EOFError:
    print("Error")
except Exception:
    print("Exception Error")
# Else block is not compulsory.
else:
    print("Thank you!")

try:
    print("Hello")
    a = 10
    b = 10
    c = a/b  # ZeroDivisionError - raise exception.

    fruits = {1: "Apple", 2: "Mango"}
    print(fruits[4])
    print("End of try")

except KeyError as k:
    print("Wrong key ", k)

except Exception as arg:
    print("Error :- ", arg)

# Else block is not compulsory.
else:
    print("Thank you!")

try:
    print("Hello")
    fruits = {1: "Apple", 2: "Mango"}
    print(fruits[2])
    print("End of try")

except KeyError as k:
    print("Wrong key ", k)
else:
    print("No exception occured")
finally:
    print("This block will be executed always")


try:
    print("Hello")
    fruits = {1: "Apple", 2: "Mango"}
    print(fruits[2])
    print("End of try")

except:  # not giving any specific exception class will except all types of excptions
    print("Error")


try:
    fruits = {1: "Apple", 2: "Mango"}
    # print(fruits[4])
    l = [1, 2, 3]
    # print(l[5])

    import John
except (KeyError, IndexError):
    print("Error type 1")
except ImportError:
    print("Error type 2")


"""

####### Raise an exception #########
# This allows you to raise exception wherever you want.
# to do this Exception class is used
# Syntax:
# raise [Exception[, args[, traceback]]]
try:
    marks = 10

    if marks < 50:
        raise  # Exception("Fail")
    else:
        print("Congrats")

except Exception as m:
    print(m)
