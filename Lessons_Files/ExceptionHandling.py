############################################## EXCEPTION HANDLING ############################


# how to handle exception in python:  An exception is an error in your cade that will stop the execution

# A Python program terminates as soon as encounter an error

""" errors are 2 types:
1) syntax error
2) runtime errors ( example dividing by 0, file not present,index out of range or import error etc)

syntax errors cannot be handled instead runtime errors can be handled """

# Runtime errors are in fact called Exceptions, and they can be handled

# example with no existing file
"""
fo=open("File.txt") >>> File "C:/Users/u6017127/PycharmProjects/AutomationTraining.py/venv/ExceptionHandling.py", 
this command gives an error as file do not exist, to handle this runtime error you need to use "try,except" the code is:"""

try:                      # try to run this block of code
    fo=open("file.txt")
    print(fo.read())
    fo.close()
except Exception as e:   # if there is an exception print error
    print(e)    #  >>>>> [Errno 2] No such file or directory: 'file.txt'


"""
exception handling for known error: instead of using e you can handle know errors individually and provide the correct intructions 
see exapmple of known exceptions the more you gain experience the more errors you will get to know and predict:
 
"NameError",
"Type Error",
"FileNotFoundError",
"ZeroDivisionError"

"""

try:
    print(a)
except NameError:   # we can handle exception this way as we know that in case variable a do not-exist the error is NameError type
    print("variable not defined")

########################## FINALLY #########################################

try:
    print("no error on this line")
    import fabric  # remember whenever getting exception the rest of code in try block will not execute
    print(4/0)
except ZeroDivisionError:   # we can handle exception this way as we know that in case variable a do not exist the error is ZeroDivisionError type
    print("you cannot dived by 0")
except ModuleNotFoundError:   # we can handle exception this way as we know that in case module a do not exist the error is ModuleNotFoundError type
    print("your module do not-exist")
except Exception as e:  # you can add extra layer in case of any other not predictable error ( this line always at the end as the execution is sequential
    print(e)
finally:
    print("this code will always execute")  # you can use finally module to run additional code , the code in finally will always execute after try catch


###################### Try Except else and  finally error handling differences #################################
try:
    print("there is no error in try block")
    # print(a)  #if you cause an exception in try block else will not execute
except Exception as e:
    print(e)
else:
    print("this block of code will execute only if no error in try block")  # as opposed to finally that is always executed

########################## Raise user defined Exceptions   ###############################################

# what is custom exception - it is error created by user to display an error, it can be created with "rise" and "assert"

# raise = to raise an existing Exception when we want

"""raise Exception("this is an exception")"""

# to use in real time let's write an if condition if flase instead of print I want to raise an exception and stop the code

age=34
if age<33:
    print("the age range is correct")
else:
    raise ValueError("the age is not in the defined range")  # raise an exception and stop the code ( that's the difference from a standard print out)

############# Assert = to create an AssertionError - assert will raise exception if condition is false ################################

# assert(1>5)  # condition is false AssertError is created and code will stop

try:
    assert(1>5)
except AssertionError:
    print("Assertion error condition is false")