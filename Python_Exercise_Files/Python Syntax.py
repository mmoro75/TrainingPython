                                  ########## #  Identation and Comments #############

# = comment on single line, not executed when running python programm

'''
comments on multiple lines 
all statements into '''  ''' is not executed when running python program they only serve for commenting 
'''



'''

What is Indentation in Python?
Indentation in Python refers to the whitespaces at the start of the line to indicate a block of code. We can create an indentation using space or tabs.  
When writing Python code, we have to define a group of statements for functions and loops. This is done by properly indenting the statements for that block.

The leading whitespaces (space and tabs) at the start of a line are used to determine the indentation level of the line. 
We have to increase the indent level to group the statements for that code block. Similarly, reduce the indentation to close the grouping.

The four whitespaces or a single tab character at the beginning of a code line are used to create or increase the indentation level. 


'''



if True:
    print("true")
else:
    print("false")


'''
 in other languages block of code is represented by braces i/s on Java curly baces are used see hello world example below
 
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
}


'''

############################  Special Character #####################################################

## Special Characthers in python have to be used only inside ""
## on printing if you want to go next line you can use "\n" meaning new line. see example

print("my name is Iryna")
print ("my surname is Herasimchuck")

print("my name is Marco \nMy surname is Moro")

## \b = cursor back space,  the more \b you add the more spaces you get back

print("hello world")
print("hello \bworld")

## \t = tab , adds a tab in your statement

## \ = escape, meaning you can skip the characther after a good example is

print("this is a \"python\" script") #to escpae the "" inside otherwise cannot be used

# this is a problem when you have to provide a windows path in python. paths contains \ character to avoid this you have to manually add \\ for your path to be valid

print("C:\\Users\\U6017127\\OneDrive - London Stock Exchange Group\\Documents\\TrainingPython")






















