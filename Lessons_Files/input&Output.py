#################################   How to get values from external user ########################################

#### The input() function takes input from the user and returns it.

# input is always a string

a=input("what is the value of a:")
b=input("what is the value of b:")
c=a+b
print(f" if you have {a} and {b} added together the value is {c}")

# if you want an int (or any other data type) it has to be converted

a=int(input("what is the value of a: "))
b=int(input("what is the value of b: "))
c=a+b
print(f" if you have {a} and {b} added together the value is {c}")

#eval will let python evaluate your input and coverted to the relevant data type (while using eval function if you want value as string "" has to be used)


a=eval(input("what is the value of a: "))
b=eval(input("what is the value of b: "))
c=a+b
print(f" if you have {a} and {b} added together the value is {c}")