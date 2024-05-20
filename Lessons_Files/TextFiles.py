########################################### TXT FILES ############################################################

# payton allows you to work with text files to read , write from ant to files.txt

"""
Generally when working with files you have 3 options:
1) Create a new File
2) Add Content to an existing file
3) Read content from existing file

On your operating system you create a new file or open an existing file you always are in read/write mode automatically
with command line or python scripting that is not possible so you have to specify read or write more when intercating with a file

open ----> W ( write mode)  === Existing file or to create a new file
open ----> a ( append mode ) === Existing file
opep ----> r ( Read mode )   ==== Exitsting file

"""

# create new file - remember whenever you open a file in write mode the data will always be created from 0 (cursor position top left)
# text can be included in write mode based on cursor position

fo=open("C:\\Test\\test_file.txt","w")  # to create a file specify location and file name then you need to use w=write mode ( empty file created)

### important every time you open a file after the cations needed file has to be close
# fo.close()  # close will save the file automatically


print(fo.mode) # to print in which mode your file is open w=write, a=append, r=read
print(fo.readable()) # boolean result in this case it is False as the file is open in writing mode
print(fo.writable()) # boolean True in this case as we opened write mode

## Important to read and write or append in a file is always important the cursor position see examples below #####

fo.write("this is a test file first line\n") # to write content in your file  ( cursor position start from 1st line position 0)
     #to go to next line \n ( otherwise you will stay  on same line)
fo.write("New content in second line\n") #
fo.write("New content in third line")
fo.close()  # close will save the file automatically

### Remember every time you close the file if you re-run the code above everything will be overwritten it basically creates a new file from 0 #####

my_content=["test 1\n","test 2\n","test 3"]
fo=open("C:\\Test\\Files\\list file.txt","w")
fo.writelines(my_content)  # I can use a list to write my content in file with writelines function
fo.close()

my_content=["test 1","test 2","test 3"]
fo=open("C:\\Test\\Files\\loop_file.txt","w")
for each_line in my_content:
   fo.write(each_line+ "\n")  # I am passing the \n in the loop iterations, so it can write in my file each line
fo.close()

# add content to file ( open file in a mode a= append) it won't disrupt existing data it will add data at the end
# note append mode and write mode if file is not there are same but if file already exist (if it doesn't exist append cannot be used)
my_content=["test 1\n","test 2\n","test 3"]
fo=open("C:\\Test\\Files\\loop_file.txt","a")  # im append mode you will include the data from existing file
for each_line in my_content:
   fo.write(each_line+ "n")  # I can use loop to write in my file each line
fo.close()

# read content from file ( open in r mode r=read)
fo=open("C:\\Test\\Files\\loop_file.txt","r")
print(fo.read()) # to read data in your file
file_content=fo.read() # store the content in a variable
fo.close()

print(file_content) # now the data it is stored in the variable even if the file is closed, and it can be re-used

# you can also read line by line using function fo.readline() but it is no so efficient if you have multilple line you can instead use
# fo.readlines() and get the data in a list by then you can use a loop to print all the lines see example below:

# read line each line using loop
fo=open("C:\\Test\\Files\\loop_file","r")
file_lines=fo.readlines() # you will get list of content in your file ( each line a new element in the list
# now with for loop I want to read first 2 lines I am using index
for each in range(2): # I am using range function in the loop to give number of iterations
    print(file_lines[each])  # I am using variable each to read index in file lines ( remember file_lines is a list)
fo.close()


#### copy content from a file and copy to a new file ###############

source_file=open("C:\\Test\\Files\\sourceFile.txt","r") # open in read mode to get the content
source_content=source_file.read()  # read content from source file and storein cource content variable
source_file.close()

dest_file=open("C:\\Test\\Files\\myDest_File.txt","w")  # open in write mode to copy the data from source
dest_file.write(source_content) # write content from source file into dest file
dest_file.close()

""" 
if would be good to give provide path from sorce adn destination to be clear where you want to pick up and save the files
default location is where you are running the script

path_file=open("c:\\path.txt","w") # safe option is to provide complete path always to avoid mistakes

remmeber if you do not provide any mode the default is read mode for a file
"""

################## useful function to open a generated file on screen automatically ################################

filename="C:\\Test\\test_file.txt"
os.startfile(filename)
