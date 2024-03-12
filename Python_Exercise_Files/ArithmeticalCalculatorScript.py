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

First_Number=eval(input(f"Please provide the first number to calculate: "))
if type(First_Number) not in [int,float]:    #this condition doesn't work if enter str type value. Red Error appears. How to make this step repeatable?
  print(f"The option you selected are not correct please provide 2 valid number and a correct operation you want to perform")
elif type(First_Number) in [int,float]:
  Second_Number = eval(input(f"Thank you, your first number is {float(First_Number)}\nPlease provide the second number to calculate: "))
  if type(Second_Number) not in [int,float]: #this condition doesn't work if enter str type value. Red Error appears. How to make this step repeatable?
    print(f"The option you selected are not correct please provide 2 valid number and a correct operation you want to perform")
  elif type(Second_Number) in [int,float]:
    Operation = (input(f"Thank you, your second number is {float(Second_Number)}.\nPossible operations with selected valuses are:\n(+) adding\n(-) substruction\n(*) multiplication\n(/)division\nWhich operation would you like to perform?: "))
    if Operation == "+":
      Result_adding=(First_Number + Second_Number)
      print(f"The result for adding is = {Result_adding}")
    elif Operation == "-":
      Result_substruction= (First_Number - Second_Number)
      print(f"The result for substruction is = {Result_substruction}")
    elif Operation == "*":
      Result_multiplication= (First_Number * Second_Number)
      print(f"The result for multiplication is = {Result_multiplication}")
    elif Operation == "/":
      Result_division= (First_Number / Second_Number)
      print(f"The result for substruction is = {Result_division}")
    else:
      print(f"The option you selected are not correct please provide 2 valid number and a correct operation you want to perform")