########################################## MODULES in PYTHON ###################################################################

'''module is a file containing python definitions and statements, that means a module contains python class, functions and variables.
a module can help to compile your code by reusing already defined logics for specific features you want to develop
the key word "import + module name " give you access to predefined classes, functions and variables defined in modules'

## in our examples see ScriptsVariables module that contains the variables we want to re-use
## in the script we want to execute we have to import the module first then we can access the variables as many time as we want
# see the syntax below
'''
import ScriptsVariables   # here we import all the content from the module to our script

print(ScriptsVariables.Ric_List)  # to access the content type modulename."the name of what you want to access defined in module

#### for now make sure the files are in the same location we will see later bout different locations

'''
######################## In python we already have pre-defined modules! #############################################

###################  list the predefined modules use "help("modules") ######################################################
p.s all the listed modules are installed with Python and they can be accessed and used based on your needs 

!!!!!!!!!!!!!!!!!!!!!!!! YOU DO NOT HAVE TO KNOW ALL OF THEM JUST LEARN WHAT IS AVAILABLE WHEN NEEDED AND EXPLORE!!!!!!!!!!!!!!!!!!

also remember as displayed above you can also create your own module call it "your-module.py and import it in your script "import your-module" to reuse code
'''

#### let's explore one like maths

import math
dir(math)  # gives this command to python consolle and get all the operations available for the specific module
help(math) # always on python consolle gives you documentation

print(math.pow(3,2)) # to use power function in math module it needs values to evaluate  """when you see parentesis you are always using a function""""
print(math.pi)  ## pi is variable so it is constant value
print(math.factorial(4))   # factorial number

######################### there are 2 types of modules in python : 1) default modules 2) third party modules  #####################################

# pip install is to get third parties modules for your needs
# pip install boto3       #example to install module work with aws

### the purpose with modules it to re-use the existing code and write your scripts more efficiently


############## another option available is to just import only specific operation from a module to avoid importing the whole module ##################
#################### See below methods to import a module #################################

##### method 1 direct import ########
from math import * # from math import all by using star

print(pow(3,2)) #in this occasion you can access the functions pow directly without specifying module name first

########## method 2 import only what is neede from module with from ########
from math import pow # with this syntax we are only importing power function
from math import pi,pow # or multiple functions together with sngle line

####### method 3 import as alias ######################################
import math as m #  you can create alias name and use the functions by using the alias names to simplify the code

print(m.pow(3,2)) # now you are using m in your script to access maths functions


############ REMEMBER WITH THE HELP PF MODULES YOUR LENGTH OF CODE WILL BE REDUCED ##########################################