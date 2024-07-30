#####################################   OOPS = Object oriented programming concept   ####################################################
"""
programming with Functions it is called procedural programming  (mostly used for scripting)
Python also support object programming concepts   ( mostly used to develop application)
--- WHAT IS OBJECT ORIENTED PROGRAMMING
it's about class, object inheritance, Polymorphism, data abstraction and data encapsulation

to make is simpler OOP It's mainly combination of CLASS and OBJECT


"""

"""
--------------------------- WHAT IS AN OBJET ---------------------------------------------
Object  everything that can exist in real time such as : car, human , jenkins , code , path ect ect 
 
 each object has characteristic and functions like: 
      human = 
          characteristic: age, name , surname, address etc 
          functions: speach, walking , running etc 

Why are we creating objects? 

=== To group related functions (methods)    
It is a concept where characteristic and functions of a real object is packages in a single entity in the code 
Writing your code in Blocks it is called Object programming

=== To create a template or blueprint
in OOP template is a CLASS form the template you can create N number of Objects very easily 
     " ***Methods are functions defined into an Object under Class***"
          *** it always have a default argument self****
    

"""

####################### Class and Object Attributes  ##################################################

# Class is a template/blueprint to create an object
# Class is a combination of attributes and methods
# We can define Attributes for Class and Objects

# -- Example maintain data for 2 employees

class employees:      # first of all I am defining the blueprint for employees (remember this is a templAte, and it won't execute until it is called by the object)
    def get_name_age_salary(self,name,age,salary):  # I am defining method and attributes for the employees ( remember self has to be passed as it will hold the objet name iself for the method to be used)
        self.name=name       # self has to be used to define the variables as those variables belong to the object and self is placeholder for the object
        self.age=age
        self.salary=salary
#       self.display_details() # remember to display a method inside a class you need to use self placeholder to be executed
        return None
    def display_details(self): # we do not need to pass the attributes name, age , salary to the display methods as they are still accessible inside the CLass
        print("Employee Name: ", self.name)
        print("Employee Age: ",self.age)
        print("Employee Salary: ",self.salary)
        return None

###### now we are creating objects by using the Employees template ########

employee_1=employees()  # now I am creating employee "object" 1, and I am assigning the template employees created
employee_2=employees()  # employee_2 object with relevant template employees template now I ve got 2 objects with his own template

# print(dir(employee_1)) # you can see all the methods available for Employee_1

# now I have to pass the attribute name to the employees objects created by using the relevant method

employee_1.get_name_age_salary("Marco","33","£45000") # I am now using the method for the created object to pass the information
employee_2.get_name_age_salary("Iryna","21","£75000") # passing different values to second object by using the same method

# now I can display the values for each employee object created by using display_details method in the class

employee_1.display_details()  # to call the method outside Class object name dot method name
employee_2.display_details()

# to access the variables stored in the object from outside you need to use object name instead of self as in the memory location the valued is stored with "objname.var"
print(employee_1.salary)  # use created object name and variable name to access (self stores the object name created)

"""
 Main concept with OBJECT is that we create separate memery location for each object that keeps the relevant values for each object we are creating
 there won't be any overlap that would happen using procedural programming with functions,
 so we can access variable in the object anytime once it is created
 with an object we are grouping functions to achieve our required task under one name (template)
 we are creating template to create objects under templete we create related functions for the object
"""
######## find how many objects have been created by using this template ################

