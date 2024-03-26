## given the below list:

numbers=[1,2,4,5,6,7,8,11,14,15,17,18,20]
new_list=[]
# using the for loop and the conditional statement create a new list empty list and include only the even numbers in it

for n in numbers:
    if n%2==0:
        new_list.append(n)
print(new_list)

### given the below counter with the help of  while loop that print odd number to 300

count=3
while count<=300:
    print(count)
    count=count+2

## think caefully how to increase the count value in the loop to get only the odd numbers

count=3
while count<=300:
    if count%2==0:
        print(count)
    count=count+1

