### STEP -1 = Please include the following script into a function and call the function to execute the script

prompt=input("Please enter your string: ")
action=input("how would you like to display your string : upper/lower or title format?")

if action=="upper":
    print(action.upper())
elif action=="lower":
    print(action.lower())
elif action=="title":
    print(action.title())
else:
    print("please enter a valid action upper/lower or title")


## STEP 2 = using the same script collect the information from user outside the function, give the variable action a default value of "upper" and call the  function to execute the script


## STEP 3 = again using the same script please create a main function  to collect info from user and call the second function to execute the logic into the main function
## passing the relevant arguments for the second function to execute..   ( please remember to call the main function to start the script


## when running step 2 and 3 please remember the global variable concept and how to pass the argument into the function when is required both when you define and when calling the function