################################### OS MODULE ####################################################################
"""
with the help of OS module allows you to interact with your operating system and automate tasks like create/remove directory and more
it works both with windows and linux
"""

############################################### OS ###################################################################

import os  # OS module as always has to be imported first

# print(dir(os)) -  available functions
# print(help(os)) -  documentation

print(os.getcwd()) # get current work directory
os.chdir("c:\\Users\\u6017127") # change directory remember in windows always remember to use "\\ separator" for paths ( remember python special characters some \n \u in previous lesson?)
print(os.getcwd()) # print new location
os.chdir("c:\\Users\\u6017127\\PycharmProjects\\AutomationTraining.py\\venv")

print(os.sep)  ## this variable very important gives you separator value remember if you are windows is "\" if you are linux is "/"

print(os.listdir())  # print list directory output is a list ( remember this in case the values have to be re-used)
# print (os.listdir(path)) you can provide path is required
# os.mkdir("c:\\Users\\u6017127\\Documents\\new_folder") # create directory
# os.rmdir("c:\\Users\\u6017127\\Documents\\New_Folder1") # remove directory
# s.makedirs("c:\\Users\\u6017127\\Documents\\New_folder2\\New_SubFolder")  # create directory and subdirectory
# os.removedirs("c:\\Users\\u6017127\\Documents\\New_folder2\\New_SubFolder") # remove directory and subdirectory
# os.rename(source, destination) to rename a file
#print(os.environ) # get environment info
# print(os.getuid())  # get user id
print(os.getpid())  # get process id

#################################### OS.PATH ###########################################################
#
# this submodule of the OS module and it is used to work with paths

# print(dir(os.path))  ## List all the available functions for this submodule


print(os.path.sep) # separator for your operating system
path="c:\\Users\\u6017127\\PycharmProjects\\AutomationTraining.py\\venv"
print(os.path.basename(path)) #basename last part of your path
print(os.path.dirname(path))  # path name till basename
# os.path.join(path1,path2) to join 2 paths together ( paths are stings you can indeed add 2 strings together with + buy uou won't get the separator automatcally hence this function can turn to be useful)
print(os.path.split(path)) # get path head and tail ina tuple try tu run it and see the output
print(os.path.getsize(path))
print(os.path.exists(path)) # to see if exist result in boolean
print(os.path.isdir(path))  # see if path is a directory result in boolean
print(os.path.isfile(path)) # see if ptah is a file result in boolean
print(os.path.islink(path)) # to check if it is a link or not result in boolean

###################################################### OS.System ##############################################
#
# with OS.System function you can execute operating system commands ( very useful )

# despite some commands for your Operating system are already included in OS module  like make dir , change dir etc not all of them are available therefore
# the OS.System function can be very useful fir wide range cf commands


print(os.system("dir")) # the output will be displayed on the screen alongside execution code 0=command successful any other code menas command failed

# if you assign the execution to a variable only execution result will be stored, and you can determine if the result is good or not

cmd_res=os.system("dir")      # in this example the command is executed

if cmd_res ==0:
    print("your command is executed ")
else:
    print("Your command failed")




########################################################## OS.WALK######################################
#
# the os.walk(path) function it is used to generate file and directory in a directory tree by walking
# ( for example find a file it will find on given path and all subdirectory )

path1="C:\\Users\\U6017127\\OneDrive - London Stock Exchange Group\\Documents\\Eikon\\Project\\Test"  # to try this first identify a path pn your machine first that you want to navigate
print(list(os.walk(path1)))   ## os.walk generate list first then item in the given path in tuples

# the values in tuple are always 1) your path , 2) directory in the given path 3) files in the given directory
'''
to understand the concept we are going to generate a list for the given path
 result will give a list containing a tuple the tuple contains 3 values each value is a lists: 
 1) your path 
 2) list of direcotries in your path 
 3) list of files in your direcotry
 
 for each sub directory for the given path it would generate another tuple with same values 
 and so on to cover up all the directory and files
'''

################ separate the tuples with a for loop ############################################

print("---------------------------------------")

for each in os.walk(path1):
    print(each)       # result would separate tuples and give it in separate lines ( see output )

############################  Separate List in the given path using loop ##########################


for root,dir,files in os.walk(path1):
    if len(path1) !=0: #  to exclude empty paths if needed to get only internal data
      # print(root,files)  # I am separating roor path and files in 2 variables and print them
      print(files) # print just files


########################## To get list of files in the given path #########################################


for root, dir, files in os.walk(path1):
    if len(path1) != 0:  # to exclude empty paths if needed to get only internal data
        #print(root,files)   # If needed you can also separate root path and files in 2 variables and print them
        print(f"see list of files in {path1}")
        print(files)  # print just files

# additionally you can reconstruct the path for each file by using for loop
# ( this can be very useful for generating scrips when entire path is needed )

for root,dir,files in os.walk(path1):
    for each_file in files:
        print("See list of files with root path included")
        print(os.path.join(root,each_file))  # now print root and each file associated by using joint function