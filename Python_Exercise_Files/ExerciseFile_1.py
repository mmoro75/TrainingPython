                            ############### STRING EXERCIE #############################
# given the belo string
A="Marco and Iryna are doing Python Training together"

# store your name in "MyName" string and print it out
MyName="Iryna Herasymchuk"
print(MyName)
# store first and last digit of A string in another string "B" and print on screen
B=(A[0],A[-1])
print(B)
# try to obtain the length of string A and print on screen
print(len(A))
# convert A string all in UPPER CASE store in string C and print
C=str.upper(A)
print(C)
# with boolean operation check if the C string is UPPER CASE verify the result should be now false
print(C.islower())
print(C.isupper())
#with boolean check is string is ending with er veryfy the result is TRUE
print(A.endswith("er"))
# count how mant letters o are in string A and print on screen
print(A.count("o"))
# given the RIC
RIC="![VOD.L"

# strip the mangling store the value in string RIC and print
print(RIC.lstrip("!["))
# use the command print(dir(A)) explore some more functions/methods for Strings and on teams tell me one that you think it might be very useful in the future for our scripts
print(dir(A))
## if needed rememeber to use print(help(str) or visit the pyhton documentation website https://docs.python.org/3.10/library/index.html

"""
досліджуйте, вчіться, розважайтеся, насолоджуйтесь, захоплюйтесь і, найголовніше, якщо щось нелегко, 
як здається, НЕ ПАНІКУЙТЕ, я тут, щоб допомогти!

"""



####################################### INPUT OUTPUT  EXERCISE#######################

# ask the user to provide a value for variable x in integer
x=int(input("what is the value of x: "))
# ask the user to provide a value for varibale y in integer
y=int(input("what is the value of y: "))
# declare varibale C and sum x+y and print
C=x+y
print(f"if you have {x} and {y} added together the value is {C}")
# ask the user to provide a value for variable Name in string
Name=input("What is your name? ")
# ask the user to provide a value for varibale Surname in string
Surname=input("What is your surname? ")
# print out with the help of format f in 2 separate rows  my name is: given name and my surname is: given surname
print(f"my name is {Name} \nand my surname is {Surname}")



