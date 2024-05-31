
####################################### Windows ##############################################################
import os
import string

req_file=input("please enter filename you want to search: ")
sys_path="C:\\"  # I am just looking in C: drive in Windows
for root,dir,files in os.walk(sys_path):  # i am separating with walk root, dir and files
    for each_file in files:       # I want to print each file for the given path ( system path for this requirements)
        if each_file==req_file:  # if statement to print just given file
          print(os.path.join(root,each_file))  #print given file with his path and each file associated by using joint function



"""
in case there are more drive in your windows you can use the code below and include that in your script for the entire systsm including other partitions

import os  # import os Module to serch paths
import string  # import string module for Capital letter in alphabet

systempath=string.ascii_uppercase   
Drives=[]  # create ampty list to collect available drives
for drive in systempath:   
      if os.path.exists(drive+":\\"):   # if path exist in the list of systemptah letters it will be printed and included in the empty Drivers list
          print("valid drives in your system are: ")
          print(drive)     # print the available drive 
          Drives.append(drive)  # now include the existing drive in your systme into the list that can be eventually be used in the main scrip for looping

print(Drives)

"""




##########################################LINUX #########################################################################################

import os
req_file=input("please enter filename you want to search: ")
sys_path="/"  # entire drive for Linus is "/"
for root,dir,files in os.walk(sys_path):  # i am separating with walk root, dir and files
    for each_file in files:       # I want to print each file for the given path ( system path for this requirements)
        if each_file==req_file:  # if statement to print just given file
          print(os.path.join(root,each_file))  #print given file with his path and each file associated by using joint function