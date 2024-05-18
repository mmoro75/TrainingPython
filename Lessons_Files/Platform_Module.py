############################################## PLATFORM MODULE ############################################

# to use for getting information about your underlying hardware and component (architectural information)
import platform

# or import platform as pt
# print(dir(platform))   # to get all the available functions for module platform
# print(help(platform))  # print platfomr module documentation
print(platform.system()) # operating system
print(platform.processor()) # processor
print(platform.python_build())
print(platform.platform()) # multiple information
print(platform.architecture())
print(platform.node())
print(platform.machine())   ### machine type
print(platform.uname())   ### get all info in single command

# ############################ GETPASS MODULE ############################

# - it helps to get user and password from user in a secure manner see examples below:


import getpass

# print(dir(getpass))
# print(help(getpass))

print(getpass.getuser())     # get userid from environment variables

password=getpass.getpass() # prompt user for password in windows in secure way
print("my passwod is:", password) # print password

my_pass=(getpass.getpass(prompt="give me your db password:")) # to customize prompt
print(my_pass)
