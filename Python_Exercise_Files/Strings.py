######################################### STRINGS ###########################

############################## TEST ########################

"""
Strings in python is a sequence of characters ( any character in your keyboard numbers, letters, special char ( in python even space is included be aware)

remember computer do not read characters but only numbers in form of bites
is sting is stored and manipulated by a computer by a combination of 0 and 1
python interpreter will deal with that at execution

conversion from characters to numbers is called ENCODING reverse in called DECODING
popular ones are ASCII and Unicode

in Python string is a sequence of unicode character. it was introduced to include any character in any language and bring uniformity in the encoding

"""
 ### how to create a sting ?

My_name="Marco"
My_Role='developer'

# fpr multiple lines you can use triple quotes

my_info="""I am working in LSEG
I am moving into automation
I will be sucecssfull 
"""


######## how to access characters in your string------------- IMPORTANT CONCEPT === indexes"

a="Marco Moro"
print(a)
print(a[0],a[6])  # in square bracket we specify which index to get from the string for printing

# you can do it revers by using minus numbers for indexes
# if I want to get last character is always index -1# and so on
print(a[-1])

# get from to characters # this is called slicing operation
print(a[0:5])



############################## how to change or delete a string ###########################################

# strings are immutable and once defined cannot be deleted the only way is to re-assign new value or delete it
# this applies also if you want to assign more char to string or delete some (example del a[0:2] )

del a

# length of a string
print(f"length of your string is: {len(a)}")
print(len(my_info))


# how to concatenate 2 or more strings
b="gino"
c="latino"
e=" "  #to add a space#
d=b+e+c
print(d)

################################## Srtings advanced operations ################################

# String case conversion #
a="String Convesrion"
print(a)
print(a.lower())
print(a.upper())

# print available operation for a string it can be used for other classes too
# alternately you can use help(str) including documentation or you can use python online documentation at https://docs.python.org/3.10/library/index.html
print(dir(a))



# boolean with string = remember with boolean result it will only be true or false

f="Moro"
print(f.startswith("M"))
print(f.endswith("oro"))
print(f.isspace())
print(f.islower())
print(f.isupper())


##################################### More Advanced operations with Strings ###############################################

# joints for strings
h="join"
j=" ".join(h)
print(j)


# centre give number of spaces as argument
print(h.center(40))
print(f"{h.center(20)} \n{f.center(20)}")


# Zfill for strings to add characters to your string
print(h.zfill(10))


#Strip (removes spaces left or right or any character if is start or end
y="   gino latino   "
print(y)
print(y.strip())
k="Aloahh"
print(k.strip("A"))
print(k.strip("hh"))

# Strip left or right
l="Marco Roma is not original Marco"
print(l.lstrip("Marco"))
print(l.rstrip("Marco"))

#miltiple stips
print(l.lstrip("Marco").rstrip("Marco"))

#Split it splits the string based on spaces and gives a list or splits based on given charachters
print(l.split())
print(l.split("is"))

# Count how many given characters are included in the string
print(l.count("is"))
print(l.count("M"))

#index in strings example how to work with them

print(l.index("M")) # see which index M is stored

# if you want to skip positions specify index value too for the operation

print(l.count("M",12))  # count from index 12
print(l.count("M",0))  # count from index 0
#find -1 result means value is not found in any index
print(l.find("M",12))  # find from index 12 and gives index position
print(l.find("M",0))  # find from index 0 and gives index position
print(l.find("Roma",0))  # find from index 0 and gives index position
print(l.find("x",0))  # find from index 0 and gives index position




