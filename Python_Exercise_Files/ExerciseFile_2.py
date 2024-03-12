
### given the below list ####################

My_Shopping=["apple","avocados","eggs","rice","bread","sweets","tomatoes","salad","ice cream"]

# create another list with only the last 3 items
My_Shopping_New=My_Shopping[-3:].copy()
print(My_Shopping_New)
# remove the unhealthy sweets and include nuts :)
My_Shopping[5]="nuts"
print(My_Shopping)
# print how many items are listed in the shopping list
print(len(My_Shopping))
# copy My_shopping into another list called My_NextShopping
My_NextShopping=My_Shopping.copy()
print(My_NextShopping)
# add 2 more items at your choice into My_NextShopping list
IrynasWishes=("olive oil","fish")
My_NextShopping.extend(IrynasWishes)
print(My_NextShopping)
# with the help of print(dir(list)), print(dir(tuple) and the documentation explore few more options at your choice
print(dir(list))
print(dir(tuple))

if My_NextShopping.__contains__("fish"and"olive oil"):
    print("My_NextShopping contains all Iryna's wishes :)")
elif My_NextShopping.__contains__("fish"or"olive oil"):
    print("My_NextShopping contains some Iryna's wishes")
else:
    print("My_NextShopping doesn't contain Iryna's wishes")

############   given the below Dictionary ##########################################

My_Items={"food":"bread","tool":"hammer","main":"rice","sportCar":"ferrari","utensil":"nail","car":"Lamborghini","fruit":"banana","city":"London","color":"orange"}
# print only key values type
print(My_Items.keys())
# print only values type
print(My_Items.values())
# print all the items
print(My_Items.items())

# copy My_Items dictionary into My_NewItems dictionary
My_NewItems=My_Items.copy()
print(My_NewItems)

# pop out all the cars from My_NewItems
My_NewItems.pop("sportCar")
My_NewItems.pop("car")
print(My_NewItems)

# with the help of print(dir(dict)), print(dir(set))  and the documentation explore few more options at your choice
print(dir(dict))
print(dir(set))

######################################## Operators ###################################################
# given the below false condition change it to make it print True
print(3>4 and 1 in [1,2,3], "\"original\"")
print(3>4 or 1 in [1,2,3], "changed to true")
print(3<4 and 1 in [1,2,3], "\"changedto true\"")
print(3!=4 and 1 in [1,2,3], "\"changed to true\"")
# given the below true condition change it to make it print false
print(3>4 or 1 in [1,2,3], "\"original\"")
print(3>4 and 1 in [1,2,3], "\"changed to false\"")
# given the below true condition change it to make it print false
print(all([2<3,4<5,5<6,6<7,7<8]), "\"original\"")
print(not all([2<3,4<5,5<6,6<7,7<8]), "\"changed to false\"")
# given the below true condition change it to make it print false
print(any([2<3,4<5,5<6,6<7,7<8]), "\"original\"")
print(not any([2<3,4<5,5<6,6<7,7<8]), "\"changed to false\"")
print(not all([2<3,4<5,5<6,6<7,7<8]), "\"changed to false\"")