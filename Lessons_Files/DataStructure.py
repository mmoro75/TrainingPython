############################ Data Structure ################################################

"""
Data structure is a variable that holds more than one value: ergo collection of data.
there are 4 different types in python by default ( you might have more in external modules like Arreas )

list[]
tuple()
Dictionary{} - includes value pairs
sets{}

With multiple values stored in the memory location the concept of indexes applies as per Strings

"""

# Lists - [] (list contains multiple values numeric or characters and as opposed to strings are mutable, values can be added deleted and changed)
# dir(my_list)  # list of methods for list

my_list=[3,2,"Marco",5.6,2]   #list structure
print(my_list)
print(my_list[:])      # prnt entire list
print(my_list[0:])      # prnt entire list
print(my_list[1:])     # print from index 1 to last
print(my_list[2:3])    #print list from an index to another

print(my_list[2][0])   # print list index and access specific index of internal string

my_list[0]=4           # change a list value based on index in this example on index 0 I am giving 4 value

## best practise when performing modification operation do nor print execute directly and then print the value stored in the new bariable

print(my_list[:])
print(my_list.index(2))  # to find a values  in the list and see whic index is stored ( for multiple values use indexes sub chunk)
print(my_list.index(2,1)) # in case you have similar value search from the index after in this case from index 1 to end, and you fill find the other value 2
print(my_list.count(2))  # count how many times the values is in the list

## List modifications

# my_list.clear()   # clear the entire list
my_new_list=my_list.copy()  # to create a copy of your list in another memory allocation # remember if you do x=my_list the list x will refer to same memory location
my_new_list.append(12)  # append value
print(my_new_list)

my_list.append(my_new_list)
print(my_list)            # if you append an antire list with fucntio append it create a sublist in the list to make a unique list use extend function see below


my_new_list.insert(1,55)  # insert  value 55 based on index position 2
print(my_new_list)
my_list.extend(my_new_list) # to extend to list with values from another list
print(my_list)
my_list.remove(12)   # remove a specific value in the list
print(my_list)
my_list.pop(2)       # remove value by index position in this case remove index 2 in the list
print(my_list)
print(my_list.pop(1)) ####### feature with POP if you perform pop operation with print it is also going to print out the data removed



print(my_new_list,"original")
my_new_list.reverse()   # reverse list order
print(my_new_list,"reversed")


my_new_list.sort()      # sort list in ascending order
print(my_new_list,"sorted")

print(bool(my_list))    # convert full list to boolean gives true empty list gives false
my_empty_list=[]
print(bool(my_empty_list))
print(len(my_new_list),"lenght of my list")



#Tuples - () ( tuples are immutable - operations are not permitted - only the entire data is, like delete and recreate)
# see available operations with print(dir(tuple))  as they are immutable all the insert and modify operation are not available but only count and index

my_tuple=(3,2,5,[1,2,3])  # tuple containing a list ( the list is seen as single value into a Tuple) values into the list are accessible via sub index see example
my_tuple[3][2]  # access sendo index in tuple list based on tuple indexes
print(my_tuple)

my_tuple0=()
print(bool(my_tuple0))
print(len(my_tuple),"length of my tuple ")

print(my_tuple[1:3]) # same as list print from index to etc see above list section for more example

tuple=1,3,5,6  # you can alo use this syntax to create a tuple see print out
print(tuple)
print(type(tuple))
# pay attention when defining numeric variable if you define x=1, with a come at the end it will be a tuple single value


#Dictionralies - {} they are like list mutable but the data structure consist with key value pair
# always use print(dir(dict)) to see available operations that can be performed

my_dict={"fruit":"apple","car":"ferrari",2:"two",1:1}
print(my_dict["fruit"]) # access value by key
print(my_dict.get(2))  # get value from key another syntax however if the value specified is not there you will get result None instead of error

my_dict["country"]="Italy"  # add value in dictionary based on key ( if no exist will be created if existing will be changed

print(my_dict)
print(my_dict.keys())   #print only key values type
print(my_dict.values())  #print only values type
print(my_dict.items())   #print items



x=my_dict.copy()  # create a copy in new memory location remember if you do y=my_dict it creates a copu but it will refer to same memory location
print(x)

new_dic={"name":"gino"}
my_dict.update(new_dic)  #update dictionary with another dictionary
print(my_dict)
my_dict.pop("name")  # remove key pairs value

keys=[1,2,3,4,5,6]
my_key_dic=dict.fromkeys(keys)  # create a new dictionary from keys
print(my_key_dic)



#Sets - {}  - set gives the data in ascending order and remove duplicates

my_set={8,4,5,7,8,3,3,4,2,0,3,3}
print(my_set)
new_set={9,1,3}
list=[1,7,5,3,3,4,9,2,2,9,9]
print(set(list),"set list")   # convert list into a set

print(my_set.union(new_set),"union")   # unions
print(my_set.intersection(new_set),"intersection") # intersecion

empty_Set=({})  # this is the sytax for empty set ottherwise just curly braces it will be a dictionary

##  explore more operation with print(dir(set))


