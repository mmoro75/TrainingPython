"""
Welcome to the first and not last challenge for this training course
we are now going to develop the first python script by using some logic we have learned so far

---------------  Arithmetical Calculator Requirements ----------------------------------

- With the help of input function - operators and conditional statement we want the following

1) ask the user to provide first number ( either integer or float )
2) ask the user to provide second number ( either integer or float )
3) ask the user which arithmetical operation wants to perform giving the options + , - , * or /
4) with the help of operators and conditional statement perform the arithmetical operation and numbers selected by the user  and
   with the help of format print statement "the result for your 'option selected' is = "
5) if the user enter a wrong option print "the option you selected are not correct please provide 2 valid number and a correct operation you want to perform"


"""

"""
Не бійтеся робити помилки. всі це роблять. ми стаємо кращими людьми, лише роблячи це та навчаючись у них.

ТИ МОЖЕШ ЦЕ ЗРОБИТИ !!!!
"""


# tip : if you are not getting the desired results remember to use the "print" function to monitor the progress of variables in your script
# if it crashes see the error from the console and try to fix it 

while True:
    a = eval(input("Provide the first number: "))
    if type(a) not in [int, float] :
        print("Not valid type of value. \nOnly int or float can be used.")
    else:
        a = float(a)
        break

while True:
    b = eval(input("Provide the second number: "))
    if type(b) not in [int, float]:
        print("Not valid type of value. \nOnly int or float can be used.")
    else:
        b = float(b)
        break

while True:
    R = input("Provide the operation: ")  # eval not needed when user enter a string ##
    if R not in ["+","-","*","/"]:
        print(f"Available operations are: +, -, *, /")
    elif R == "+":
        R = a + b
        print(f"Addition result is {R}")
        break
    elif R == "-":
        R = a - b
        print(f"Substraction result is {R}")
        break
    elif R == "*":
        R = a * b
        print(f"Multiplication result is {R}")
        break
    else:
        R = a / b
        print(f"Division result is {R}")
        break