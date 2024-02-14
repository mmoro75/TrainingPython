                        ###  Data Types ########

# numeric = int,float,complex

x=1
print(type(x))
y=2.5
print(type(y))

# alphaberic = str

my_name="Marco"
print(type(my_name))

# true or false - boolean

x=True
t=False

print(x,type(x))
print(t),type(t)




# how to convert data type

h=56
print(type(h))

p=str(h)
print(type(p))

print(int(y),type(y))
#print(int(z),type(z))

""" 
remember you can convert number to string but not the other way round
int to float. or numeric to str
 Variable can be converted all to boolean ,
 bool(any_data)=True
 bool(empty) false
 bool(non_empty) True
"""
j=2
f=0
l=None
o=[]   # this is a list
d=()   # this is a tuple
v={}   # this is a dictionary

# list, Tuple and Dictionary will be covered later

print(bool(j))
print(bool(f))
print(bool(l))
print(bool(o))
print(bool(d))
print(bool(v))
''' 'you can find memory location for your varibale if needed

print(id(my_name))

'''



##################################  Multiple Variables in Print ##########################################

# define variables in multiple line or single line ( same apply for printing)

x=1
y=2.5
My_Name="marco"

print(x)
print(y)
print(My_Name)

"""
x=1,y=2.5,My_name="marco"
print(x,y,My_Name)


"""

print(x,y,My_Name)
print("{} {} {}".format(y,x,My_Name)) # The format operator, % allows us to construct strings, replacing parts of the strings with the data stored in variables
print(f"the value of x is: {x} the value of y is: {y} my name is: {My_Name}")  # lets' write this in new lines

