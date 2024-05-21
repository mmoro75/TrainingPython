################# Given the txt file ExecricseFile_4.txt in GIT #################################

"""
1)open the file and read the entire content and print tha on the screen

fo=open("C:\\Test\\Files\\ExecricseFile_4.txt","r")
print(fo.read())
fo.close()

2) with the help of for loop read the entire file and print on the screen only lines with at least 3 # , "###"

fo=open("C:\\Test\\Files\\ExecricseFile_4.txt","r")
file_lines=fo.readlines()
for each in file_lines:
    if "###" in each:
        print(each)
fo.close()

3) with the help of for loop try to read the file ExecricseFile_4.txt and write on a new file "Result.txt" only line with at least 3 * , "***"

source_file=open("C:\\Test\\Files\\ExecricseFile_4.txt","r")
source_content=source_file.readlines()
source_file.close()

dest_file=open("C:\\Test\\Files\\Result.txt","w")
for each in source_content:
    if "###" in each:
        dest_file.write(each)
dest_file.close()

"""


############################### Given the csv file OMXINET01_20240304.csv in GIT #################################################

"""
1) open the csv file read the content and with the help of for loop print on the screen only result for RIC == "BLKGA.COf" 

import csv
my_csv="C:\\Test\\Files\\OMXINET01_20240304.csv"
fo=open(my_csv,"r")
content=csv.reader(fo)
for each in content:
    if "BLKGA.COf" in each:
        print(each)
fo.close()

"""

###################################### Given the json file lsegtp01.json in GIT #######################################

"""
1) open the file and print the content on the screen 

import json
myfile="C:\\Test\\Files\\lsegtp01.json"
fo=open(myfile,"r")
print(json.load(fo))
fo.close()

2) generate a json file named "Employee.json" with the below parameters 

my_dictionary={"name":"Iryna","skills":"[aws,python,qa,Kubernetes,Atlas,]","office":"home","Location":"Kiev","company":"Luxsoft","Goals":"[python,English,Confidence]"}

provide indentation as well for correct json format

myfile2="C:Test\\Files\\Employee.json"
my_dictionary={"name":"Iryna","skills":"[aws,python,qa,Kubernetes,Atlas,]","office":"home","Location":"Kiev","company":"Luxsoft","Goals":"[python,English,Confidence]"}
fo=open(myfile2,"w")
json.dump(my_dictionary,fo,indent=4)
fo.close()

"""