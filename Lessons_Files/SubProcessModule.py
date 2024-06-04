################################# SUBPROCESS MODULE ####################################################


# This module is useful to execute operating commands on your system (it is a default module in python no download just import )

'''
note even "os.system("dir") can execute commands on your system however you cannot store results in variables like:
a=os.system("dir") -----> result is always a printed out and not stored it will only store 0=command executed or 1=command fail
'''

import subprocess

"""
# with subprocess you can run command and store in variables the result

sp=subprocess.Popen(cmd,shell=True/False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True) # syntax to run command
# if your command is a string you have to set shell=True (cmd="dir")
# if not and it is a list for example you nee to set shell=False (cmd=["ls -ltr","dir","pwd"])
#universal_newline=True to get result as a string as oppose to bytes ( by default result is in bytes)
rc=sp.wait()  # set wait time for command to execute and store result to variable rc ( if 0 success if 1 fail)
out,err=sp.communicate()  # store result in 2 variables out or error
print(f"the output is: {out}")  # print output result
print(f"Error is: {err}") # print error result
"""

cmd=input("provide the command you want to run: ")
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True) # syntax to run command note shell=True
rc=sp.wait()
out,err=sp.communicate()
print(f"the command fails code is {rc}") # print error code
print(f"the output is: {out}")
print(f"Error is: {err}")
# if you need the result as list when it is required you can use splitlines
print(f"Command Result in List is: {out.splitlines()}")
print(f"Command Result in List is: {err.splitlines()}")



##### FOR WINDOWS ALWAYS USE SHELL=TRUE AND COMMAND AS STRING###

''' note this block of code won't work on windows######

cmds=input("provide list of commands you want to run: ")
cmds.split() #convert your command to a list or pass the command as a list directly
print(type(cmds))
sp=subprocess.Popen(cmds,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True) # shell=false to run list of commands
rc = sp.wait()
out, err = sp.communicate()
print(f"the command fails code is {rc}")  # print error code
print(f"the output is: {out}")
print(f"Error is: {err}")
# if you need the result as list you can use splitlines
print(f"Command Reuslt in List is: {out.splitlines()}")


# recommendation is where you are working with environment variables pass command as a string and shell=True otherwise pass command as a list and shell=False
# shell=true open a shell and program is heavier and slower. so simple command pass as command as List with shell=False on Linux operating system

to obtain a list from a string command line toy can use the function split ex cmd=ls -ltr.split() result is cmd=["ls", "-ltr"]
'''


#################### Example below to find Python version on your system ########################

cmd_java=input("enter command to find python Version: ")
sp=subprocess.Popen(cmd_java,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc = sp.wait()
o,e = sp.communicate()
if rc==0:
    print(f"your result is: {o}")
else:
    print(f"your command fails with error {e}: ")






