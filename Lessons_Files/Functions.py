#################################### FUNCTIONS ####################################################################


# Function is a specific code for a specific operation - it can be reused multiple times in your code based on requirements
# a Function is executed only when it is called

# how to define a function and how to use it

def display():  # keyword def is used to define your function
# function name is only letters or numbers ( not special characters)
# function name cannot start with numbers or special char
# do not include any space in function name
# Similar rule as per defining a variable as discussed in introduction with variable session
    print("this is my display function")
    print("first line of code")
    print("second line of code")
    return None # it is good practice to set up return null if you are not returning any value

display() # to call your function just use its name (remember to define the function in your sequence before it is called)

# functions are for code re-usability
# improve code modularity ---->  try always to write your code logic as a function and re-use it for your scripting

# ----------there are 2 types of Functions--------------------------------------
# *Built-in Functions - Functions that are included in python (built-in)
# *User Defined Functions - Functions that you create based on your requirements

#################### Call a Function from another function and scope of variables ######################################

## pay attention about the scope of the variables === Local and Global

def myfunction1():
    # variable defined inside a function are local variable, and they can be accessed only into the functions #
    name="Marco" # variable inside a Function are local and can only be accessed inside (name won't be accessible from myfunction2)
    print("welcome",name)
    myfunction2() # you can call function 2 inside function 1  ( basically you can call any function in any place in your code )
    return None
def myfunction2():
    print("thank you",x)
    return None
#global variable#
x=10 # variable outside the functions are global and can be accessed (define the variable before calling the function)
myfunction1()

# if you define for example x local variable and x global the function on execution will take the local if local is not here it will look for global
# if none is defined it will fail the execution


# when scripting or coding it is good practise to write your code all into functions you can for instance start with a main function and call other functions
def myfunction1():
    name="Marco"
    print("welcome",name)
    myfunction2()
    return None
def myfunction2():
    print("thank you",x)
    return None

def main():
    global x # you can use the keyword "global" into a function to make the variable available for other functions to use
    x=22
    print("my execution start from main")
    myfunction1() # your code now will start here by calling function main
    return None
main()


# Functions when passing arguments, difference between - Arguments and Parameters

def get_sum(value):
    # The function expect to pass a value for the sum and the variable value is called parameter/positional argument,
    # and it would store the value you pass as an argument
    sum=value+10
    print(f"the result is: {sum}")
    return None
def main2():
    # global num # unless specified is not good to make variable global in your main - best to pass the variable as argument ( see below)
    num=eval(input("give me your number: "))
    get_sum(num) # the variable is passed to your get num as an ARGUMENT
    return None
main2()



########################## Arguments and Return value with a Function ##############################

def get_sum(c,d): #arguments value are stores in parameters c,d to be used in the function
    result=c+d
    return result # the variable result is returned, and it is now accessible to our main function to be printed
    # issue return !=none whenever you want to access function result somewhere else
def main3():
    a=eval(input("give me your number: "))
    b=eval(input("give me your number: "))
    get_sum(a,b) # the variables a and b is passed to your get num as an ARGUMENT
    sum=get_sum(a,b) # you are storing the result in sum of the get_sum function by returning the result in the function itself
    print(f"the result is: {sum}") # sum value now is available, and it can be printed out
    return None
main3()

######################################## Function with default Arguments ################################

def add_number(a,b=0):  # note function needs 2 arguments to be executed however we are assigning default value for b
      # remember default value is position dependent assigning a=0,b is not working as if you pass 1 argument it will always be for a
    result=a+b
    print("the result is:",result)
    return None

add_number(5,6) # function requires two arguments to be passed to get result
add_number(4)  # in this case we can still print the result as we can use default value for b
# add_number() # it will give an error as at least a argument is needed

'''

def add_number(a=0,b):  # remember the arguments are positional therefore in the example we are getting an error because we are passing only 1 and 2 is expected
                         # meaning the default arguments have to be passed at the end 
    result=a+b
    print("the result is:",result)
    return None

add_number(6) # function requires two arguments to be passed to get result

'''

# user for server example

def serv_user_login(user="root"): # default user is root for your server
    print("I am logging in as: ",user)
    return None

serv_user_login("mmoro")
serv_user_login()  # it should give default user



########################## KeyWord based Argument #################################

def display_value(a,b): # remember this a position based argument whoever is passed first get a and second gets b
    print(a,b)
    return None

display_value(a=4,b=3) # we can force the value of the variable to be as we want not depending on position
display_value(b=6,a=8) # in this case names have to match what you are passing into the function ( in this example a and b )

# by doing this way you do not change the order of the values you are passing try all the options to see the output

display_value(b=3,a=4)
display_value(a=8,b=6)

################################### variable length argument ###################################################

# It is a function than can accept n numbers or Arguments and gives result in Tuple, it is defined as follows:

def display_type(*arg): # *args get n number of argument
    # print(type(arg)) # this result is always a tuple
    for each in arg:  #use for loop to get type of each value in the resulting tuple
        print(type(each))
    return None
display_type()
display_type(1)
display_type(1,2,"dir")

############################  function with variable keyword argument #####################################

# same as before it accept n number of Arguments but in this case result is a Dictionary:

def key_val(**karg): # this syntax will give you result of key and value dictionary
    print(karg)  # you basically have a dictionary available in your function based on n number of values from arguments
    return None
key_val(a=1,b="marco",user="root") # you need to pass the arguments in order for the function to give you the result


#################################### How to use Functions of a script into another script ################################################

# first of all import the functions defined in ScriptFunctions to make them available to be called

import ScriptsFunctions

def calculator(a,b):
    result=a+b
    print(result)
    return None

a=5
b=7

calculator(a,b)
ScriptsFunctions.calculator(a,b)

"""
#### modified including main function and if ---name--- ########################
### to be used in your Live_testing file###########################

import ScriptsFunctions

def calculator(a,b):
    result=a+b
    print(result)
    return None

def main():
    a=5
    b=7
    calculator(a,b)
    ScriptsFunctions.calculator(a,b)


if __name__=="__main__":
      main()

"""



"""

# however remember when you are importing a module if operations are available in the module you're importing they will be executed first
# so to define functions and importing modules there are certain basic rules to follow

# to execute a script create always a main function
# include always ---->  if __name__=="__main__":
#                           main()

# this is preventing to run main on imported script but only the ones you are calling on your script

# always use this structure with functions when importing from other modules --- import , main , and if__nanme at the bottom








#################################### BACK+UP For ScriptsFunctions to test ##############################

"""

def calculator(a,b):
    result=a-b
    print(result)
    return None


a=3
b=5
calculator(a,b)


"""
#### modified including main function and if ---name--- ########################
### to be used in your ScriptsFunctions.py file ###########################

def calculator(a,b):
    result=a-b
    print(result)
    return None

def main():
     a=3
     b=5
     calculator(a,b)

if __name__=="__main__":
    main()

"""


