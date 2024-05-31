
import os
import sys
import datetime

path=input("please enter your path: ")
age = int(input("provide number of days you want the file to be older from: "))

if not os.path.exists(path):
    print("please provide a valid path: ")
    sys.exit(1)
if os.path.isfile(path):
    print("please provide a directory path: ")
    sys.exit(2)

today = datetime.datetime.now() #  create today date as reference for the loop

for file in os.listdir(path):  # use for loop to get all files in given path
    each_file_path=os.path.join(path,file)  # use joint between given path and file to obtain a complete path ( meaning path+file)
    if os.path.isfile(each_file_path):  # use conditional statement to only get actual files ( not folders too)
       file_creation_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))  # combine os getctime to find out creation time for the file and use dateime fromtimestamp to convert to date
        #print(each_file_path,today - file_creation_date)  # get number of days from when files were created printed
        # print(each_file_path, (today - file_creation_date).days) # print only days when they were created not all date by using the function days
       dif_days = (today - file_creation_date).days  # create the variable to use for the diff
       if dif_days > age:  # now using the conditional statement we are just printing the files older than number of days from the counter
          print(each_file_path,dif_days) # print only the files older than given age