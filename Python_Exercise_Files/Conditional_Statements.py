################################### Conditional Statements ####################################################
"""
Conditional statements (if, else, and elif) are fundamental programming constructs that allow you to control the flow of your program
based on conditions that you specify. They provide a way to make decisions in your program and execute different code based on those decisions.
"""

# if is called simple conditional statement use to control the execution of set of lines or block of code

"""
if expression:
   statement1
   stetement2

   you can use
   -comparison operators
   -identity operators
   -membership operators
   -logical operators

"""

# if and Else conditional statement to be used only if the conditions are 2 yes or no

my_string=input("do you want your number in letter? please enter yes or no:")

if my_string=="yes":
    print("your number will be converted in letters in the next scrip")
else:
    print("thank you for your time")


# for multiple conditions the option is using "elif"  - else if

a=eval(input("enter your number you want to check into your list: "))

if a not in [1,2,3,4,5,6,7]:
  print(f"provided number {a} is not included into the list")
elif a == 1:
  print(f"{a} is into your list")
elif a == 2:
  print(f"{a} is into your list")
elif a == 3:
  print(f"{a} is into your list")
elif a == 4:
  print(f"{a} is into your list")
elif a == 5:
  print(f"{a} is into your list")
elif a == 6:
  print(f"{a} is into your list")
elif a == 7:
  print(f"{a} is into your list")
else:
  print(f"{a} is into your list")




# example how to optimize the code and print the provided number in list by using dictionary


a=eval(input("enter your number you want to check into your list: "))
num_dic={1:1,2:2,3:3,4:4,5:5,6:6,7:7}   # define dictionary value-keys

if a not in [1,2,3,4,5,6,7]:
    print(f"{a} is not included in your list ")
else:
    print(f"{num_dic.get(a)} is included in your list")   # use get to print value of given key
