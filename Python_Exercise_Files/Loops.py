                ##################### LOOPS #####################################

# Loops are useful to execute block of codes many times ( all programming language needs that it is a fundamental procedure)
# for loop will iterate for the number of time for the given value

"""
for "any variable" in "value" *** values can be any from list,Tuple, Dictionary, (Even text files, EXL files and Json Files) 
total number of iterations depends on number of indexes in the stored variable 
"""

MyList=[1,2,4,5,6,7,8,9,10]
# syntax of for loop = "for" determine the type of loop, "n" is a variable that stores the value for the given main Variable for each iteration, in " variable you want to iterate"
for n in MyList:
    print(n)


# use for loop to print a string and corresponding index
string=input("provide a string: ")
index=0 # give a reference value for your variable in the loop to take at first iteration == (this variable has to be defined before the loop of defined into the loop it gets reset each iteration and loose its purpose)
for each in string:
 #   print(each.index(each))
    print(each,"--->",index)
    index=index+1  # increase index number +1 every iteration


# for loops with Dictionary, tuple, list

tu_list=[(1,2),(4,5),(8,9)]   # list contains tuple as values ( it could also be a list containing other lists)

for each_value in tu_list:
    print(each_value)   # with this loop you are unpacking the list and variable each value will get the tuple

for fr,sd in tu_list:  # by assigning 2 variables in the for loop you can unpack the tuple values and print them out separately
    print(fr)  # print only first value of tuple
print("-------------------------")
for fr,sd in tu_list:
    print(sd)  # print second value of tuple

#this scenario is very important when working with disctionary

my_dic={0:1,2:3,4:"m"}

for each_item in my_dic:
    print(each_item)  # in this scenrio with a single variable you are going to get only key values ofyour dictionary

for key,value in my_dic.items():
    print(key,value)  # with 2 variables you can get key and value in your dictionary ( or print them separatley)
