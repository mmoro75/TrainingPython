#################################### REGULAR EXPRESSION ######################################################################

'''
--regEx or regular expression is a procedure to look for a specific pattern in a given text
--pattern is a sequence of charters that represent multiple strings
    examples
       "i[st]" -----> in regular expression: is, it
       "python[23]' -----> in regular expression: Python2, python3

       string = "pythons is simple and it is easy
       string.split("is")
       string.split("it")

       what if I want to split both at the same time?

       import re
       re.split("i[st]",string)


'''

import re # first af all to use regular expression you have to import default module re

print(dir(re)) # see all the available functions with this module
# print(help(re)) # for help and documentation

############################ Rules to Create a pattern ######################################44
'''
syntax to use module re 

re.search(pattern,text)
re.match(pattern,text)
re.finditer(pattern,text)
re.finditer(pattern,text)

to perform the operation we always use pattern for the given text now let's see some rule to build pattern 

- pattern is sequence of character which represent multiple strings
'''

text="this is python and it is very easy to learn"
patt1="is"
print(re.findall(patt1,text)) # find all will find all the string is in your text
print(len(re.findall(patt1,text))) # will give how many times is there

patt2="i[st]"  # I am building a pattern to find is, and it sees that we take common letter i and in [] we include st to make the combinations
print(re.findall(patt2,text))

################## Rules to create patterns ############################################
# a,x,9,@ -> ordinary character match themselves
# [abc] -> match a or b or c
# [a-d] -> match letter from (a to d) ( sequential can be abbreviated with -) example 2: [a-dm-px-z] match letter from (a tod), (m to p) and (x to z)
# [a-zA-Z0-9] -> match [a to z] [A to Z] and [0 to 9]
# \w -> match any letter ( capital and lower letter), digit or underscore
# \w\w -> means we are going to search string with 2 char any combination and so on with \w\w\w string 3 letters ect ect
# \W -> match all the characters not included in \w
# \d -> match 0-9 decimal digits ( can be used in combination like python\d = serach for any version of python1-9) or \d\d -> 2 digits
# . -> match any single character except new line character ( .. -> 2 char , ... -> 3 char and so on)
   # p.s  to match char dot only the syntax is "\."

# example find the ip address in my text

ip_text="my server ip for EMEA is 127.245.789.188"
patt3="\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"  # find 3 digits and dot in given text ( \. to match dot not all char)
print(re.findall(patt3,ip_text))

############################# Advanced Rules for Patterns ############################

# ^ -> start of-the string ( start of the lines in case of multiple strings)
# $ -> end of-the string ( and newline character in case of multiple strings "like in a file")
# \b -> empty string beginning or end of a word
# \B -> empty string not at beginning or end of-the word
# \t \n \r -> match respectively tab, newline , return
text2="it is a wonderful day hope it stays the same_its hot"
patt4="^i[st]"  # it will search for it or is only at the beginning of the string
print(re.findall(patt4,text2))

patt5=r"\bit" # the r will skip the python special character so \b will be treated as space in regular expression. with r it search for pattern beginning with spaces
# if you want to search for the exact word hope for example rule is "\bhope\b"
print(re.findall(patt5,text2))

################## more advanced rules ########################

# {2} -> exactly 2 times ( or more you can use it to find sequential same characters
# {2,4} -> 2 times or 3 times or 4 times
# {2,} -> 2 or more number of times
# + -> one or more
# * -> 0 or more times
# ? -> once or none ( example in ax?z = axz or az )

seq_text="this is aaaa for bbb"
patt6=r"a{4}"  # look for 4 seq a
print(re.findall(patt6,seq_text))


################################ rules to create pattern with Flags #########################

# re.I -> IGNORECASE makes regular expression not case-sensitive -> full re.IGNORECASE)
# re.M -> MULTILINE ( useful when working with files ) -> full re.MULTILINE
# re.L -> LOCALE ( dependent on local languages ) -> full re.LOCALE
# re.S -> DOTALL ( th dot will match every char plus new line )
# re.U -> UNICODE ( dependant on unicode character mode )
# re.X -> VERBOSE ( i.e whitespace will be ignored )

new_text="this and This and tHIs and THIS"
patt7=r"this"
print(re.findall(patt7,new_text,re.I))  # flag re.I will make the search not case-sensitive

multiline="""this is first line
this is second line
THIS is third line
this is forth line"""
print(re.findall(patt7,multiline,re.M))
print(re.findall(patt7,multiline,re.M|re.I)) # to work with multi-flag you have touse | now I am using them together





############################## working with search and match operations ##############################################

# search look the entire text and gives the first match by default search will search in all the lines in case of multi-lines

long_text="I am1 Marco and I am2 an engineer I am3 Italian and I am4 white"
patt8=r"\bam\d\b"
print(re.search(patt8,long_text))  # object print out it gets value store in a variable and indexes
result=re.search(patt8,long_text) # store in a variable
if result:
    print("my value is:", result.group())
    print("starting index is: ", result.start())
    print("end index is:", result.end()-1)
    print("length: ",result.end()-result.start())
else:
    print("no match found")

# match will only look at the start (0 index), no matter if single line or multiline

print(re.match(patt8,long_text))

#################################### FindIter ######################################################################

long_text="I am1 Marco and I am2 an engineer I am3 Italian and I am4 white"

patt8=r"\bam\d\b"
print(re.findall(patt8,long_text))  # as you can see findall gives a list of result but no info about indexes
print(len(re.findall(patt8,long_text))) # we can use length operation for list to know how many matches there are

print(re.finditer(patt8,long_text)) # you are getting iterable object with info as result

for each_ob in re.finditer(patt8,long_text):  # to retrieve all the info use for loop
    print(each_ob)

# use the syntax as for search and match to get all the required info

for each_ob in re.finditer(patt8,long_text):
    print("my value is:", each_ob.group())
    print("starting index is: ", each_ob.start())
    print("end index is:", each_ob.end() - 1)
    print("length: ", each_ob.end()-each_ob.start())
    print("------------------------------------------")

########################################## Split , sub , and subn operation with RE module ############################

sample_text="I am Marco and I am white and I am employed and I am living in UK"
patt9=r"\bam\b"
print(re.split(patt9,sample_text))  # it will split where am is
# print(help(re.split))  # see additional options split(pattern, string, maxsplit=0, flags=0)
print(re.split(patt9,sample_text,maxsplit=2,flags=re.I))

print(re.sub(patt9,"gin",sample_text)) # it will remove am and use gin instead
# print(help(re.sub))  # see the rules sub(pattern, repl, string, count=0, flags=0)
print(re.sub(patt9,"gin",sample_text,count=1)) # it will remove am and use gin only 1 time as count is 1
print(re.subn(patt9,"gin",sample_text)) # with subn it will give you in the result how many times it did the sub


############################### Compile operation for RE module ###################################################

sample_text="I am Marco and I am white and I am employed and I am living in UK"

my_patt_ob=re.compile(patt9) # I can compile my pattern into re module and create an object
print(my_patt_ob) # my pattern is included in the objet
print(my_patt_ob.findall(sample_text)) # now I can perform all the re operation using my object just passing the string
print(my_patt_ob.split(sample_text))


# whenever you are using same pattern several time in your code try to use compile ##

     ### See all available options for RE at ################
#### https://www.debuggex.com/cheatsheet/regex/python ######

