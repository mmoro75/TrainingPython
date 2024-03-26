#############  Here the challenge is to make these bugging script to work ###########################################

###################### Run each program one by one and try to correct the error with the help pf print and console displayed error ##################

########## 1 - make sure the printout output is what it is expected ###########################


### Given the scrip example below: we are asking the user to enter a string and give the options to return the selected string in either UPPER , LOWER or TITLE

### Test all the scenarios and ake sure they work -  There are 3 errors in the scrip see if you can spot them and correct

prompt=input("Please enter your string: ")
action=input("how would you like to display your string : upper/lower or title format?")

if action=="upper":
    print(prompt.upper())
elif action=="lower":
    print(prompt.lower())
elif action=="title":
    print(prompt.title())
else:
    print("please enter a valid action upper/lower or title")


############### 2 - make the below script work as expected   #######################################################################

# there are 3 mistakes here pay attention to varible type , variables not declared that are not supposed to be there and print formatting

a=eval(input("enter your number you want to check into your list: "))

if a not in [1,2,3,4,5,6,7]:
  print(f"provided number {a} is not included into the list")
elif a in [1,2,3,4,5,6,7]:
  print(f"{a} is into your list")


################ 3 -Print all the number in the list with FOR loop  ################################################################

# there are 3 errors in the scrip make sure the print output is what you want , the list is declared properly and the loop syntax is correct

MyList=[1,2,4,5,6,7,8,9,10]
# syntax of for loop = "for" determine the type of loop, "n" is a variable that stores the value for the given main Variable for each iteration, in " variable you want to iterate"
for n in MyList:
    print(f"{n} is in {MyList}")