class employees_new:  # I am creating another Class employees_new for the new requirement
    count=0   # I am defining the variable count outside a method, this variable belongs to the Class and can be accessed externally with class-name.variable
    def get_name_age_salary(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        self.increase_count() # I am calling the method to increase the counter every time object is created
        return None
    def increase_count(self): # I am creating a method to increase the count number every time an object is created
        employees_new.count=employees_new.count+1 # note the variable is defined as employees_new as it belongs to the class
        return None
    def display_details(self): # we do not need to pass the attributes name, age , salary to the display methods as they are still accessible inside the CLass
        print("Employee Name: ", self.name)
        print("Employee Age: ",self.age)
        print("Employee Salary: ",self.salary)
        return None

####### Remember COUNT=Class attribute ######### SELF.VARIABLE=Object attributes ( self is placeholder for object name) ############

employee_3=employees_new() # I am creating new employee_3 object with new template
print("starting count is: ",employees_new.count) # remember count is a variable for the class non the object as it is defined outside a method and can be accessed by using class name
employee_3.get_name_age_salary("Gino","35","£30000")
print("the new variable is: ",employees_new.count) # see the counter is up

print(employees_new.count)  ## class attribute is accessible outside just call class name and attribute

##################################### CONSTRUCTOR OF A CLASS #############################################################

# a Constructor is a special method defined in yur class that gets called by default whenever you create an object for that class

class init:
    def __init__(self):  # syntax to define init constructor method
        print("Constructor method will get executed by default every time")
        return None
display=init() # see the method gets executed by default on creation ( print out displayed)

######################## let's modify the previously created employees_new to implement count with Constructor method #########################

class employees_count:
    count=0
    def __init__(self): # I am creating a constructor method to increase the count number every time an object is created
        employees_count.count=employees_count.count+1
        print("the new counter is: ",employees_count.count)
    def get_name_age_salary(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        return None
    def display_details(self): # we do not need to pass the attributes name, age , salary to the display methods as they are still accessible indide the CLass
        print("Employee Name: ", self.name)
        print("Employee Age: ",self.age)
        print("Employee Salary: ",self.salary)
        return None

employee_4=employees_count() # now init method will execute and counter increase every time you create a new object

print(employees_count.count)

class per(object): #### use this syntax when creating a class as it will be usefully when using inheritance
    def __init__(self,name,surname):  # now I am giving argument to the init method
        self.name=name
        self.surname=surname
        print(f"The given name is:{self.name}\nthe given surname is: {self.surname}")
        return None
person=per("Marco","Moro") # as init method has to arguments now you need to pass them on creation of the object


class per(object): #### use this syntax when creating a class as it will be usefully when using inheritance
    def __init__(self,name,surname):  # now I am giving argument to the init method
        self.name=name
        self.surname=surname
    #    self.display()  # call inside a classe use self
    def display(self):
        print(f"The given name is:{self.name}\nthe given surname is: {self.surname}")
        return None
person=per("Marco","Moro") # as init method has to arguments now you need to pass them on creation of the object

person.display()  ## call outside the class use object
####################################### DESTRUCTOR OF A CLASS ################################################

# Destructors is a method when it gets called the object gets destroyed
# python had got garbage collector that handles memory management automatically
# for this reason destructors are not needed as much as in C++ for example

del person # you can delete an object with del also but destructors are more useful in python

class person(object): #### use this syntax when creating a class as it will be usefully when using inheritance
    def __init__(self,name,surname):  # now I am giving argument to the init method
        self.name=name
        self.surname=surname
        print(f"The given name is:{self.name}\nthe given surname is: {self.surname}")
        return None
    def __del__(self):   # syntax for destructor method
        print("The created object is now deleted")
        return None



person2=person("Gino","Laino")  ## see output the object gets deleted

# Destructor method will be call automatically and destroy the object so the difference between destructor method and del
# is that with destructor Python control the deletion with del you are controlling it

############################## INHERITANCE AND POLYMORPHISM ################################################

# Polymorphism in python allows us to define same methods in different Classes also known as method overriding
# eben by defining the same method in different classes there won't be overlap

# defining 2 different Classes
class JavaVersion(object):
      def __init__(self,version):
          self.javaV= version
          print("java created")
          return None
      def display(self):
          print("the version of java is: ",self.javaV)
          return None
class PythonVersion(object):
    def __init__(self, version):
        self.PythonV = version
        print("python created ")
        return None
    def display(self):
        print("the version of Python is: ", self.PythonV)
        return None
# note both Classes uses same method display

java=JavaVersion("1.3.4")
python=PythonVersion("3.7")
java.display()     # it will only access Display method in java-Version Class
python.display()    # it will only access Display method in Python-Version Class

# thi is called polymorphism as same methods can coexist without interfering

######################################## INHERITANCE #############################################

# inheritance is a mechanism that allows you to create new classes known as child Class that ia bases upon existing Class "Parent Class"

# using the below example the display method is exactly the same, so we can use inheritance by passing Java-Version2 methods to PythonVersion2 Class
class JavaVersion2(object):
    def __init__(self, Version):
        self.Version = Version
        print("java created")
        return None
    def display(self):
        print("Version is: ", self.Version)
class PythonVersion2(JavaVersion2): # in this way I am passing all methods of JavaVersion2 to PythonVersion2
    def __init__(self, Version):
        self.Version = Version
        print("python created ")
        return None
# display method is now inherited from JavaVersion2 Class

#### NOW PythonVesrion2 is Child and JavaVersion2 is Parent ( or superclass) ######

java2=JavaVersion2("1.3.8")
python2=PythonVersion2("3.9")
# see Python2 object can use display method inherited
python2.display()
java2.display()

# Advantage of inheritance is that prevents you to create duplicated code


###################################### ENCAPSULATION #################################################

# we can restrict access of Method and variables outside a class ( syntax is double underscore )

class myself(object):
    def get_name_Surname(self,name,surname):
        self.__name=name  # this variable cannot be accessed outside the Class
        self.surname=surname
        self.__display() # only inside the class you can access the method
        return None
    def __display(self):   # this method cannot be accessed outside the Class
        print(f"The given name is:{self.__name}\nthe given surname is: {self.surname}")
        return None

Marco=myself()
Marco.get_name_Surname("Marco","Moro")
print(Marco.__name) # it won't be accessible outside the Class, see error

########### using OOPS in python we can restrict access to mtheods and variables #########
########## this is called encapsulation and prevent data of being modified #####################







