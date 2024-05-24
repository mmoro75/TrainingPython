### STEP -1 = Please include the following script into a function and call the function to execute the script

def format():
    prompt=input("Please enter your string: ")
    action=input("how would you like to display your string : upper/lower or title format?")
    if action=="upper":
        print(prompt.upper())
    elif action=="lower":
        print(prompt.lower())
    elif action=="title":
        print(prompt.title())
    else:
        print("please enter a valid action upper/lower or title")
    return None
format()


## STEP 2 = using the same script collect the information from user outside the function, give the variable action a default value of "upper" and call the  function to execute the script

prompt = input("Please enter your string: ")
def format(action="upper"):
    if action == "upper":
        print(prompt.upper())
    elif action == "lower":
        print(prompt.lower())
    elif action == "title":
        print(prompt.title())
    else:
        print("please enter a valid action upper/lower or title")
    return None
format()

## STEP 3 = again using the same script please create a main function  to collect info from user and call the second function to execute the logic into the main function
## passing the relevant arguments for the second function to execute..   ( please remember to call the main function to start the script

def format(value):
    action = input("how would you like to display your string : upper/lower or title format?")
    if action == "upper":
        print(value.upper())
    elif action == "lower":
        print(value.lower())
    elif action == "title":
        print(value.title())
    else:
        print("please enter a valid action upper/lower or title")
    return None
def main():
    prompt = input("Please enter your string: ")
    return format(prompt)
main()

## when running step 2 and 3 please remember the global variable concept and how to pass the argument into the function when is required both when you define and when calling the function