#################################### WHILE LOOP ##############################################################

# while loop it is useful to repeat until a condition is true and then stop when condition is false
'''
while True:
    print("monitor the machine")  # this is an example of infinite loop as the condition for while is always true
'''

# we generally use while loop when we do not know beforehand how many times we have to iterate


while true:
    print("infinite iterations")     # whith while loop you can write an infinie loop
    print("----------------------")   # a real life example of infinite loop for example if you want to monitor server performance you are going to run the code infinite number of time


# now we want to see scenarios where we need to stop by using while
value=10  # this value stands ad a counter for the number of times we want the loop to run
while value<=100:  # loop will stop once get to 100
    print(value)
    value=value+2  #increase value by 2 each iteration to increase the counter

####################################### LOOP CONTROL STATEMENTS ########################################################################
############ while and for loop === statements: = continue,break and pass ##################################################

           ##################################### BREAK #########################

for each_value in [1,2,3,4,5]:
    print(each_value)
    break # when break is found will stop your loop ( in this example you are getting only 1 iteration)

##### Note stopping a loop with break statement it only means getting out of the loop not the entire python script

for each_value in [1,2,3,4,5]:
    print(each_value)
    if each_value==3:
        break # break will stop your loop ( in this example you are stopping when getting value 3)
        #once your condition is true the loop will stop and won't iterate fully as it is not needed

        ########################### Continue ##############################

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for each_number in numbers:
    if each_number==7:
        print("---------------------------------------------------------")
        print("I Am standing before continue iterantion 7 not executed")
        continue     # if the above condition is true the remaining block of code in the if condition is skipped and only code outside the continue blok are executed
        print("next number")   # the remaning line in this iteration are not executed they will continue from 8 to 15
        print("I am not going to be executed")
    print("----------------------------------")
    print(f"this is iteration number = {each_number}") # statement is outside the if condition and will be executed every iteration

                  ############################ PASS  ##########################
 # pass will simply skip where you are supposed to get an error

while True:
    pass  # no error is displays but simplu pass ( block of code was expected )

numbers=[1,2,3,4,5,6,7,8,9,10]

for n in numbers:   # you should get an error try to comment out pass and see what happens
    # pass
print("now I am executed")