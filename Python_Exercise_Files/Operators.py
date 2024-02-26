######################################## OPERATORS #######################################################

"""
Waht is an operator?
In mathematics and computer programming, an operator is a character that represents a specific mathematical or logical action or process.
operators are placed in between operands to perform the action
operands can be either values, variable or combination of varibale and values

a = 1 + 1
b = a + 1
c = a + b

"""

# Arithmatic and Assignment Operators -
# these operators get input and output as a value
'''
+ - addition operator
- - minus operatior
* - moltiplication operator
/ - division operator
%  - modulo operator - gives the reminder for the operation
// - floor division ( rounds the number divided )
** - power of  operaror exponenatial
=  - assign operator
'''

# #Comparison , Identity and Membership Operators -
# these operators get input value but the output will be in boolean "True or False"

'''
> - greater than 
< - less than 
== - equal 
!= - noteqal 
>= -  greater or equal to
<= - less or equal to 
'''

# to compare strings find out the ASCII code assigned to each letter with "ord("any-character") or "chr("any-value")
# it then compares character by charter for the given strings



print(ord("a"))    # get ascii value for sting a
print(ord("b"))    # get ascii value for string b

print(chr(97))    #  with char function you convert the number value to obtain letter 97 is a
print(chr(98))    # 98 is b

print("a" < "b")    # ascii value for a is 97 and b 98 therefore this result is true
print("abc" < "acc")  # in this case comparison char bu char first ia a and it is equal but second b is < than c therefore result is trues



#~~~~~~~ Identity and Membership  operators ~~~~~~~~~~~~~~#
# these operators get input as Boolean and output boolean too " true or false"

#identity  is used to find type of variable Class/object/type

# the available operators are: "is" and "is not"

x=6.5
print(type(x))
y="marco"
print(type(y))

print(type(x) is type(y))
print(type(x) is not type(y))

# Membership operators are to validate the membership of a value
# basically tells you if a value is present or not

a=[1,2,3,5,6,7,8,8]
print(5 in a)    # this is true because 5 is in list a
print(10 in a)   # this is false because 10 in not in the list

## se example below for more real scenario

Ric_list=["VOD.L","CARL.L","BARK.L","GOL.L"]
your_ric=input("please provide ric value you are looking in the list: ")

if your_ric in Ric_list:
     print(f"RIC {your_ric} has been found in the list")
else:
     print(" your given RIC"" is not in the list ")

# other available option for membership operators is "not in" to evaluate



#------------------------------- Logical Operators -----------------------------#

# these operators are useful to combine multiple conditions see examples below - results are always boolean True or False
"""
available options are 
- and
- or 
- not
"""

print(3>4 and 1 in [1,2,3])  # with option "and" both the conditions have to be true

print(3>4 or 1 in [1,2,3])  # with option "or" at least one condition has to be true

# Not operators reverse the condition False to True and True to False see examples:
print(not 1 in [1,2,3]) # option "not" for true will give false result
print(not 4 in [1,2,3]) # option "not" of false will give true

### combining operators option = "all " and "any" and "not all" and "not any" see examples below:

# with all option it is true if all conditions are True otherwise it is False
# with any as long as one condition is ture result is True otherwise it is False

print(all([2<3,4<5,5<6,6<7,7<8]),"all is true") # with all you can club all the conditions together without repeating and operator
print(any([2<3,4<5,5<6,6<7,7<8]),"all is true") # with any you can club all the conditions together without repeating or operator

print(not all([2<3,4<5,5<6,6<7,7<8]),"all is true")
print(not any([2<3,4<5,5<6,6<7,7<8]),"all is true")