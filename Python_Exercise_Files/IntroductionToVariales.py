########################################   Variables ############################################

                      # What is a variable?
# It is a reserved spaced of memory to store a value. you are giving the computer data to work on


                              # how to declare a variable

# python already indentify what kind of variable you are declaring you do not need to specify in fact Python is called Dynamically typed language
x=2 # variable x is an int
y=4.5 # variable is a float
z="name" # varibale is a string

print(type(x))
type(y)
type(z)

# display a variable using print

print(z) # do not use "" now you are printing the value stored in memory location called z

# re declare a variable = you can simply give the variable a new value following line and variable stores the new value

d=10
print(d)
d=20
print(d)

# delete a variable = of python program is too long and you are not using the varible anymore you can delete a variable to free up memory

c=10
print(c)
del c
print(c)


# rules to define a variable names

"""
1) it only contain letters numbers and underscore
example  "install_pkg=" or "file_name=" 

2) do not use pre defined words in python
example "if_code=" cannot be used because "if" is a pre defined word in pyton for conditional statements ot "print" or "while"

3) can't contain spaces 
example "my name=" not valid name 

4) do not start variable name with a number 

5) remember variable name are case sentitive 
example "MyName=Marco" is different from myname=Marco 



"""

