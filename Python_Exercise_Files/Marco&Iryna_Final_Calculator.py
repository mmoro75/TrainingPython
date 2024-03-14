

while True:
  try:
     a = eval(input("Provide the first number: "))
     if type(a) not in [int, float] :
         print("Not valid type of value. \nOnly int or float can be used.")
     else:
        a = float(a)
        break
  except NameError:
         print("Not valid type of value. \nOnly int or float can be used.")
         continue

while True:
  try:
     b = eval(input("Provide the second number: "))
     if type(b) not in [int, float]:
         print("Not valid type of value. \nOnly int or float can be used.")
     else:
         b = float(b)
         break
  except NameError:
         print("Not valid type of value. \nOnly int or float can be used.")
         continue


while True:
    R = input("Provide the operation: ")
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