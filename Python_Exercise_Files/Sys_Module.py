#################################### SYS MODULE ####################################################

# sys module is used to work with payton runtime environment - meaning if you want to interact with your python interpreter whislt is running
# sys does not mean your system it means python runtime environment on your system
# function in this module are used to manipulate different part of the python runtime environment

# first it needs to be imported ( remember always print(help(sys) for the complete documentation)

import sys

# print(dir(sys))
print(sys.version)  ## python version running on your system
print(sys.version_info) # this function gives you system info in Tuple ( one example where tuple is used to preserve data)
print(sys.path) # system environment path for python ( locations from where python take info to function)

print(sys.modules)  ## list all the modules imported ( see the not only sys is listed that's because python import modules by default to interpreter)
sys.exit() # stop python script ( it can be used to stop the script wherever you feel it is necessary - it will turn to be very useful )

""" sys.argv it returns list of commands line arguments passed to a python script.

 to pass command line arguments always run script from command 
 
 example:
 
 "python yourscript.py" your command line arguments
  
#### the extra information are called command line arguments  in order to pass them to your script  you need to use sys.argv

with the use of sys whatever is passed as command line arguments they will be included in your script in a list 
basically sys is capturing whatever value you are passing in the command line arguments and include them in a list as string vallues 

note index 0 in the list is always your script name then the value you are passing from command line



"""

import sys
print(sys.argv)
# copy and paste  the above lines on your testing file and now run from command line python yourtestingfile.py  Marco 1 2 3 then observe the output
# you should get the command line arguments in a list note that they are all strings and index 0 is always your script name
"""

### Given the scrip example below: 

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
    """

# now let's rewrite this script in a non-interactive mode by passing arguments with sys.argv and run from command line passing arguments

# ****** run from command line "pyton yourtestfile.py your string action"
import sys

# when passing script arguments from command line better to take care of the entry in order not to get error in case wrong number of arguments are passed
# in this example we expect 3 indexes ( 2 arguments + script name into index 0
if len(sys.argv) !=3: # for this script proper arguments are 3 hence if the entry is different to 3 the if code will run in order not to get error ( 0 script name, 1 is desired string , 2 action)
    print("Please enter correct values as required see example below: ") # reminder instruction for the user to enter proper arguments
    print(f"{sys.argv[0]} <your required string>, <upper,lower,title>") #reminder for the user to enter proper selection
    sys.exit()  # exit the script without error if the correct arguments are not passed

prompt=sys.argv[1] # argument 1 in index 1 is the string from the list created via command line arguments
action=sys.argv[2] # argument 2 in index 2 is the action from the list created via command line arguments (always remember index 0 is script name)

if action=="upper":
    print(prompt.upper())
elif action=="lower":
    print(prompt.lower())
elif action=="title":
    print(prompt.title())
else:
    print("please enter a valid action upper/lower or title")